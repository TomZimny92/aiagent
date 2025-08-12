import unittest
from functions.get_file_content import *
from functions.write_file import *

class TestGetFilesInfo(unittest.TestCase):
    def testDot(self):
        result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(result)
        self.assertIn('Successfully', result)
    def testFolder(self):
        result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print(result)
        self.assertIn('Successfully', result)
    def testDenied(self):
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(result)
        self.assertIn('Error', result)
   # def testDot(self):
   #     result = get_file_content("calculator", "main.py")
   #     print(result)
   #     self.assertIn('def main():', result)

   # def testFolder(self):
   #     result = get_file_content("calculator", "pkg/calculator.py")
   #     print(result)
   #     self.assertIn('def _apply_operator(self, operators, values)', result)

   # def testOutOfBoundsBin(self):
   #     result = get_file_content("calculator", "/bin/cat")
   #     print(result)
   #     self.assertIn('Error:', result)

   # def testOutOfBoundsBack(self):
   #     result = get_file_content("calculator", "pkg/does_not_exist.py")
   #     print(result)
   #     self.assertIn('Error:', result)

if __name__ == "__main__":
    unittest.main()
