# **  /main.py


def func_from_root():
    print('/main.py func_from_root()')


if __name__ == '__main__':
    print("second level print from /main.py, inside if __name__ == '__main__' clause")
    func_from_root()
    from my_submodule import func_from_my_submodule

    func_from_my_submodule()

print('first level print from /main.py')
