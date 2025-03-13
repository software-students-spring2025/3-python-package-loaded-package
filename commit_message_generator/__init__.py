# commit_message_generator/__init__.py
from .emoji import emoji_commit
from .style import style_commit
from .haiku import haiku_commit

__all__ = ['emoji_commit', 'style_commit', 'haiku_commit']