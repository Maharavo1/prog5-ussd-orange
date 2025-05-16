from abc import ABC, abstractmethod
from typing import Callable, Optional, Any

class MenuOption(ABC):
    @abstractmethod
    def get_label(self) -> str:
        pass

    @abstractmethod
    def get_action(self) -> Optional[Callable[[], Any]]:
        pass

    @abstractmethod
    def get_sub_menu(self) -> Optional['Menu']:
        pass

class InputOption(MenuOption):
    def __init__(
        self,
        label: str,
        on_input: Callable[[str], Any],
        next_menu: Optional['Menu'] = None,
        validator: Callable[[str], bool] = lambda _: True
    ):
        self.label = label
        self.on_input = on_input
        self.next_menu = next_menu
        self.validator = validator

    def get_label(self) -> str:
        return self.label

    def get_action(self) -> Optional[Callable[[], Any]]:
        return None

    def get_sub_menu(self) -> Optional['Menu']:
        return self.next_menu

    def handle_input(self, input_str: str) -> bool:
        if self.validator(input_str):
            self.on_input(input_str)
            return True
        return False

class MenuOptionImpl(MenuOption):
    def __init__(
        self,
        label: str,
        action: Optional[Callable[[], Any]] = None,
        sub_menu: Optional['Menu'] = None
    ):
        self.label = label
        self.action = action
        self.sub_menu = sub_menu

    def get_label(self) -> str:
        return self.label

    def get_action(self) -> Optional[Callable[[], Any]]:
        return self.action

    def get_sub_menu(self) -> Optional['Menu']:
        return self.sub_menu