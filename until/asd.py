class Foo(object):
    staticField = "old boy"

    def __init__(self):
        self.name = 'wupeiqi'

    def func(self):
        return 'func'

    @staticmethod
    def bar():
        return 'bar'


print(getattr(Foo, 'staticField'))
print(getattr(Foo, 'func'))
print(getattr(Foo, 'bar'))
a = Foo()
print(getattr(a, 'name'))
print(getattr(a, 'staticField'))
print(getattr(a, 'func'))
print(getattr(a, 'bar'))