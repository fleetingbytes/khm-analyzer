from pathlib import Path


class KhmWarning(UserWarning):
    pass


class InvalidXmlCorrectedWarning(KhmWarning):
    def __init__(self, wrong: str, corrected: str, line: int) -> None:
        message = f"Corrected {wrong} -> {corrected} on line {line}"
        super().__init__(message)
        self.wrong = wrong
        self.corrected = corrected
        self.line = line


class FileNotCorrectedWarning(KhmWarning):
    def __init__(self, path: Path) -> None:
        message = f"Could not correct file {path}"
        super().__init__(message)
        self.path = path
