def ft_tqdm(lst: range) -> None:
	
	for i in lst:
		print(i, "%|\033[47m \033[0m", end='')

if __name__ == "__main__":
	ft_tqdm(range(70))