import math

def NULL_not_found(thing: any)-> int:

	if type(thing) == float and thing != thing:
		return 0
	type_names = {
		None: "Nothing : None <class 'NoneType'>",
		float: "Cheese: nan <class 'float'>$",
		0: "Zero: 0 <class 'int'>",
		'': "Empty: <class 'str'>",
		False: "Fake: False <class 'bool'>"
	}
	return_value = type_names.get(thing, 1)
	if return_value == 1:
		print("Type not find")
	else:
		print(return_value)
		return_value = 0
	return return_value
