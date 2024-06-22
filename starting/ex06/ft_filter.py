import sys

def ft_filter(function, iterable):
	"""filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

	# for i in iterable:
	# 	if function(i):
	# 		yield i
	#filter cree un generateur pas une list ou quoi que ce soit qui sois stpcket en memoire, seulement 
	#(i for i in iterable if function(i))

	#consigne:
	filtered_list = [item for item in iterable if function(item)]
	return iter(filtered_list)
# print("ici")
n = [1, 4, 6, 9, 10, 13, 15]
# n2 = iter(n)
# print(list(n))
# print("ici")
n2 = iter(n)
# print(next(n2))
# print(next(n2))
# print(next(n2))
# print(next(n2))
# print(next(n2))
# print(next(n2))
# print(next(n2))
# try:
# 	print(next(n2))
# except StopIteration:
# 	print("Fin de l'itérateur")
if __name__ == "__main__":
	# print(list(ft_filter(lambda i: i in [4,9], n)))
	print(filter.__doc__)
	print("="*40)
	print(ft_filter.__doc__)
