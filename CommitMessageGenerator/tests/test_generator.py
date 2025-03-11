import pytest
from commit_message_generator.generator import emoji_commit, themed_commit, haiku_commit, dramatic_commit

def test_emoji_commit():
    assert isinstance(emoji_commit(), str)

def test_themed_commit():
    assert themed_commit("pirate") in ["Arrr! Fixed me code, matey! 🏴‍☠️", "Shivered me timbers! A bug be gone! 🦜"]
    assert themed_commit("superhero") in ["Justice is served! Bug fixed! 🦸‍♂️", "With great power comes bug fixes! ⚡"]

def test_haiku_commit():
    assert isinstance(haiku_commit(["main.py"]), str)

def test_dramatic_commit():
    assert dramatic_commit("fixed bug") == "🔥🔥 FIXED BUG 🔥🔥"


