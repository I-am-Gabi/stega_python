from parser_arg.validator import *
import unittest


class TestValidatorMethods(unittest.TestCase):
    def test_BadArgumentValidatorFile(self):
        self.assertEqual(validator_file(""), False)
        self.assertEqual(validator_file("../fileError.error"), False)
        self.assertRaises(TypeError, validator_file(None))

    def test_GoodArgumentValidatorFile(self):
        self.assertEqual(validator_file("../resources/images/face.png"), True)

    def test_BadArgumentValidatorPattern(self):
        self.assertEqual(validator_pattern(""), False)
        self.assertEqual(validator_pattern("error"), False)
        self.assertRaises(TypeError, validator_pattern(None))

    def test_GoodArgumentValidatorPattern(self):
        self.assertEqual(validator_pattern("direct"), True)
        self.assertEqual(validator_pattern("reverse"), True)

    def test_BadArgumentValidatorChannels(self):
        self.assertEqual(validator_channels(""), False)
        self.assertEqual(validator_channels("error"), False)
        self.assertEqual(validator_channels(["gray", "red"]), False)
        self.assertEqual(validator_channels(["red", "yellow"]), False)
        self.assertRaises(TypeError, validator_channels(None))

    def test_GoodArgumentValidatorChannels(self):
        self.assertEqual(validator_channels(["red"]), True)
        self.assertEqual(validator_channels(["green"]), True)
        self.assertEqual(validator_channels(["blue"]), True)

    def test_BadArgumentValidatorFileSignature(self):
        self.assertEqual(validator_file_signature("[]"), False)
        self.assertEqual(validator_file_signature("[error]"), False)
        self.assertRaises(TypeError, validator_file_signature(None))

    def test_GoodArgumentValidatorFileSignature(self):
        self.assertEqual(validator_file_signature("../resources/images/face.png"), True)


if __name__ == '__main__':
    unittest.main()
