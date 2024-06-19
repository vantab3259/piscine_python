def wtf(thing: any)-> int:
	type_dic = {
		list: "List",
		tuple: "Tuple",
		set: "Set",
		dict: "Dict",
		str: "String"
	}
	thing_type = type(thing)
	type_name = type_dic.get(thing_type, "Type not found")
	if thing_type == str:
		print(f"{thing} is in the kitchen :{thing_type}")
	elif type_name != "Type not found":
		print(f"{type_name} : {thing_type}")
	else:
		print("Type not found")
	return 42