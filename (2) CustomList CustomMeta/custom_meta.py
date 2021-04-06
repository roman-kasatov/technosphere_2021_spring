class CustomMeta(type):
    """why pylint takes CustomMeta() as an error?"""
    @staticmethod
    def is_magic(name):
        return name.startswith('__') and name.endswith('__')

    def __new__(cls, name, bases, dct):
        new_dct = {'custom_' + attr: dct[attr]
                   for attr in dct if not CustomMeta.is_magic(attr)}

        return super().__new__(cls, name, bases, new_dct)


if __name__ == '__main__':
    class A(metaclass=CustomMeta):
        x = 3
        y = 5
        __z = 8

        def mul(self, a, b):
            return a * b

    print(dir(A))
