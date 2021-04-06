import unittest
# from unitTestCustomMeta.mock import patch

from custom_meta import CustomMeta


class TestCustomMeta(unittest.TestCase):
    @staticmethod
    def without_magic(lst):
        return list(
            filter(
                lambda x: not (x.startswith('__') and x.endswith('__')),
                lst
            )
        )

    def test_void(self):
        class MyClass(metaclass=CustomMeta):
            pass
        self.assertEqual(TestCustomMeta.without_magic(dir(MyClass)), [])

    def test_vars(self):
        class MyClass(metaclass=CustomMeta):
            x = 10
            y = 25
        self.assertEqual(TestCustomMeta.without_magic(dir(MyClass)),
                         ['custom_x', 'custom_y'])

    def test_funcs(self):
        class MyClass(metaclass=CustomMeta):
            def add_func(self, a, b):
                return a * b
        self.assertEqual(TestCustomMeta.without_magic(dir(MyClass)),
                         ['custom_add_func'])

    def test_private(self):
        class MyClass(metaclass=CustomMeta):
            __priv = 80
        self.assertEqual(TestCustomMeta.without_magic(dir(MyClass)),
                         ['custom__MyClass__priv'])

    def test_inst(self):
        class MyClass(metaclass=CustomMeta):
            __priv = 80

            x = 10
            y = 25

            def add_func(self, a, b):
                return a * b

            def __init__(self):
                self.z = 5

        inst = MyClass()

        print(inst.__dict__)

        self.assertEqual(TestCustomMeta.without_magic(dir(inst)),
                         ['custom_add_func', 'custom__MyClass__priv', 'custom_x', 'custom_y', 'z'])


if __name__ == '__main__':
    unittest.main()
