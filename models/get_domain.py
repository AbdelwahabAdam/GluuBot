async def get_domain(self) -> Domain:
   domain_as_yaml = self.get_content("domain.yml")
   return Domain.from_yaml(domain_as_yaml)


def get_content(self, path: Text, ) -> Text:
   file = self.repository.get_contents(path)
   return file.decoded_content.decode("utf-8")