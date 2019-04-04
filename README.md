# Kana2Romaji File Renamer

#### Introduction
One of the first programs I ever wrote outside of class was a kana-to-romaji filename translator. The original program was written in Java and, if I'm being honest, looking at it now makes my eyes bleed.
(╯°□°）╯︵ ┻━┻

Even though I've gotten much better at programming since then, looking over that old program ~~shamed me~~ inspired me to create a new version that I could be proud of. These days I can read hiragana and most katakana at a glance so this program isn't going to be much use to me but maybe it will be useful to you. Either way, I got to do some Python programming and that's always a win in my book.

### About
Kana2Romaji File Renamer is a Python 3 script that accepts a directory path as an argument (defaults to script directory if none is passed in) and attempts to rename all directory files that contain Japanese hiragana/katakana characters. The kana characters are replaced with their romaji equivalent. At the end, a brief report is printed to stdout indicating the number of successful renames and, if appropriate, the number of ignored files & failed rename attempts.  

### Project Prerequisites
* Python 3.7 interpreter

### Project Structure

./
├─ src/                     # source code files
│  │
│  ├─ init.py               # allows this directory to be importable by test.py
│  └─ main.py               # a callable script that renames files in a directory
│
├─ test/                    # unit test files
│  │
│  └─ test.py               # contains some short unit tests
│
├─ LICENSE
└─ README.md

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
