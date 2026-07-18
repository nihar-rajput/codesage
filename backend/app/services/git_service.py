from app.config.settings import REPOSITORY_DIR
from git import Repo

class GitService:
    def parse_repository_url(self , url:str):
        parts = url.split("/")
        if len(parts) < 5:
            raise ValueError("invalid GitHub repository URL")
        if parts[2] != "github.com":
            raise ValueError("Only GitHub repository supported")
        owner = parts[3]
        repo = parts[4]
        if repo.endswith(".git"):
            repo = repo[:-4]
        folder_name = f"{owner}__{repo}"
        return owner,repo,folder_name
    
    def clone_repository(self ,url: str):
        owner, repo, folder_name = self.parse_repository_url(url)
        destination = REPOSITORY_DIR/folder_name
        if destination.exists():
            raise FileExistsError("Repository already exists")
        
        Repo.clone_from(url,destination)
        return destination




