from abc import ABC, abstractmethod
from typing import Callable, Optional, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .menu import Menu

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
