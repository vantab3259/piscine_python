import sys

sys.tracebacklimit = 0

def main():
	assert len(sys.argv) == 3, "the arguments are bad"
	string = sys.argv[1]
	try:
		n = int(sys.argv[2])
	except ValueError:
		raise AssertionError("Invalid argument types.")
	lst = string.split()
	return[i for i in lst if (lambda x: len(x) >= n)(i)]
try:
	print(main())
except AssertionError as e:
	print(e)