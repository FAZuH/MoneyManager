from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from moneymanager.app.app import App


class BaseController(ABC):
    def __init__(self, app: App) -> None:
        self._app = app

    @abstractmethod
    def run(self) -> None:
        """Runs the controller."""

    @property
    def app(self) -> App:
        return self._app
