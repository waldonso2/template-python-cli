from tool import core
from tool.cli import main


def test_word_counts_by_frequency_then_alphabetically():
    assert core.word_counts("b a, B! c a b") == [("b", 3), ("a", 2), ("c", 1)]


def test_punctuation_only_is_no_word():
    assert core.word_counts("... !!") == []


def test_cli_prints_the_top_words(tmp_path, capsys):
    f = tmp_path / "in.txt"
    f.write_text("x y x", encoding="utf-8")
    assert main([str(f), "--top", "1"]) == 0
    assert capsys.readouterr().out == "2\tx\n"
