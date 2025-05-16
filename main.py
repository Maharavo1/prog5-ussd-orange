from models.menu import Menu
from models.menu_option import MenuOptionImpl
from services.menu_service import create_numero_menu

def setup_menus() -> Menu:
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


    main_menu = Menu(
        "Menu Principal :",
        [
            MenuOptionImpl("Transfert d'argent", None, transfer_to_menu),
            MenuOptionImpl("Service Orange", None, orange_service_menu),
           
        ]
    )

 
    transfer_to_menu.set_parent(main_menu)
    orange_service_menu.set_parent(main_menu)


    return main_menu

def main():
    from models.ussd_session import UssdSession
    
    main_menu = setup_menus()
    session = UssdSession(main_menu)

    while True:
        print(session.display_current_menu())
        user_input = input("Votre choix (ou tapez 'exit') : ")
        
        if user_input.lower() == 'exit':
            print("Au revoir !")
            break
            
        session.handle_input(user_input)

if __name__ == "__main__":
    main()