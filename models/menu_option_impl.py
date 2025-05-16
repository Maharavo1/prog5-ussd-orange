from typing import Callable, Optional, Any
from .menu_option import MenuOption
from .menu import Menu

class MenuOptionImpl(MenuOption):
    def __init__(
        self,
        label: str,
        action: Optional[Callable[[], Any]] = None,
        sub_menu: Optional[Menu] = None
    ):
        self.label = label
        self.action = action
        self.sub_menu = sub_menu

    def get_label(self) -> str:
        return self.label

    def get_action(self) -> Optional[Callable[[], Any]]:
        return self.action

    def get_sub_menu(self) -> Optional[Menu]:
        return self.sub_menu
