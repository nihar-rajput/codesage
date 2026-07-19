from pydantic import BaseModel
from pathlib import Path
from app.models.language import Language
 

class Document(BaseModel):
    document_id: str

    repository_id: str

    file_path: Path
    language: Language 

    content_hash:str