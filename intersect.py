#!/usr/bin/python3
import sys
import re
import itertools
from argparse import ArgumentParser

def main():
	config = []
	out = []
	parser = ArgumentParser()
	parser.add_argument('-c', '--config', help="config file")
	conf = parser.parse_args().config
	with open(conf) as f:
		for line in f:
			src, dst = line.rstrip("\n").split("\t")
			config.append((src, dst))

	for line in sys.stdin:
		words = line.split("$")
		readings = []

		for word in words:
			word = word.rstrip("\n").lstrip(" ")
			split = word.rstrip("$").split("/")
			surface = split[0]
			if src in word:
				readings.append(["^" + i + "$" for i in split[1:]])
			else:
				readings.append([split[0].lstrip("^")])

		for i in itertools.product(*readings):
			for src, dst in config:
				sys.stdout.write(re.sub(src, dst, " ".join(i) + "\n", count=1))

if __name__ == '__main__':
	main()
