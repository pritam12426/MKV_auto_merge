import os, pymkv
from sys import platform
from rich.tree import Tree
from rich.console import Console


# def addChapter(video_name):
# 	with open(video_name) as chapter:
# 		chapter = chapter.read()
# 	pass


def findTypeSystem():
	if platform == "win32":
		return "cls", "\\"	
	
	elif platform == "linux" or platform == "darwin":
		return "clear", "/"
	
	else:
		exit("Unsported os")


formate = lambda name: name.replace("_", " ").replace("  ", "_").replace(" ", "_").replace("__", "_").title()

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
		tree = Tree(f"[color(14) b]{path}[/] :eyes:")
		vd = tree.add(f"[color(10) bold]{i}[/] >>> [color(10) bold]for main video file.[/]")
		merge = pymkv.MKVFile(title=formate(vdo_name).replace("_", " "))

		merge.add_track(pymkv.MKVTrack(i, track_id=0, track_name=formate(vdo_name), language=lan, default_track=True))
		merge.add_track(pymkv.MKVTrack(i, track_id=1, track_name=formate(vdo_name), language=lan, default_track=True))

		if f"{vdo_name}.srt" in all_file:
			merge.add_track(pymkv.MKVTrack(path + vdo_name + ".srt", track_name=formate(vdo_name), language="eng"))
			vd.add(f"[color(11) bold]{vdo_name}.srt[/] >>> [color(11) bold]for subtitle.[/]")

		if f"{vdo_name}.txt" in all_file:
			pass
			# merge.add_track(vdo_name + ".txt")
			# vd.add(f"[color(9) bold]{vdo_name}.txt[/] >>> [color(9)]for time stamp.[/]")

		if f"{vdo_name}.jpg" in all_file:
			merge.add_attachment(vdo_name + ".jpg")
			vd.add(f"[color(12) bold]{vdo_name}.jpg[/] >>> [color(12)]for album cover.[/]") 

		Console().print(f"[color(11) bold]RECOGNIZE[/]: Found corresponding file form:\n")
		Console().print(tree)


		while True:
			output_path = input("\nOutput path folder path or [^+c] ? > ")

			if os.path.exists(output_path):

				if os.path.isdir(output_path):
					break

				else:
					Console().print(f"\n[color(9) bold]FOLDER TYPE ERROR[/]: This >>> '[color(14) bold]{output_path.split(findTypeSystem()[1])[-1]}[/]' :eyes: not a folder.\nTyr again...\n")

			else:
				exit(Console().print(f"\n[color(9) bold]FOLDER NOT FOUND[/]: No '[color(14) bold]{output_path}[/]' :eyes: directory in your system.\nTry again..\n"))
						

		merge.mux(output_path + formate(vdo_name)+ ".mkv")
		print("Done")

if run:
	exit(Console().print(f"\n[color(9) bold]NO VIDEO FOUND:[/] No file endswith '.mp4' or '.mkv' in '[color(14) bold i]{path}[/]' :eyes: folder."))
