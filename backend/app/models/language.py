from enum import Enum

class Language(str,Enum):
    PYTHON = "python"
    JAVA = "java"
    CPP = "cpp"
    JAVASCRIPT = "javascript"
    UNKNOWN = "unknown"