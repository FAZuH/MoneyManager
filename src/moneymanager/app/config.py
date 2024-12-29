class Config:
    UI: str

    @classmethod
    def load(cls) -> None:
        cls.UI = "cli"
