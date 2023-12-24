#!/usr/local/bin/python3
"""
	express.py
	Matches one or more input strings against a given regular expression
	and highlights all potential matches.

	Copyright © 2023 Christian Rosentreter

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <https://www.gnu.org/licenses/>.

	$Id: express 4 2023-12-24 10:11:39Z tokai $
"""

__author__  = 'Christian Rosentreter'
__version__ = '1.1'
__all__     = []


import re
import argparse
import sys
import logging
import unicodedata



def verify_regex(inputs, regex, case_insensitive=False, normalize=False, extra_colors=False):
	"""Happy exploration of regular expressions."""

	print("\033[1mRegular Expression:\033[0m {}\n".format(regex))

	if normalize:
		regex = unicodedata.normalize('NFC', regex)

	colors = [34, 36, 35] if extra_colors else [34]
	flags  = re.IGNORECASE if case_insensitive else 0 # re.NOFLAG

	for i, searchstr in enumerate(inputs):
		if normalize:
			searchstr = unicodedata.normalize('NFC', searchstr)
		logging.debug("Input string: \033[1m%s\033[22m", str(searchstr))

		last_match = 0
		output     = ''
		match_cnt  = 0
		color_id   = 0

		for match in re.finditer(regex, searchstr, flags=flags):
			logging.debug("• \033[1mMatch #%lu\033[22m: <\033[%lum%s\033[33m> (%lu»%lu, %lu characters)",
				match_cnt + 1,
				colors[color_id],
				match.group(),
				match.start(),
				match.end(),
				match.end() - match.start(),
			)

			for j, g in enumerate(match.groups()):
				if g:
					logging.debug("   \\%lu: %s", j + 1, g)

			start, end = match.span()
			output += '{}\033[{}m{}\033[0m'.format(
				searchstr[last_match:start],
				colors[color_id],
				searchstr[start:end]
			)
			last_match = end

			color_id += 1
			if color_id >= len(colors):
				color_id = 0

			match_cnt += 1

		output += searchstr[last_match:]

		if match_cnt:
			if match_cnt > 1:
				match_cnt_str = '\033[1m{}\033[22m matches'.format(match_cnt)
			else:
				match_cnt_str = '\033[1m1\033[22m match'
		else:
			match_cnt_str = 'no matches'

		print('\033[1m{}\033[0m: {}  \033[90m({})\033[0m'.format(i + 1, output, match_cnt_str))



def main():
	"""Setting sail…"""

	#sys.tracebacklimit = 0

	ap = argparse.ArgumentParser(
		description='Matches one or more input strings against a given regular expression and highlights all potential matches.',
		epilog='Report bugs, request features, or provide suggestions via https://github.com/the-real-tokai/express/issues'
	)

	ap.add_argument('-V', '--version', action='version',
		help="show version number and exit", version='%(prog)s {}'.format(__version__))

	ap.add_argument('inputs', type=str, metavar='STRING', nargs='*',
		help=('One or more inputs to match against the regular expression, alternatively/ '
			'additionally %(prog)s will read data from standard input'))

	ap.add_argument('-r', '--regex', type=str, default='.',
		help='A regular expression to match any inputs against  [default: .]')
	ap.add_argument('-i', '--case-insensitive', action='store_true', default=False,
		help=('Perform matching by ignoring the case, e.g. expressions like `[A-Z]\' will match '
		'lowercase letters too'))
	ap.add_argument('-n', '--normalize', action='store_true', default=False,
		help='Forces Unicode\'s normalization form C (NFC) for all inputs and the regular expression')
	ap.add_argument('-x', '--extra-colors', action='store_true', default=False,
		help='Highlight multiple matches on a single input with alternating colors')
	ap.add_argument('-d', '--debug', action='store_true', default=False,
		help='Enable extra output to aid analyzing all matches and subgroups of matches')

	args = ap.parse_args()

	if args.debug:
		logging.basicConfig(level=logging.DEBUG, format="\033[33m%(levelname)s: %(message)s\033[0m")
	delattr(args, 'debug')

	if not sys.stdin.isatty():
		# TODO: that's not too efficient here, but good enough for my personal use cases
		#       (probably should move enumeration out of verify_regex().)
		for line in sys.stdin:
			args.inputs.append(line.rstrip())

	verify_regex(**vars(args))



if __name__ == "__main__":
	main()
