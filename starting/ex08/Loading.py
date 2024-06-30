import shutil
import time

def ft_tqdm(lst: range) -> None:
	start = time.time()
	terminal_size = int(shutil.get_terminal_size().columns) - 38
	for i in lst:
		laps = time.time()-start
		percent = int(((i)/(len(lst))) * 100)
		first= int((percent * terminal_size) /100)
		second = terminal_size - first
		it = f"{(i/laps):.2f} it/s" if i>0 else "],  ?/it"
		print(f"\r{percent}%|{first* '█'}{second * ' '}|{i}/{len(lst)} [{int(laps)//60:02}:{int(laps)%60:02}],  {it}", end="")
		yield i
	print(f"\r100%|{terminal_size * '█'}|{len(lst)}/{len(lst)} [{int(time.time()-start)//60:02}:{int(time.time()-start)%60:02}],  {it}")


if __name__ == "__main__":
	from tqdm import tqdm
	for elem in ft_tqdm(range(5)):
		time.sleep(0.5)
