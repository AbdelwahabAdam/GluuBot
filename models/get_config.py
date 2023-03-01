async def get_config(self) -> Dict:
   config_as_yaml = self.get_content("config.yml")
   return io_utils.read_yaml(config_as_yaml)