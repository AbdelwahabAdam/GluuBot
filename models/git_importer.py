import os
from typing import Optional, Text, Dict, List, Union

from github import Github
from github.ContentFile import ContentFile

import rasa.data
from rasa.core.domain import Domain
from rasa.core.interpreter import RegexInterpreter, NaturalLanguageInterpreter
from rasa.core.training.structures import StoryGraph
from rasa.core.training.dsl import StoryFileReader
from rasa.importers.importer import TrainingDataImporter
from rasa.nlu.training_data import TrainingData
import tempfile
import rasa.utils.io as io_utils


class GitImporter(TrainingDataImporter):

    def __init__(self,
                 config_file: Optional[Text] = None,
                 domain_path: Optional[Text] = None,
                 training_data_paths: Optional[Union[List[Text], Text]] = None,
                 repository: Text = ""):
        github = Github()
        self.repository = github.get_repo(repository)

        data_files = self.get_files_from("data")
        directory = tempfile.mkdtemp()
        for f in data_files:
            with open(os.path.join(directory, f.name), "w+b") as file:
                file.write(f.decoded_content)

        self.story_files, self.nlu_files = rasa.data.get_core_nlu_files([directory])

    def get_files_from(self, directory: Text) -> List[ContentFile]:
        files = []
        for file in self.repository.get_contents(directory):
            if file.type == "file":
                files.append(file)
            else:  # it's another directory
                files += self.get_files_from(file.path)
        return files

    async def get_stories(self,
                          interpreter: "NaturalLanguageInterpreter" = RegexInterpreter(),
                          template_variables: Optional[Dict] = None,
                          use_e2e: bool = False,
                          exclusion_percentage: Optional[int] = None) -> StoryGraph:
        story_steps = await StoryFileReader.read_from_files(
            self.story_files,
            await self.get_domain(),
            interpreter,
            template_variables,
            use_e2e,
            exclusion_percentage,
        )
        return StoryGraph(story_steps)

    async def get_config(self) -> Dict:
        config_as_yaml = self.get_content("config.yml")
        return io_utils.read_yaml(config_as_yaml)

    def get_content(self, path: Text, ) -> Text:
        file = self.repository.get_contents(path)
        return file.decoded_content.decode("utf-8")

    async def get_nlu_data(self, language: Optional[Text] = "en") -> TrainingData:
        from rasa.importers import utils

        return utils.training_data_from_paths(self.nlu_files, language)

    async def get_domain(self) -> Domain:
        domain_as_yaml = self.get_content("domain.yml")
        return Domain.from_yaml(domain_as_yaml)