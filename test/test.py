#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unittest
from ..src import main


class TestMain(unittest.TestCase):
    """
    Only tests valid data since main is not designed to handle
    invalid input.
    """

    def test__replace_digraphs__with_valid_data(self):
        self.assertEqual(["s", "h", "a"], main._replace_digraphs(["し", "ゃ"]))
        self.assertEqual(["n", "y", "a"], main._replace_digraphs(["に", "ゃ"]))
        self.assertEqual(["b", "y", "o"], main._replace_digraphs(["び", "ょ"]))
        self.assertEqual(["g", "y", "u"], main._replace_digraphs(["ぎ", "ゅ"]))
        self.assertEqual(["c", "h", "a"], main._replace_digraphs(["チ", "ャ"]))
        self.assertEqual(["c", "h", "u"], main._replace_digraphs(["チ", "ュ"]))
        self.assertEqual(["n", "y", "u"], main._replace_digraphs(["ニ", "ュ"]))
        self.assertEqual(["j", "o", "j", "o"], main._replace_digraphs(["ジ", "ョ", "ジ", "ョ"]))
        self.assertEqual(["k", "y", "a", "き"], main._replace_digraphs(["き", "ゃ", "き"]))

    def test__replace_monographs__with_valid_data(self):
        self.assertEqual(["s", "h", "i"], main._replace_monographs(["し"]))
        self.assertEqual(["n", "i"], main._replace_monographs(["に"]))
        self.assertEqual(["b", "i"], main._replace_monographs(["び"]))
        self.assertEqual(["g", "i"], main._replace_monographs(["ぎ"]))
        self.assertEqual(["n", "i"], main._replace_monographs(["ニ"]))
        self.assertEqual(["j", "i"], main._replace_monographs(["ジ"]))
        self.assertEqual(["k", "i", "k", "i"], main._replace_monographs(["き", "き"]))
        self.assertEqual(["j", "o", "j", "o", "j", "i"], main._replace_monographs(["j", "o", "j", "o", "ジ"]))

    def test__replace_choonpu__with_valid_data(self):
        self.assertEqual(["z", "a", "a", "s", "o"], main._replace_choonpu(["z", "a", "ー", "s", "o"]))
        self.assertEqual(["d", "a", "a", "s", "o"], main._replace_choonpu(["d", "a", "ー", "s", "o"]))
        self.assertEqual(["r", "e", "e", "s", "o"], main._replace_choonpu(["r", "e", "ー", "s", "o"]))
        self.assertEqual(["a", "a", "s", "o"], main._replace_choonpu(["a", "ー", "s", "o"]))
        self.assertEqual(["b", "i", "i", "s", "o"], main._replace_choonpu(["b", "i", "ー", "s", "o"]))
        self.assertEqual(["b", "o", "o", "s", "o"], main._replace_choonpu(["b", "o", "ー", "s", "o"]))

    def test__replace_sokuon__with_valid_data(self):
        self.assertEqual(["s", "o", "z", "z", "a"], main._replace_sokuon(["s", "o", "っ", "z", "a"]))
        self.assertEqual(["s", "o", "z", "z", "a"], main._replace_sokuon(["s", "o", "ッ", "z", "a"]))
        self.assertEqual(["s", "o", "d", "d", "a"], main._replace_sokuon(["s", "o", "っ", "d", "a"]))
        self.assertEqual(["s", "o", "d", "d", "a"], main._replace_sokuon(["s", "o", "ッ", "d", "a"]))
        self.assertEqual(["s", "o", "r", "r", "e"], main._replace_sokuon(["s", "o", "っ", "r", "e"]))
        self.assertEqual(["s", "o", "r", "r", "e"], main._replace_sokuon(["s", "o", "ッ", "r", "e"]))
        self.assertEqual(["s", "o", "b", "b", "a"], main._replace_sokuon(["s", "o", "っ", "b", "a"]))
        self.assertEqual(["s", "o", "b", "b", "a"], main._replace_sokuon(["s", "o", "ッ", "b", "a"]))

    def test__translate_kana_to_romaji__with_valid_data(self):
        self.assertEqual("", main.translate_kana_to_romaji(""))
        self.assertEqual("doumo arigatou gozaimasu", main.translate_kana_to_romaji("どうも ありがとう ございます"))
        self.assertEqual("sayonara", main.translate_kana_to_romaji("さよなら"))
        self.assertEqual("meruto", main.translate_kana_to_romaji("メルト"))
        self.assertEqual("baiohazaado", main.translate_kana_to_romaji("バイオハザード"))
        self.assertEqual("bakabaka", main.translate_kana_to_romaji("ばかばか"))
        self.assertEqual("poketto monsutaa", main.translate_kana_to_romaji("ポケット モンスター"))
        self.assertEqual("atogatari", main.translate_kana_to_romaji("あとがたり"))
        self.assertEqual("20. haatoandaabureedo.mp3", main.translate_kana_to_romaji("20. ハートアンダーブレード.mp3"))
        self.assertEqual("Ew, English", main.translate_kana_to_romaji("Ew, English"))
