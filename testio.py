# Example of usage
# python testio.py
import os
import sys
import unittest
from interviewio import main, get_namespace


def argv_create_function():
    sys.argv.append('-files')
    sys.argv.append('5')
    sys.argv.append('-size')
    sys.argv.append('1024')
    sys.argv.append('-dir')
    sys.argv.append('Test')
    sys.argv.append('-P')
    sys.argv.append('Hello')
    return sys.argv


class MainTest(unittest.TestCase):
    def test_files_should_exists(self):
        argv_create_function()
        main()
        namespace = get_namespace()
        for i in range(namespace.files):
            self.assertEqual(os.path.exists("Test/" + str(i) + ".txt"), True)

    def test_files_should_have_necessary_size(self):
        namespace = get_namespace()
        for i in range(namespace.files):
            file_path = "Test/" + str(i) + ".txt"
            self.assertEqual(os.stat(file_path).st_size, namespace.size)


if __name__ == "__main__":
    unittest.main()
