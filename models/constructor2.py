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