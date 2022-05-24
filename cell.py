from colorama import Fore, Back, Style

class Cell:
    def __init__(self):
        self._status = 'Dead'

    def set_dead(self):
        self._status = 'Dead'

    def set_alive(self):
        self._status = 'Alive'

    def is_alive(self):
        if self._status == 'Alive':
            return True
        return False

    def get_print_character(self):
        if self.is_alive():
            return Fore.GREEN + '∎' + Style.RESET_ALL
        return Fore.BLACK + '∎' + Style.RESET_ALL
