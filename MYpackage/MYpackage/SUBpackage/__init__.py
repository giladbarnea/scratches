from ..term import bold

_stats = f'/MYpackage/SUBpackage/__init__.py\n\t__name__: "{__name__}"\n\t__file__: "{__file__}"\n\t__package__: "{__package__}"'
try:
    print(bold(f'{_stats}\n\t__path__: "{__path__}"'))
except NameError:
    print(bold(_stats))


def other_func():
    print(bold('MYpackage/SUBpackage/__init__.py other_func()'))
