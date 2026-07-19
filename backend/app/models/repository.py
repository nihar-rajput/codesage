from pydantic import BaseModel
from pathlib import Path
from datetime import datetime

class Repository(BaseModel):
    repository_id: str

    name: str
    url: str

    branch:str
    local_path: Path 

    commit_hash: str

    indexed_at: datetime
