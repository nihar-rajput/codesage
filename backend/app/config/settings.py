from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
REPOSITORY_DIR = BASE_DIR/"repositories"
REPOSITORY_DIR.mkdir(parents=True,exist_ok=True)

IGNORED_DIRECTORIES = {
    ".git",
    "node_modules",
    "__pycache__",
    "venv",
    ".venv",
    "build",
    "dist",
    "target",
}

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB
TEXT_SAMPLE_SIZE = 4096           # 4 KB