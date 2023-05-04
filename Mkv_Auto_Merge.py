print("Loading...")
import os
import pymkv
from sys import platform
from rich.tree import Tree
from rich.console import Console
from rich.panel import Panel
from time import time, sleep, strftime, gmtime


def addChapter(name):
	chapter = 1
	if os.path.exists(path + vdo_name + "_Chapter.txt"):
		open(path + vdo_name + "_Chapter.txt", "w")

	with open(name, "rt") as file:
		for line in file:
			line = file.readline()
			if ":" in line and line[0:2].isdigit() and line[2] == ":" and line[3].isdigit():
				time_parts, name = line.split(" ", maxsplit=1)
				
				time_parts = time_parts.split(":")
				if len(time_parts) == 1:
					time_parts = ['00', '00', '00'] + time_parts

				elif len(time_parts) == 2:
					time_parts = ['00'] + time_parts	

				time_parts = ':'.join(time_parts)
				
				
				name = name.split()
				name = " ".join(name)
				name = name.replace(name[0], name[0].upper())
			
				with open(f'{path + vdo_name}_Chapter.txt', 'a') as file1:
					file1.write(str(f'CHAPTER{chapter}={time_parts}.000\n'))  # Will write the timeing of chapter.
					file1.write(str(f'CHAPTER{chapter}NAME={name}\n'))  # Will write the chapter name.
					chapter += 1
					
	return path + vdo_name + "_Chapter.txt"



def findTypeSystem():
	if platform == "win32":
		return "cls", "\\"	
	
	elif platform == "linux" or platform == "darwin":  # Darwin is for mac os
		return "clear", "/"
	
	else:
		Console().print("[color(9) bold u]Unsupported system[/]:")
		sleep(3)
		exit()


formate = lambda name: name.replace("_", " ").replace("  ", "_").replace(" ", "_").replace("__", "_").title()

os.system(findTypeSystem()[0])

while True:
	path = input("Inset input directory path or [^+c] > ")

	if os.path.exists(path):

		if os.path.isdir(path):
			break

		else:
			Console().print(f"\n[color(9) bold]FOLDER TYPE ERROR[/]: This >>> '[color(14) bold]{path}[/]' not a folder.\nTry again...\n")

	else:
		Console().print(f"\n[color(9) bold]FOLDER NOT FOUND[/]: No '[color(14) bold]{path}[/]' :eyes: directory in your system.\nTry again...\n")
	

print("")

Console().print(" Language ".center(20, "="), style="color(9) bold\n")
Console().print(f"[color(57) ]{'Hindi':17}: h[/]\n[color(190)]{'English':17}: e[/]\n[white bold i]{'Other language':17}: o\n")


lan = input("Video language [h/e/o] ? ")

print("")


if lan.lower() == "h":
	lan = "hin"

elif lan.lower() == "e":
	lan = "eng"

else:
	lan = "mul"


os.chdir(path)
all_file = os.listdir()
run = True

for i in all_file:
	if i.endswith(".mkv") or i.endswith(".mp4"):
		run = False
		vdo_name = i.split(".")[0]
		tree = Tree(f":file_folder: [color(14) b]{path}[/] :eyes:")
		vd = tree.add(f":movie_camera: [color(10) bold]{i}[/] >>> [color(10) bold]for main video file.[/]")
		merge = pymkv.MKVFile(title=formate(vdo_name).replace("_", " "))

		merge.add_track(pymkv.MKVTrack(i, track_id=0, track_name=formate(vdo_name), language=lan, default_track=True))
		merge.add_track(pymkv.MKVTrack(i, track_id=1, track_name=formate(vdo_name), language=lan, default_track=True))

		if f"{vdo_name}.srt" in all_file:
			merge.add_track(pymkv.MKVTrack(path + vdo_name + ".srt", track_name=formate(vdo_name), language="eng"))
			vd.add(f":card_file_box:  [color(11) bold]{vdo_name}.srt[/] >>> [color(11) bold]for subtitle.[/]")

		if f"{vdo_name}.txt" in all_file:
			merge.chapters(addChapter(vdo_name + ".txt"))
			vd.add(f":clapper: [color(9) bold]{vdo_name}.txt[/] >>> [color(9)]for time stamp.[/]")

		if f"{vdo_name}.jpg" in all_file:
			merge.add_attachment(vdo_name + ".jpg")
			vd.add(f":clipboard: [color(12) bold]{vdo_name}.jpg[/] >>> [color(12)]for album cover.[/]") 

		Console().print(Panel(tree, title="[color(11) bold u]RECOGNIZE[/]: Found corresponding file form", subtitle="[color(9) b i u]All above files are going to merge.[/]", subtitle_align= "right"))

		while True:
			output_path = input("\nOutput path folder path or [^+c] ? > ")

			if os.path.exists(output_path):

				if os.path.isdir(output_path):
					break

				else:
					Console().print(f"\n[color(9) bold]FOLDER TYPE ERROR[/]: This >>> '[color(14) bold]{output_path.split(findTypeSystem()[1])[-1]}[/]' :eyes: not a folder.\nTyr again...\n")

			else:
				Console().print(f"\n[color(9) bold]FOLDER NOT FOUND[/]: No '[color(14) bold]{output_path}[/]' :eyes: directory in your system.\nTry again..\n")
		
		Console().print(f"\nMerging files it may take some minutes.", style=("color(10) i bold\n"))
		print("")

		try:
			init = time()
			merge.mux(output_path + formate(vdo_name)+".mkv")

		except Exception as e:
			exit(e)

		else:
			Console().print(f"\n[color(11) b]DONE: [/]Total time taken for merging:")
			print(formate(vdo_name) + ".mkv",end=" ") 
			Console().print(f">>> [color(14) b u]{strftime('%H:%M:%S', gmtime(time() - init))}[/]")
			Console().print(f"\nA 'mkv' file is waiting for you in [color(11) bold i]{output_path}[/] directory.")


if run:
	exit(Console().print(f"\n[color(9) bold]NO VIDEO FOUND:[/] No file endswith '.mp4' or '.mkv' in '[color(14) bold i]{path}[/]' :eyes: folder.\n"))
