from senders import sender
import unittest
from unittest.mock import patch


class testSenders(unittest.TestCase):
    def test_no_data_entered(self):
        self.assertEqual(sender([]), TypeError)

    def test_one_input_was_entered(self):
        self.assertEqual(sender(["a", ]), TypeError)

    def test_two_input_was_entered(self):
        self.assertEqual(sender(["a", "b"]), TypeError)

    def test_all_input_was_entered(self):
        self.assertEqual(sender(["a", "b", "c"]), 0)
