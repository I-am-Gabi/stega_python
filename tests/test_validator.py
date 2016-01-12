import unittest, sys
sys.path.insert(0, '../')
from parser_arg.validator import validator_file


class TestValidatorMethods(unittest.TestCase):

  def test_EmptyArgument(self):
      self.assertEqual(validator_file(""), False)

  def test_NullArgument(self):
      self.assertRaises(TypeError, validator_file(None))

  def test_GoodArgument(self):
      self.assertEqual(validator_file("../resources/face.png"), True)

if __name__ == '__main__':
    unittest.main()