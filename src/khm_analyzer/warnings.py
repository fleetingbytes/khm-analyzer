class KhmWarning(UserWarning):
    pass


class InvalidXmlCorrectedWarning(KhmWarning):
    def __init__(self, wrong: str, corrected: str, line: int) -> None:
        message = f"corrected {wrong} -> {corrected} on line {line}"
        super().__init__(message)
        self.wrong = wrong
        self.corrected = corrected
        self.line = line
