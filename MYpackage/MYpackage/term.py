_stats = f'term.py\n\t__name__: "{__name__}"\n\t__file__: "{__file__}"\n\t__package__: "{__package__}"'
try:
    print(f'{_stats}\n\t__path__: "{__path__}"')
except NameError:
    print(_stats)


def bold(s):
    """Prints things in bold."""
    return '\033[1m{0}\033[0m'.format(s)
