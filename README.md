# Express

[![GitHub](https://img.shields.io/github/license/the-real-tokai/express?color=green&label=License&style=flat)](https://github.com/the-real-tokai/express/blob/master/LICENSE)
[![GitHub Code Size in Bytes](https://img.shields.io/github/languages/code-size/the-real-tokai/express?label=Code%20Size&style=flat)](https://github.com/the-real-tokai/express/)
[![Twitter Follow](https://img.shields.io/twitter/follow/binaryriot?color=blue&label=Follow%20%40binaryriot&style=flat)](https://twitter.com/binaryriot)

## Synopsis

`express.py` is a simple and streamlined Python 3 script to explore regular expressions.

While not as comfortable without a graphical user interface `express` was created as quick and simple drop-in-replacement for
abandoned Mac OS X tools like Reginald or Reggy (both only available as 32-bit builds that are no longer supported
by recent versions of macOS).

## Requirements

An installation of `Python 3` (any version above `3.5` should do fine).

## Usage

```
usage: express [-h] [-V] [-r REGEX] [-i] [-n] [-x] [-d] [STRING [STRING ...]]

Matches one or more input strings against a given regular expression and
highlights all potential matches.

positional arguments:
  STRING                One or more inputs to match against the regular
                        expression, alternatively/ additionally express will
                        read data from standard input

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         show version number and exit
  -r REGEX, --regex REGEX
                        A regular expression to match any inputs against
                        [default: .]
  -i, --case-insensitive
                        Perform matching by ignoring the case, e.g.
                        expressions like `[A-Z]' will match lowercase letters
                        too
  -n, --normalize       Forces Unicode's normalization form C (NFC) for all
                        inputs and the regular expression
  -x, --extra-colors    Highlight multiple matches on a single input with
                        alternating colors
  -d, --debug           Enable extra output to aid analyzing all matches and
                        subgroups of matches

Report bugs, request features, or provide suggestions via
https://github.com/the-real-tokai/express/issues
```

### Usage Examples

``` shell
# basic usage, e.g. match and highlight vocals
$ express -r '[aeiou]' 'Foobar'
```

``` shell
# explore a larger dataset via stdin
$ cat data.txt | express -r '^[A-Z]'
```

``` shell
# generate a more colorful output with extra information
$ express -d -x -r 'o+' 'Foobar'
```

## History

<table>
    <tr>
        <td valign=top>1.1</td>
        <td valign=top nowrap>24-Dec-2023</td>
        <td>Initial public source code release</td>
    </tr>
</table>
