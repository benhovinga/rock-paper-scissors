import os
import platform

from page import Page


class UI:
    current_page: Page
    title_fillchar: str = '='

    def __init__(self, width: int = 60, height: int = 40):
        self.max_width = width
        self.max_height = height

    def print_screen(self) -> None:
        """Prints the game info to the screen"""
        # TODO
        buffer: str = ''
        width: int = self.max_width
        page: Page = self.current_page

        # Page Title
        buffer += page.title.center(width, self.title_fillchar)
        buffer += page.content

        # Print final buffer
        print(buffer)

    def set_page_title(self, title) -> None:
        # TODO
        pass

    @staticmethod
    def clear() -> None:
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')


# ''.rjust(10)
# ''.ljust(20)
# ''.center(10, '=')
