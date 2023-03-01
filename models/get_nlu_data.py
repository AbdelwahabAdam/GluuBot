async def get_nlu_data(self, language: Optional[Text] = "en") -> TrainingData:
   from rasa.importers import utils

   return utils.training_data_from_paths(self.nlu_files, language)