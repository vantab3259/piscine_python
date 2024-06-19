ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"
ft_tuple = ("Hello", "France!")
# [i], .index(elem), .count(elem) on peu les additionner ou les empiler en multipliant
ft_set.add("Paris!")
ft_set.remove("tutu!")
#element unique dasn un set car fonction de hashage memoire

ft_dict["Hello"] = "42Paris!"
# .update ecrase et ou ajoute c'est cool




print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)