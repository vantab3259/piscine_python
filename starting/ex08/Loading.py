import shutil
import time

def ft_tqdm(lst: range) -> None:
	terminal_size = int(shutil.get_terminal_size().columns) - 30
	for i in lst:
		percent = int(i/(len(lst)-1) * 100)
		print(percent,"%|", end ='')
		print(int((percent * terminal_size) /100) * '█', (terminal_size - percent * (len(lst)-i+1)) * "-", end='\r')
		time.sleep(0.5)
		yield i


if __name__ == "__main__":

	for elem in ft_tqdm(range(15)):
		time.sleep(0.005)
	print()
