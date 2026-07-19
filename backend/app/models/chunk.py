from pydantic import BaseModel
from pathlib import Path
from app.models.language import Language
from typing import Optional

class Chunk(BaseModel):
    #identity
    chunk_id: str

    #Repository and document
    document_id: str

    #code hierarchy
    symbol_id: str | None = None
    symbol_name: str | None = None

    #content
    content: str

    #chunk information
    chunk_index: int
    total_chunks: int
    
    #source location
    start_line: int
    end_line: int
