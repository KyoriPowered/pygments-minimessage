Examples
========

.. role:: mm(code)
  :language: minimessage
  :class: highlight

At the end of the day it's just a Pygments lexer, here's some samples of places we've used it:

Docutils code blocks
--------------------

The MiniMessage lexer can be used within any Sphinx codeblock:

.. tab-set-code::

  .. code:: rst

    .. code:: mm

      <rainbow>Hello <lang:myplugin.user:'<name>'>

  .. code:: markdown

    ```mm
      <rainbow>Hello <lang:myplugin.user:'<name>'>
    ```

produces:

.. code:: mm

  <rainbow>Hello <lang:myplugin.user:'<name>'>

Inline code fragments
---------------------

With a little bit of glue, it's possible to highlight code inline as well!

Add a ``docutils.conf`` file to your project, with the contents:

.. literalinclude:: docutils.conf
  :language: ini

Then, if using reST, include the following block in your preamble.

.. code:: rst

  .. role:: mm(code)
    :language: minimessage
    :class: highlight

Now you can inline to your heart's content. A paragraph like:

.. tab-set-code::

  .. code:: rst

    This is a :mm:`<red>formatted` message!

  .. code:: markdown

    This is a `<red>formatted`{l=mm} message!

Which becomes:

This is a :mm:`<red>formatted` message!

At the command line
-------------------

Since we're registered as a pygments lexer, pygmentize can highlight any input and spit it out to the console:

.. code:: sh

  $ echo "<rainbow>hi there" | pygmentize -l mm -O style=monokai
  # <...ansi-coloured output...>
