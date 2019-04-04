#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys

_num_files_ignored: int = 0
_num_rename_success: int = 0
_num_rename_failure: int = 0
_filenames_failed = []

_KANA_DIGRAPH_DICT = {
    # map digraph hiragana to romaji
    "きゃ": "kya", "きゅ": "kyu", "きょ": "kyo",
    "しゃ": "sha", "しゅ": "shu", "しょ": "sho",
    "ちゃ": "cha", "ちゅ": "chu", "ちょ": "cho",
    "にゃ": "nya", "にゅ": "nyu", "にょ": "nyo",
    "ひゃ": "hya", "ひゅ": "hyu", "ひょ": "hyo",
    "びゃ": "bya", "びゅ": "byu", "びょ": "byo",
    "ぴゃ": "pya", "ぴゅ": "pyu", "ぴょ": "pyo",
    "みゃ": "mya", "みゅ": "myu", "みょ": "myo",
    "りゃ": "rya", "りゅ": "ryu", "りょ": "ryo",
    "ぎゃ": "gya", "ぎゅ": "gyu", "ぎょ": "gyo",
    "じゃ": "ja", "じゅ": "ju", "じょ": "jo",
    "ぢゃ": "ja", "ぢゅ": "ju", "ぢょ": "jo",

    # map digraph katakana to romaji
    "キャ": "kya", "キュ": "kyu", "キョ": "kyo",
    "シャ": "sha", "シュ": "shu", "ショ": "sho",
    "チャ": "cha", "チュ": "chu", "チョ": "cho",
    "ニャ": "nya", "ニュ": "nyu", "ニョ": "nyo",
    "ヒャ": "hya", "ヒュ": "hyu", "ヒョ": "hyo",
    "ビャ": "bya", "ビュ": "byu", "ビョ": "byo",
    "ピャ": "pya", "ピュ": "pyu", "ピョ": "pyo",
    "ミャ": "mya", "ミュ": "myu", "ミョ": "myo",
    "リャ": "rya", "リュ": "ryu", "リョ": "ryo",
    "ギャ": "gya", "ギュ": "gyu", "ギョ": "gyo",
    "ジャ": "ja", "ジュ": "ju", "ジョ": "jo",
    "ヂャ": "ja", "ヂュ": "ju", "ヂョ": "jo",
}

_KANA_MONOGRAPH_DICT = {
    # map monograph hiragana to romaji
    "あ": "a", "い": "i", "う": "u", "え": "e", "お": "o",
    "か": "ka", "き": "ki", "く": "ku", "け": "ke", "こ": "ko",
    "が": "ga", "ぎ": "gi", "ぐ": "gu", "げ": "ge", "ご": "go",
    "さ": "sa", "し": "shi", "す": "su", "せ": "se", "そ": "so",
    "ざ": "za", "じ": "ji", "ず": "zu", "ぜ": "ze", "ぞ": "zo",
    "た": "ta", "ち": "chi", "つ": "tsu", "て": "te", "と": "to",
    "だ": "da", "ぢ": "ji", "づ": "zu", "で": "de", "ど": "do",
    "な": "na", "に": "ni", "ぬ": "nu", "ね": "ne", "の": "no",
    "は": "ha", "ひ": "hi", "ふ": "fu", "へ": "he", "ほ": "ho",
    "ば": "ba", "び": "bi", "ぶ": "bu", "べ": "be", "ぼ": "bo",
    "ぱ": "pa", "ぴ": "pi", "ぷ": "pu", "ぺ": "pe", "ぽ": "po",
    "ま": "ma", "み": "mi", "む": "mu", "め": "me", "も": "mo",
    "や": "ya", "ゆ": "yu", "よ": "yo",
    "ら": "ra", "り": "ri", "る": "ru", "れ": "re", "ろ": "ro",
    "わ": "wa", "ゐ": "wi", "ゑ": "we", "を": "wo", "ん": "n",

    # map monograph katakana to romaji
    "ア": "a", "イ": "i", "ウ": "u", "エ": "e", "オ": "o",
    "カ": "ka", "キ": "ki", "ク": "ku", "ケ": "ke", "コ": "ko",
    "ガ": "ga", "ギ": "gi", "グ": "gu", "ゲ": "ge", "ゴ": "go",
    "サ": "sa", "シ": "shi", "ス": "su", "セ": "se", "ソ": "so",
    "ザ": "za", "ジ": "ji", "ズ": "zu", "ゼ": "ze", "ゾ": "zo",
    "タ": "ta", "チ": "chi", "ツ": "tsu", "テ": "te", "ト": "to",
    "ダ": "da", "ヂ": "ji", "ヅ": "zu", "デ": "de", "ド": "do",
    "ナ": "na", "ニ": "ni", "ヌ": "nu", "ネ": "ne", "ノ": "no",
    "ハ": "ha", "ヒ": "hi", "フ": "fu", "ヘ": "he", "ホ": "ho",
    "バ": "ba", "ビ": "bi", "ブ": "bu", "ベ": "be", "ボ": "bo",
    "パ": "pa", "ピ": "pi", "プ": "pu", "ペ": "pe", "ポ": "po",
    "マ": "ma", "ミ": "mi", "ム": "mu", "メ": "me", "モ": "mo",
    "ヤ": "ya", "ユ": "yu", "ヨ": "yo",
    "ラ": "ra", "リ": "ri", "ル": "ru", "レ": "re", "ロ": "ro",
    "ワ": "wa", "ヰ": "wi", "ヱ": "we", "ヲ": "wo", "ン": "n",

    # map obsolete symbols to empty string
    "ゝ": "", "ヽ": "", "ゞ": "", "ヾ": "",
}


def _replace_choonpu(lst: list) -> list:
    """choonpu indicates that the previous vowel is extended"""
    return [lst[idx - 1] if str(item) == "ー"
            else str(item) for idx, item in enumerate(lst)]


def _replace_sokuon(lst: list) -> list:
    """sokuon indicates that the following consonate is geminated"""
    return [lst[idx + 1] if str(item) == "っ" or str(item) == "ッ"
            else str(item) for idx, item in enumerate(lst)]


def _replace_digraphs(lst: list) -> list:
    """digraphs have two kana - one regular sized, one small"""
    temp = []
    for idx, c in enumerate(lst):
        if c == "ゃ" or c == "ゅ" or c == "ょ" \
                or c == "ャ" or c == "ュ" or c == "ョ":
            temp.pop()
            digraph_str = "".join(lst[idx - 1:idx + 1])
            temp.extend(list(_KANA_DIGRAPH_DICT[digraph_str]))
        else:
            temp.append(c)
    return temp


def _replace_monographs(lst: list) -> list:
    """monographs are one regular sized kana"""
    temp = []
    for idx, c in enumerate(lst):
        if c in _KANA_MONOGRAPH_DICT:
            temp.extend(list(_KANA_MONOGRAPH_DICT[c]))
        else:
            temp.append(c)
    return temp


def translate_kana_to_romaji(s: str) -> str:
    """translates hiragana/katakana string to romaji equivalent"""
    translation = list(s)  # split s into list of chars
    translation = _replace_digraphs(translation)
    translation = _replace_monographs(translation)
    translation = _replace_choonpu(translation)
    translation = _replace_sokuon(translation)
    return "".join(translation)  # return str of translation


def print_detailed_results():
    num_files = _num_files_ignored + _num_rename_failure + _num_rename_success

    print("Results: " + str(_num_rename_success) + " of "
          + str(num_files) + " files were renamed successfully.")

    if _num_rename_success != num_files:
        print(" - " + str(_num_files_ignored) + " ignored files")
        print(" - " + str(_num_rename_failure) + " files failed to rename")
        print("Failed to rename:")
        for x in _filenames_failed:
            print(str(x))


def try_rename(filename: str, new_filename: str):
    global _num_rename_failure, _num_rename_success
    try:
        os.rename(filename, new_filename)
        _num_rename_success += 1
    except():
        _filenames_failed.append(filename)
        _num_rename_failure += 1


def valid_new_filename(filename: str, new_filename: str) -> bool:
    return new_filename is not None \
           and new_filename != "" \
           and new_filename != filename


def main(dir_path):
    global _num_files_ignored
    print("Starting Kana2Romaji File Renamer by DrewHans555...")

    if dir_path is None or dir_path == "":
        dir_path = "."

    for filename in os.listdir(dir_path):
        new_filename = translate_kana_to_romaji(filename)
        if valid_new_filename(filename, new_filename):
            try_rename(filename, new_filename)
        else:
            _num_files_ignored += 1

    print("...finished!")
    print_detailed_results()


if __name__ == "__main__":
    main(sys.argv[0])
