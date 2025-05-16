from models.ussd_session import UssdSession
from services.menu_service import setup_menus

def main():
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