_stats = f'/MYpackage/__init__.py\n\t__name__: "{__name__}"\n\t__file__: "{__file__}"\n\t__package__: "{__package__}"'
try:
    from .term import bold

    try:
        print(bold(f'BOLD\n{_stats}\n\t__path__: "{__path__}"'))
    except NameError:
        print(bold(_stats))

except ValueError:
    try:
        print(f'BOLD\n{_stats}\n\t__path__: "{__path__}"')
    except NameError:
        print(_stats)

from .SUBpackage import other_func

other_func()
