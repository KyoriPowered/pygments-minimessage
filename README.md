# pygments-minimessage

A [pygments](https://pygments.org/) language highlighter for the MiniMessage language.

This implementation is fairly basic at the moment, it is what has been used for [adventure's own docs](https://docs.advntr.dev/), and captures most of the language's syntax. There will be some differences in behaviour, since the actual MM parser has a fixed list of known tags - this highlighter treats anything that looks like a tag as a tag.

## Usage

`pygments-minimessage` is available on PyPI. The lexer is exposed with a plugin entrypoint, so it will automatically be picked up by pygments.

To install, use pip or your tool of choice:

```sh
$ pip install pygments-minimessage
```

See [examples](examples) for some usage scenarios.

```mm
<blue>Hello <shadow:red:0.8>MiniMessage</shadow>! <rainbow>Enjoy your stay!
```

For any other questions, we're happy to help out in the [Kyori discord](https://discord.gg/MMfhJ8F)

## Contributing

We welcome contributions that help move this lexer closer to parity with the full MiniMessage parser.

## License

`pygments-minimessage` is released under the terms of the MIT license.
