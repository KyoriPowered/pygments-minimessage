## pygments-minimessage

A [pygments](https://pygments.org/) language highlighter for the MiniMessage language.

This implementation is fairly basic at the moment, it is what has been used for [adventure's own dogs](https://docs.advntr.dev/), and captures most of the language's syntax. There will be some differences in behaviour, since the actual MM parser has a fixed list of known tags - this highlighter treats anything that looks like a tag as a tag.
