import os
import platform

from page import Page


class Cli:
    title_fillchar: str = '='
    border_char: str = '*'
    max_width: int = 60
    max_height: int = 40
    inner_width: int = max_width - 4

    @staticmethod
    def clear() -> None:
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    def print_screen(self, p: Page) -> None:
        """Prints the game info to the screen"""

        buffer: str = ''
        inner_width: int = self.max_width - 4
        divider = (self.border_char * self.max_width) + '\n'

        def print_line(line, just='left', fillchar=' '):
            if just == 'left':
                line = line.ljust(inner_width, fillchar)
            elif just == 'right':
                line = line.rjust(inner_width, fillchar)
            elif just == 'center':
                line = line.center(inner_width, fillchar)
            else:
                raise AttributeError

            return self.border_char + ' ' + \
                line + \
                ' ' + self.border_char + '\n'

        # Page Title
        buffer += divider
        buffer += print_line(' ' + p.title + ' ', 'center', self.title_fillchar)
        buffer += divider

        # Main content
        buffer += print_line(p.content)
        buffer += divider

        # Navigation bar
        buffer += print_line(p.navigation, 'center', '.')
        buffer += divider

        # Clear the screen
        # self.clear()

        # Print final buffer
        print(buffer)


if __name__ == '__main__':
    # Testing only

    # Create UI
    cli = Cli()
    page = Page()
    page.title = 'Test'
    page.content = 'TESTING 1 2 3'
    page.navigation = '[q] Quit'
    cli.print_screen(page)

# ''.rjust(10)
# ''.ljust(20)
# ''.center(10, '=')
