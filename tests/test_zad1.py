import unittest
from unittest.mock import mock_open, patch
from src.sample.File import *


class MockFilesTest(unittest.TestCase):

    def setUp(self) -> None:
        self.mock = File()

    def test_opening_file(self):
        with patch("builtins.open", mock_open(read_data="data")) as mock_file:
            assert open("path/to/open").read() == "data"
            mock_file.assert_called_with("path/to/open")


if __name__ == "__main__":
    unittest.main()