import shutil
import time

def ft_tqdm(lst: range) -> None:
	start = time.time()
	terminal_size = int(shutil.get_terminal_size().columns) - 30
	for i in lst:
		laps = time.time()-start
		percent = int(((i)/(len(lst))) * 100)
		first= int((percent * terminal_size) /100)
		second = terminal_size - first
		print(f"{percent}%|{first* '█'}{second * ' '}|{i}/{len(lst)} [{int(laps)//60:02}:{int(laps)%60:02}]", end="\r")
		yield i
	print(f"100%|{terminal_size * '█'}|{len(lst)}/{len(lst)} [{int(time.time()-start)//60:02}:{int(time.time()-start)%60:02}]")


if __name__ == "__main__":
	from tqdm import tqdm
	for elem in tqdm(range(100)):
		time.sleep(1.0)
