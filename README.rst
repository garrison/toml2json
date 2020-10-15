toml2json
=========

I needed a script I could run from the commandline to convert toml_ to
json_ (and vice versa).

This script is written in python, and depends on the `toml package
<https://github.com/uiri/toml>`_

Because ``datetime``'s are not supported in JSON, they do not make the
roundtrip properly.  After the toml => json => toml conversion, each
``datetime`` will be a string, just like when using the web service
http://toml-to-json.matiaskorhonen.fi/

~~More to come.~~

EDIT: I no longer use this.  See https://github.com/dbohdan/remarshal for a replacement.

.. _toml: https://github.com/toml-lang/toml
.. _json: http://json.org/
