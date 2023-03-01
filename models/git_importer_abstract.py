class GitImporter(TrainingDataImporter):
   async def get_stories(self,
                         **kwargs: Dict):
       pass

   async def get_nlu_data(self, **kwargs: Dict) -> TrainingData:
       pass

   async def get_domain(self) -> Domain:
       pass

   async def get_config(self) -> Dict:
       pass