from models.menu import Menu
from models.input_option import InputOption
import re
import sys

def confirm_code() -> None:
    print("Opération avec succès !")
    print("Fin de la session USSD.")
    sys.exit(0)

def create_confirmation_menu(context: str) -> Menu:
    def validate_code(input_str: str) -> bool:
        if not re.fullmatch(r"\d+", input_str):
            print("Erreur : Le code doit être uniquement composé de chiffres.")
            return False
        if len(input_str) < 4:
            print("Erreur : Le code doit contenir au moins 4 chiffres.")
            return False
        if len(set(input_str)) < 2:
            print("Erreur : Le code doit contenir au moins 2 chiffres différents.")
            return False
        return True

    return Menu(
        f"Entrez le code pour confirmer {context}",
        [InputOption(
            "Saisir le code",
            lambda x: (print(f"Code confirmé : {x}"), confirm_code()),
            None,
            validate_code
        )]
    )

def create_montant_menu(context: str) -> Menu:
    confirmation_menu = create_confirmation_menu(context)

    def validate_amount(input_str: str) -> bool:
        try:
            amount = int(input_str)
            if amount <= 0:
                print("Erreur : Le montant doit être un nombre entier supérieur à 0.")
                return False
            return True
        except ValueError:
            print("Erreur : Veuillez saisir un nombre entier valide.")
            return False

    return Menu(
        f"Entrez le montant pour {context}",
        [InputOption(
            "Saisir le montant",
            lambda x: print(f"Montant saisi : {x}"),
            confirmation_menu,
            validate_amount
        )]
    )

def create_numero_menu(context: str) -> Menu:
    montant_menu = create_montant_menu(context)

    def validate_number(input_str: str) -> bool:
        if not re.fullmatch(r"\d{10}", input_str):
            print("Erreur : Le numéro doit contenir exactement 10 chiffres.")
            return False
        return True

    return Menu(
        f"Entrez le numéro pour {context}",
        [InputOption(
            "Saisir le numéro",
            lambda x: print(f"Numéro saisi : {x}"),
            montant_menu,
            validate_number
        )]
    )
