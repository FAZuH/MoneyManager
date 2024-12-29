from moneymanager.app._ui_option import UiOption


class Config:
    UI: UiOption

    @classmethod
    def load(cls) -> None:
        cls.UI = UiOption.CLI
