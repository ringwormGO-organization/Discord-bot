bot_commands = ['add', 'ban', 'hello', 'help', 'kick']

def log(message: str, use_color: bool, color: str):
    if use_color:
        import colorama
        if color == "red":
            print(colorama.Fore.RED + message + colorama.Fore.RESET)
        elif color == "green":
            print(colorama.Fore.GREEN + message + colorama.Fore.RESET)
        else:
            print(message)
    
    else:
        print(message)