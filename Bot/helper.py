bot_commands = ['add', 'ban', 'hello', 'help', 'kick']

def log(message: str, use_color: bool, color: str):
    if use_color:
        try:
            import colorama
        except ModuleNotFoundError:
            print("Colorama module was not found! Please install it by pip: pip install requests...")
        if color == "red":
            print(colorama.Fore.RED + message + colorama.Fore.RESET)
        elif color == "green":
            print(colorama.Fore.GREEN + message + colorama.Fore.RESET)
        else:
            print(message)
    
    else:
        print(message)
