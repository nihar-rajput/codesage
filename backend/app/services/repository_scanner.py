from pathlib import Path
import os
from app.config.settings import (
    IGNORED_DIRECTORIES,
    MAX_FILE_SIZE,
    TEXT_SAMPLE_SIZE
)
from collections.abc import Iterator

class RepositoryScanner:
    """Scans a repository and return all indexable files"""
    def scan_repository(self, repository_path : Path)-> Iterator[Path]:
        """Generator scans file and immediatly sends it to next process"""

        for root, dirs, filenames in os.walk(repository_path):
        
            dirs[:] = [
                d for d in dirs
                if not self._should_skip_directory(d)]
            
            for filename in filenames:
                file_path = Path(root)/filename

                if self._is_indexable_file(file_path):
                    yield file_path


    def _should_skip_directory(self, directory: str) -> bool:
        return directory in IGNORED_DIRECTORIES
    

    def _is_indexable_file(self, file_path: Path) -> bool:
        if not file_path.is_file():
            return False

        if file_path.stat().st_size > MAX_FILE_SIZE:
            return False
    
        try:
            with file_path.open("rb") as f:
                sample = f.read(TEXT_SAMPLE_SIZE)
                sample.decode("utf-8")
            return True
        
        except (UnicodeDecodeError,OSError):
            return False