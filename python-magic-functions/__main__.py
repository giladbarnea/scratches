class GetSet:
    def __get__(self, instance, owner):
        print(f'GetSet.__get__, instance: {instance}, owner: {owner}. returning instance.hobby')
        return instance.hobby

    def __set__(self, instance, value):
        print(f'GetSet.__set__, instance: {instance}, value: {value}')
        instance.hobby = value


class Foo:
    # / This won't work under __init__ with self.getset etc
    hobby = "drawing"
    getset = GetSet()


if __name__ == '__main__':
    foo = Foo()
    print(f'foo.getset: {foo.getset}')
