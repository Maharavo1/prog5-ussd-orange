from models.menu import Menu
from models.menu_option import InputOption, MenuOptionImpl
import re
import sys

def confirm_code() -> None:
    print("Operation avec succès !")
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

def setup_menus() -> Menu:
    # Création des sous-menus
    transfer_to_menu = Menu(
        "Transférer vers :",
        [
            MenuOptionImpl("Orange Money", None, create_numero_menu("Transfert Orange Money")),
            MenuOptionImpl("Airtel Money", None, create_numero_menu("Transfert Airtel Money")),
            MenuOptionImpl("Mvola", None, create_numero_menu("Transfert Mvola")),
            MenuOptionImpl("IZY CASH", None, create_numero_menu("Transfert IZY CASH")),
            MenuOptionImpl("Banque & Microfinance", None, create_numero_menu("Transfert Banque")),
            MenuOptionImpl("Faire livrer du cash", None, create_numero_menu("Livraison Cash"))
        ]
    )

    orange_service_menu = Menu(
        "Services Orange :",
        [
            MenuOptionImpl("Achat de crédit", None, create_numero_menu("Achat de crédit")),
            MenuOptionImpl("Achat de forfaits Internet", None, create_numero_menu("Forfait Internet")),
            MenuOptionImpl("Achat de forfaits Appels", None, create_numero_menu("Forfait Appels")),
            MenuOptionImpl("Achat de forfaits SMS", None, create_numero_menu("Forfait SMS")),
            MenuOptionImpl("Achat de forfaits Illimix", None, create_numero_menu("Forfait Illimix"))
        ]
    )

    payment_partners_menu = Menu(
        "Paiements & Partenaires :",
        [
            MenuOptionImpl("Paiement marchand", None, create_numero_menu("Paiement marchand")),
            MenuOptionImpl("Paiement de factures - JIRAMA", None, create_numero_menu("Facture JIRAMA")),
            MenuOptionImpl("Paiement de factures - Canal+", None, create_numero_menu("Facture Canal+")),
            MenuOptionImpl("Paiement de factures - Autres", None, create_numero_menu("Autres factures")),
            MenuOptionImpl("Paiement de scolarité", None, create_numero_menu("Paiement scolarité")),
            MenuOptionImpl("Paiement de services divers", None, create_numero_menu("Paiement divers"))
        ]
    )

    financial_services_menu = Menu(
        "Services Financiers :",
        [
            MenuOptionImpl("M-Kajy - Ouvrir un compte épargne", None, create_numero_menu("Ouvrir compte épargne")),
            MenuOptionImpl("M-Kajy - Faire un dépôt", None, create_numero_menu("Dépôt épargne")),
            MenuOptionImpl("M-Kajy - Faire un retrait", None, create_numero_menu("Retrait épargne")),
            MenuOptionImpl("M-Kajy - Demander un prêt", None, create_numero_menu("Demander prêt")),
            MenuOptionImpl("M-Kajy - Consulter le solde", None, create_numero_menu("Solde épargne")),
            MenuOptionImpl("M-Kajy - Consulter mini relevé", None, create_numero_menu("Mini relevé épargne")),
            MenuOptionImpl("Paiement de salaire", None, create_numero_menu("Paiement salaire")),
            MenuOptionImpl("Assurance mobile", None, create_numero_menu("Assurance mobile"))
        ]
    )

    account_menu = Menu(
        "Mon Compte :",
        [
            MenuOptionImpl("Consulter le solde", None, create_numero_menu("Solde compte")),
            MenuOptionImpl("Changer le code secret", None, create_numero_menu("Changer code")),
            MenuOptionImpl("Consulter le mini relevé", None, create_numero_menu("Mini relevé")),
            MenuOptionImpl("Réinitialiser le code secret", None, create_numero_menu("Réinit code"))
        ]
    )

    visa_card_menu = Menu(
        "Carte VISA Akory :",
        [
            MenuOptionImpl("Demander une carte", None, create_numero_menu("Demande carte")),
            MenuOptionImpl("Activer la carte", None, create_numero_menu("Activer carte")),
            MenuOptionImpl("Consulter le solde de la carte", None, create_numero_menu("Solde carte")),
            MenuOptionImpl("Recharger la carte", None, create_numero_menu("Recharge carte"))
        ]
    )

    karama_menu = Menu(
        "Compte Karama :",
        [
            MenuOptionImpl("Ouvrir un compte Karama", None, create_numero_menu("Ouvrir Karama")),
            MenuOptionImpl("Consulter le solde", None, create_numero_menu("Solde Karama")),
            MenuOptionImpl("Effectuer un dépôt", None, create_numero_menu("Dépôt Karama")),
            MenuOptionImpl("Effectuer un retrait", None, create_numero_menu("Retrait Karama"))
        ]
    )

    retrait_menu = Menu(
        "Retrait :",
        [
            MenuOptionImpl("Retrait d'argent", None, create_numero_menu("Retrait d'argent")),
            MenuOptionImpl("Générer un code de retrait", None, create_numero_menu("Générer code")),
            MenuOptionImpl("Consulter les points de retrait", None, create_numero_menu("Points retrait"))
        ]
    )

    main_menu = Menu(
        "Menu Principal :",
        [
            MenuOptionImpl("Transfert d'argent", None, transfer_to_menu),
            MenuOptionImpl("Service Orange", None, orange_service_menu),
            MenuOptionImpl("Paiements & Partenaires", None, payment_partners_menu),
            MenuOptionImpl("Services financiers", None, financial_services_menu),
            MenuOptionImpl("Mon compte", None, account_menu),
            MenuOptionImpl("Carte VISA Akory", None, visa_card_menu),
            MenuOptionImpl("Compte Karama", None, karama_menu),
            MenuOptionImpl("Retrait", None, retrait_menu)
        ]
    )

    # Définir les parents
    transfer_to_menu.set_parent(main_menu)
    orange_service_menu.set_parent(main_menu)
    payment_partners_menu.set_parent(main_menu)
    financial_services_menu.set_parent(main_menu)
    account_menu.set_parent(main_menu)
    visa_card_menu.set_parent(main_menu)
    karama_menu.set_parent(main_menu)
    retrait_menu.set_parent(main_menu)

    return main_menu