import tlogger as tl
import sys
import unittest

tl.log("hoge", "skdjflksdjf")
tl.log("hoge", "skdjflksdjf")
tl.log("hoge", "skdjflksdjf")
tl.log("hoge", "skdjflksdjf")

tl.log("foo", "skdjflksdjf")
tl.log("foo", "skdjflksdjf")
tl.log("piyo", "skdjflksdjf")


class StubOut():
    def __init__(self):
        self.__stdout = []

    def write(self, value):
        self.__stdout.append(str(value))

sys.stdout = StubOut()

class TLoggerTest(unittest.TestCase):

    def __init__(self, *args):
        super(TLoggerTest, self).__init__(*args)

    def test_works(self):
        tl.set_tags("hoge")
        output = tl.log("hoge", "Hello Hoge")
        self.assertRegexpMatches(output, "\[.+\]\s#.+\s-\s.*")
        output = tl.log("foo", "Hello Hoge")
        self.assertEqual(output, None)

if __name__ == '__main__':
    unittest.main()
