import sys

sys.tracebacklimit = 0


assert len(sys.argv) == 2, (
    "more than one argument is provided"
    if len(sys.argv) > 2
    else "less than one argument is provided"
)
assert len(sys.argv[1]) > 0, "argument is not an integer"
for c in sys.argv[1]:
    assert c.isdigit(), "argument is not an integer"
int_arg = int(sys.argv[1])
# print("I'm Even." if int_arg % 2 == 0 else "I'm Odd.")
# print("I'm", 'EOvdedn..'[int_arg % 2::2])
print("I'm", "EOvdedn.."[int_arg & 1 :: 2])
#print("Je suis", "im" * (int_arg % 2) + "pair.")
