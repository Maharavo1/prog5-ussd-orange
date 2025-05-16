from typing import Optional
from models.menu import Menu
from models.menu_option import InputOption, MenuOption
import sys

class UssdSession:
    def __init__(self, start_menu: Menu):
        self.current_menu = start_menu
        self.waiting_input_option: Optional[InputOption] = None
        
    def display_current_menu(self) -> str:
        if self.waiting_input_option is not None:
            return f"\n{self.waiting_input_option.get_label()} :"
            
        menu_text = [f"\n{self.current_menu.get_title()}\n"]
        for i, option in enumerate(self.current_menu.get_options(), 1):
            menu_text.append(f"{i}. {option.get_label()}\n")
            
        options_count = len(self.current_menu.get_options())
        if self.current_menu.get_parent() is not None:
            menu_text.append(f"{options_count + 1}. Retour\n")
            menu_text.append(f"{options_count + 2}. Quitter\n")
        else:
            menu_text.append(f"{options_count + 1}. Quitter\n")
            
        return "".join(menu_text)
        
    def handle_input(self, input_str: str) -> None:
        if self.waiting_input_option is not None:
            if self.waiting_input_option.handle_input(input_str):
                if self.waiting_input_option.get_sub_menu() is not None:
                    self.current_menu = self.waiting_input_option.get_sub_menu()
                self.waiting_input_option = None
            return
            
        try:
            choice = int(input_str)
            self._process_choice(choice)
        except ValueError:
            print("Entrée invalide. Veuillez saisir un numéro.")
            
    def _process_choice(self, choice: int) -> None:
        options_count = len(self.current_menu.get_options())
        has_parent = self.current_menu.get_parent() is not None
        
        quit_option = options_count + 2 if has_parent else options_count + 1
        back_option = options_count + 1 if has_parent else -1
        
        if choice == quit_option:
            print("Fin de la session USSD.")
            sys.exit(0)
        elif has_parent and choice == back_option:
            self.current_menu = self.current_menu.get_parent()
        elif 1 <= choice <= options_count:
            option = self.current_menu.get_options()[choice - 1]
            if isinstance(option, InputOption):
                self.waiting_input_option = option
            elif option.get_sub_menu() is not None:
                self.current_menu = option.get_sub_menu()
            elif option.get_action() is not None:
                option.get_action()()
        else:
            print("Choix invalide.")