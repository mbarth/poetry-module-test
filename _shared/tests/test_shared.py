import unittest

from server_shared import SharedClass, shared_function


class TestDb(unittest.TestCase):

    def test_shared(self):
        # Create an instance of SharedClass
        shared_instance = SharedClass("[From Within _Shared Module]")
        print(shared_instance.greet())

        # Use the shared_function
        result = shared_function(3, 7)
        print(f"Testing from within shared module; The sum is: {result}")
