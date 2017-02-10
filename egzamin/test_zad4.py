import unittest

from zad4 import R

class TestR(unittest.TestCase):
    def setUp(self):
        self.r = R(1)
    def testArabskaNaRzymska1995(self):
        self.r.l = 1995
        assert self.r.toRoman() == "MCMXCV", "zle konwertuje liczbe 1995"
    def testArabskaNaRzymska3338(self):
        self.r.l = 3338
        assert self.r.toRoman() == "MMMCCCXXXVIII", "zle konwertuje liczbe 3338"
    def testArabskaNaRzymska95(self):
        self.r.l = 95
        assert self.r.toRoman() == "XCV", "zle konwertuje liczbe 95"
    def testRzymskaNaArabskaI(self):
        self.r.l = "I"
        assert self.r.fromRoman() == 1, "zle konwertuje liczbe I"
    def testRzymskaNaArabskaX(self):
        self.r.l = "X"
        assert self.r.fromRoman() == 10, "zle konwertuje liczbe X"
    def testRzymskaNaArabskaIX(self):
        self.r.l = "IX"
        assert self.r.fromRoman() == 9, "zle konwertuje liczbe IX"
    def testRzymskaNaArabskaXVI(self):
        self.r.l = "XVI"
        assert self.r.fromRoman() == 16, "zle konwertuje liczbe XVI"
    def testRzymskaNaArabskaXXVI(self):
        self.r.l = "XXVI"
        assert self.r.fromRoman() == 26, "zle konwertuje liczbe XXVI"
    def testRzymskaNaArabskaXLIV(self):
        self.r.l = "XLIV"
        assert self.r.fromRoman() == 44, "zle konwertuje liczbe 44"
    def testRzymskaNaArabskaMCCVI(self):
        self.r.l = "MCCLVI"
        assert self.r.fromRoman() == 1256, "zle konwertuje liczbe 1206"
    def testRzymskaNaArabskaMCMXCV(self):
        self.r.l = "MCMXCV"
        assert self.r.fromRoman() == 1995, "zle konwertuje liczbe MCMXCV"
    def testRzymskaNaArabskaXCV(self):
        self.r.l = "XCV"
        assert self.r.fromRoman() == 95, "zle konwertuje liczbe 95"
    def testRzymskaNaArabskaCMXCV(self):
        self.r.l = "CMXCV"
        assert self.r.fromRoman() == 995, "zle konwertuje liczbe 995"

if __name__ == "__main__":
    unittest.main()