# This file is part of pygments-minimessage, licensed under the MIT License.
#
# Copyright (c) 2022-2025 KyoriPowered
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import Any, ClassVar

from pygments.lexer import RegexLexer
from pygments.token import Escape, Literal, Name, String

__all__ = ["MiniMessageLexer"]


class MiniMessageLexer(RegexLexer):
  """A basic implementation of something resembling the MiniMessage language.

  The behavior when encountering invalid tags differs greatly from the real MiniMessage
  parser, but it's good enough for now for the examples in the documentation.

  """

  name: ClassVar[str] = "MiniMessage component representation"
  aliases: ClassVar[list[str]] = ["minimessage", "mm"]
  filenames: ClassVar[list[str]] = []

  tokens: ClassVar[dict[str, Any]] = {
    'root': [
      (r'[^<]+', Literal),
      (r'\\[<\\]', Escape),
      (r'<', Name.Tag, 'tag')
    ],
    'tag': [
      (r'\\>', Escape),
      (r'>', Name.Tag, '#pop'),
      (r':', Name.Tag, 'tag_options'),
      (r'[^>:\'"]+', Name.Tag)
    ],
    'tag_options': [
      (r'\\>', Escape),
      (r':', Name.Tag),
      (r'>', Name.Tag, '#pop:2'),
      (r"'", String.Single, 'string_single'),
      (r'"', String.Double, 'string_double'),
      (r'[^>:\'"]+', Name.Attribute),
    ],
    'string_single': [
      (r"\\['\\]", String.Escape),
      (r"'", String.Single, '#pop'),
      (r"(?:\\[^']|[^'])+", String.Single)
    ],
    'string_double': [
      (r'\\["\\]', String.Escape),
      (r'"', String.Double, '#pop'),
      (r'(?:\\[^"]|[^"])+', String.Double)
    ]
  }  # fmt: skip
