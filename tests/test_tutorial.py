import unittest
import itertools
from unittest.mock import Mock, call


class MockTest(unittest.TestCase):

    def setUp(self) -> None:
        self.mock = Mock()

    def test_mock_has_calls(self):
        self.mock.s.hello(23).stuff.howdy('a','b','c')
        self.mock.assert_has_calls([
            call.s.hello().stuff.howdy('a','b','c')
        ])
        print(self.mock.mock_calls)  # [call.s.hello(23), call.s.hello().stuff.howdy('a', 'b', 'c')]
        # mock_calls to lista wszystkich atrap
        print(self.mock.mock_calls.index(call.s.hello(23)))
        print(self.mock.mock_calls.index(call.s.hello(23).stuff.howdy('a','b','c')))

    def test_return_value(self):
        self.mock.o.return_value = "Hello"  # always return Hello no matter params
        self.assertEqual(self.mock.o("mateusz"), "Hello")
        # print(self.mock.o())  Hello
        # print(self.mock.o("Mateusz")) Hello

    def test_non_existing_prop(self):
        del self.mock.x
        with self.assertRaises(AttributeError):
            self.mock.x += 1  # raises Exception because it doesn't exist

    def test_existing_prop(self):
        self.mock.x = 5
        self.assertEqual(self.mock.x, 5)

    def test_side_effect(self):
        self.mock.get_hour.side_effect = [1, 2, 3]  # list of possible return values
        print(self.mock.get_hour())  # za pierwszym wywolaniem zwraca 1
        print(self.mock.get_hour())  # za drugim 2 itd
        print(self.mock.get_hour())  # 3
        # jezeli tylko dwa byly w side effect to pojawi sie StopIteration Exception za trzecim razem
        # wtedy potrzebujemy itertools.count()

    def test_itertools(self):
        self.mock.get_hour.side_effect = itertools.count(5, 10)  # by default 0,1,2,3,4 mozna ustawic np. tylko start
        # start i step 5 15, 25, itd.
        # tylko start to step by default is 1
        print(self.mock.get_hour())  # zwaraca 0 dla count()
        print(self.mock.get_hour())  # 1
        print(self.mock.get_hour())  # 2 itd.
        print(self.mock.get_hour())
        print(self.mock.get_hour())


    def test_mock_instead_return_value_raise_exception(self):
        self.mock.get_hour.side_effect = [1, 2, 3, ValueError(4)]
        self.mock.get_hour()
        self.mock.get_hour()
        self.mock.get_hour()
        with self.assertRaises(ValueError):
            self.mock.get_hour()  # czwarte wywolanie wyrzuci blad




if __name__ == "__main__":
    unittest.main()
