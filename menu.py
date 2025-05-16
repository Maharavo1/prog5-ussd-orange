from typing import List, Optional
from models.menu_option import MenuOption

class Menu:
    def __init__(self, title: str, options: List[MenuOption]):
        self.title = title
        self.options = options
        self.parent: Optional[Menu] = None
        
    def set_parent(self, parent: 'Menu') -> None:
        self.parent = parent
        
    def get_title(self) -> str:
        return self.title
        
    def get_options(self) -> List[MenuOption]:
        return self.options
        
    def get_parent(self) -> Optional['Menu']:
        return self.parent