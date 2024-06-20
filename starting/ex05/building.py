import sys
import string

sys.tracebacklimit = 0

def main(args):
	Up = 0
	lo = 0
	sp = 0
	nb = 0
	ponct = 0
	a = 0
	assert len(args) <= 2, "wrong number of argument"
	if(len(args) == 1):
		command = input("Text Please:\n> ")
	else:
		command = args[1]

	for c in command:
		if c.isupper():
			Up+=1
		if c.islower():
			lo +=1
		if c.isspace():
			sp+=1
		if c.isdigit():
			nb+=1
		if c in string.punctuation:
			ponct+=1
		a+=1
	print("The text contains ", a, " characters:\n",\
	   Up," upper letters\n", lo, " lower letters\n",\
	   ponct, " punctuation marks\n", sp , " spaces\n", nb, " digits")
if __name__ =="__main__":
	main(sys.argv)