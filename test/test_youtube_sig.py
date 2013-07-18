#!/usr/bin/env python

import unittest
import sys

# Allow direct execution
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from youtube_dl.extractor.youtube import YoutubeIE
from helper import FakeYDL

sig = YoutubeIE(FakeYDL())._decrypt_signature

class TestYoutubeSig(unittest.TestCase):
    def test_43_43(self):
        wrong = '5AEEAE0EC39677BC65FD9021CCD115F1F2DBD5A59E4.C0B243A3E2DED6769199AF3461781E75122AE135135'
        right = '931EA22157E1871643FA9519676DED253A342B0C.4E95A5DBD2F1F511DCC1209DF56CB77693CE0EAE'
        self.assertEqual(sig(wrong), right)

    def test_92(self):
        wrong = "F9F9B6E6FD47029957AB911A964CC20D95A181A5D37A2DBEFD67D403DB0E8BE4F4910053E4E8A79.0B70B.0B80B8"
        right = "69B6E6FD47029957AB911A9F4CC20D95A181A5D3.A2DBEFD67D403DB0E8BE4F4910053E4E8A7980B7"
        self.assertEqual(sig(wrong), right)

    def test_90(self):
        wrong = "qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM!@#$%^&*()_-+={[]}|:;?/>.<'`"
        right = "mrtyuioplkjhgfdsazxcvbne1234567890QWER[YUIOPLKJHGFDSAZXCVBNM!@#$%^&*()_-+={`]}|"
        self.assertEqual(sig(wrong), right)

    def test_88(self):
        wrong = "qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM!@#$%^&*()_-+={[]}|:;?/>.<"
        right = "J:|}][{=+-_)(*&;%$#@>MNBVCXZASDFGH^KLPOIUYTREWQ0987654321mnbvcxzasdfghrklpoiuytej"
        self.assertEqual(sig(wrong), right)

    def test_87(self):
        wrong = "qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM!@#$^&*()_-+={[]}|:;?/>.<"
        right = "!?;:|}][{=+-_)(*&^$#@/MNBVCXZASqFGHJKLPOIUYTREWQ0987654321mnbvcxzasdfghjklpoiuytr"
        self.assertEqual(sig(wrong), right)

    def test_86(self):
        wrong = "qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM!@#$%^&*()_-+={[|};?/>.<"
        right = "ertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM!/#$%^&*()_-+={[|};?@"
        self.assertEqual(sig(wrong), right)

    def test_85(self):
        wrong = "qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM!@#$%^&*()_-+={[};?/>.<"
        right = "{>/?;}[.=+-_)(*&^%$#@!MqBVCXZASDFwHJKLPOIUYTREWQ0987654321mnbvcxzasdfghjklpoiuytr"
        self.assertEqual(sig(wrong), right)

    def test_84(self):
        wrong = "qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM!@#$%^&*()_-+={[};?>.<"
        right = "<.>?;}[{=+-_)(*&^%$#@!MNBVCXZASDFGHJKLPOIUYTREWe098765432rmnbvcxzasdfghjklpoiuyt1"
        self.assertEqual(sig(wrong), right)

    def test_83(self):
        wrong = "qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM!#$%^&*()_+={[};?/>.<"
        right = "urty8ioplkjhgfdsazxcvbqm1234567S90QWERTYUIOPLKJHGFDnAZXCVBNM!#$%^&*()_+={[};?/>.<"
        self.assertEqual(sig(wrong), right)

    def test_82(self):
        wrong = "qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKHGFDSAZXCVBNM!@#$%^&*(-+={[};?/>.<"
        right = "Q>/?;}[{=+-(*<^%$#@!MNBVCXZASDFGHKLPOIUY8REWT0q&7654321mnbvcxzasdfghjklpoiuytrew9"
        self.assertEqual(sig(wrong), right)

    def test_81(self):
        wrong = "qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKHGFDSAZXCVBNM!@#$%^&*(-+={[};?/>."
        right = "urty8ioplkjhgfdsazxcvbqm1234567e90QWERTYUIOPLKHGFDSnZXCVBNM!@#$%^&*(-+={[};?/>."
        self.assertEqual(sig(wrong), right)

if __name__ == '__main__':
    unittest.main()
