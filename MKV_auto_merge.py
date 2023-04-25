import os
import pymkv
from rich.console import Console


def addChapter(video_name):
	with open(video_name) as chapter:
		chapter = chapter.read()
	return list(chapter)
	

def fineVdo_name(i):
	if i.endswith(".mp4") or i.endswith(".mkv"):
		video_file = i.split(".")[0]
	return video_file


def remove_(name):
	name = name.replace("_", " ")
	name = name.replace("  ", "_")
	name = name.replace(" ", "_")
	name = name.replace("__", "_")
	return name.title()


while True:
	path = input("Inset input directory path > ")

	if os.path.exists(path):

		if os.path.isdir(path):
			break

		else:
			Console().print(f"[color(9) bold]FOLDER TYPE ERROR[/]: This >>> '[color(14) bold]...{path}[/]' not a folder.\n")

	else:
		Console().print(f"[color(9) bold]FOLDER NOT FOUND[/]: No '[color(14) bold]{path}[/]' :eyes: directory in your system.\n")
	

print("")

Console().print(" Language ".center(20, "="),style=("color(9) bold\n"))
Console().print(f"[color(57) ]{'Hindi':10}: h[/]\n[color(190)]{'English':10}: e[/]")

print("")


lan = input("Language [e/n] ")

if lan.lower() != "h":
    lan = "eng"
    
else:
	lan = "hin" 

os.chdir(path)
all_file = os.listdir()

for i in all_file:
	found = []

	if i.endswith(".mkv") or i.endswith(".mp4"):
		merge = pymkv.MKVFile()
		vdo_name = i.split(".")[0]
		merge.add_track(pymkv.MKVTrack(i , track_id = 0, track_name= remove_(vdo_name)))
		merge.add_track(pymkv.MKVTrack(i , track_id = 1, track_name = remove_(vdo_name), language = lan))

		if f"{vdo_name}.srt" in all_file:
			merge.add_track(pymkv.MKVTrack(path + vdo_name + ".srt", track_name = remove_(vdo_name), language = lan))
			found.append("Subtitle")


		if f"{vdo_name}.txt" in all_file:
			# merge.add_track(vdo_name + ".txt")
			found.append("Chapter")

		if f"{vdo_name}.jpg" in all_file:
			merge.add_attachment(vdo_name + ".jpg")
			found.append("Cover")

		Console().print(f"[color(11) bold]RECOGNIZE[/]: Found corresponding file for [color(5) bold]{vdo_name}.mp4 :eyes: >>> \n{found}")


		while True:
			output_path = input("Output path folder path ? > ")

			if os.path.exists(output_path):

				if os.path.isdir(output_path):
					break

				else:
					Console().print(f"[color(9) bold]FOLDER TYPE ERROR[/]: This >>> '[color(14) bold] {path}[/]' :eyes: not a folder.\n")

			else:
				exit(Console().print(f"[color(9) bold]FOLDER NOT FOUND[/]: No '[color(14) bold]{path}[/]' :eyes: directory in your system.\n"))
						

		print(" WORKING ".center(50, "="))
		# merge.track_tags(remove_(vdo_name))
		merge.mux(output_path + remove_(vdo_name) + ".mkv")
		print("Done")