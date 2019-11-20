# Example of usage
# python testio.py
import os
import shutil
import sys
import unittest
from TaskThree.interviewio import main, get_namespace, CONST_DEFAULT_DIR, CONST_DEFAULT_SIZE

CONST_DEFAULT_FILE_NAME = "0.txt"


def argv_create_function():
    sys.argv.append("-files")
    sys.argv.append("5")
    sys.argv.append("-size")
    sys.argv.append("1024")
    sys.argv.append("-dir")
    sys.argv.append("TestDirectory")
    sys.argv.append("-P")
    sys.argv.append("Hello")
    return sys.argv


class FirstTest(unittest.TestCase):

    def test_if_argv_is_empty_should_create_default_file(self):
        main()
        default_file_path = CONST_DEFAULT_DIR + "/" + CONST_DEFAULT_FILE_NAME
        print(default_file_path)
        self.assertEqual(os.path.exists(default_file_path), True)
        self.assertEqual(os.stat(default_file_path).st_size, CONST_DEFAULT_SIZE)
        shutil.rmtree(CONST_DEFAULT_DIR)


class SecondTest(unittest.TestCase):

    def test_with_argv_creating_by_function(self):
        argv_create_function()
        namespace = get_namespace()
        main()
        for i in range(namespace.files):
            file_path = namespace.dir + "/" + str(i) + ".txt"
            self.assertEqual(os.path.exists(file_path), True)
            self.assertEqual(os.stat(file_path).st_size, namespace.size)
        shutil.rmtree(namespace.dir)


if __name__ == "__main__":
    unittest.main()
