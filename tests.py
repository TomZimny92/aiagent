import unittest
from functions.get_file_content import *

class TestGetFilesInfo(unittest.TestCase):
    def testDot(self):
        result = get_file_content("calculator", "lorem.txt")
        print(result)
        self.assertIn('[...File', result)
#        expected = []
#        expected.append("- tests.py: file_size=1349 bytes, is_dir=False")
#        expected.append("- main.py: file_size=563 bytes, is_dir=False")
#        expected.append("- pkg: file_size=4096 bytes, is_dir=True")
#        final_expected = "\n".join(expected)
#        print(final_expected)
#        self.assertEqual(result, final_expected)

    def testFolder(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        print(result)
        self.assertIn('class Calculator', result)
#        expected = []
#        expected.append("- calculator.py: file_size=1779 bytes, is_dir=False")
#        expected.append("- __pycache__: file_size=4096 bytes, is_dir=True")
#        expected.append("- render.py: file_size=774 bytes, is_dir=False")
#        final_expected = "\n".join(expected)
#        print(final_expected)
#        self.assertEqual(result, final_expected)

    def testOutOfBoundsBin(self):
        result = get_file_content("calculator", "/bin/cat")
        print(result)
        self.assertIn('Error:', result)
#        expected = f'Error: Cannot list "/bin" as it is outside the permitted working directory'
#        print(expected)
#        self.assertEqual(result, expected)

    def testOutOfBoundsBack(self):
        result = get_file_content("calculator", "pkg/does_not_exist.py")
        print(result)
        self.assertIn('Error:', result)
#        expected = f'Error: Cannot list "../" as it is outside the permitted working directory'
#        print(expected)
#        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
