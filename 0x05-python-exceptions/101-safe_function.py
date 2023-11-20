#!/usr/bin/python3
import sys


def safe_function(fct, *args):
	a = args[0]
	b = args[1]
	try:
		return (fct(a, b))
	except ZeroDivisionError as e:
		sys.stderr.write(f"Exception: {e}\n")
	except IndexError as e:
		sys.stderr.write(f"Exception: {e}\n")
