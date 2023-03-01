def __init__(self,
             config_path: Optional[Text] = None,
             domain_path: Optional[Text] = None,
             training_data_paths: Optional[Union[List[Text], Text]] = None,
             repository: Text = ""):

    github = Github()
    self.repository = github.get_repo(repository)