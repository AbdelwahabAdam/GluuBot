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