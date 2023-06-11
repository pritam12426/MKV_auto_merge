print("Loading...")
import os
import sys
import pymkv
from time import time, strftime, gmtime


def get_type_system() -> tuple:
	if sys.platform == "win":
		return "cls", "\\"
	elif sys.platform == "linux":
		return "clear", "/"
	else:
		exit("Unsupported system.")


def get_lan() -> str:
	print(" Language ".center(20, "="))
	print(f"{'Hindi':17}: h\n{'English':17}: e\n{'Other language':17}: o\n")

	lan: str = input("Video language [h/e/o] ? ")

	if lan.lower() == "h":
		return "hin"
	elif lan.lower() == "e":
		return "eng"
	else:
		return "mul"


def formate_name(text: str) -> str:
	import re
	new_text: str = text.rsplit(".")[0]
	new_text: str = new_text.rsplit("[")[0]
	new_text: str = re.sub("_+", " ", new_text)
	new_text: str = re.sub(" +", "_", new_text)
	new_text: str = new_text.replace("_-_", "-").lower()
	return new_text.removesuffix("_")


def find_folder(path: str) -> bool:
	if os.path.exists(path):
		if os.path.isdir(path):
			return True
		else:
			return False
	else:
		exit(f"'{path}' --> Is not a directory of your computer.")


def find_videos(path) -> bool:
	all_videos = [n for n in os.listdir(path) if n.endswith((".mkv", ".mp4", "webm"))]

	if len(all_videos) == 1:
		return False
	elif len(all_videos) > 1:
		return True
	else:
		exit(f"There is no file video file in --> '{path}'")


def convert_time_to_int(time_string: list[str]) -> int:
	return int(time_string[0]) * 3600 + int(time_string[1]) * 60 + int(time_string[2])


def is_chapters_is_there(name: str) -> bool:
	with open(name + ".txt", "rt") as f:
		file_content: str = f.read()

	for line in file_content.splitlines():
		if ":" in line and line[0:2].isdigit() and line[2] == ":" and line[3].isdigit():
			return True

	return False


def write_chapters(name: str, ) -> str:
	with open(name + ".txt", "r") as f:
		file_content: str = f.read()

	chapters: str = ""
	numbers_of_chapters: int = 0

	for line in file_content.splitlines():
		if ":" in line and line[0:2].isdigit() and line[2] == ":" and line[3].isdigit():

			start: str = line.split(" ", maxsplit=1)[0]
			title: str = line.split(" ", maxsplit=1)[1].title()

			start: list[str] = start.split(":")

			if len(start) == 2:
				start: list[str] = ['00'] + start

			numbers_of_chapters += 1
			chapters += f"""CHAPTER{numbers_of_chapters}={":".join(start)}.000\nCHAPTER{numbers_of_chapters}NAME={title}\n\n"""

	with open(name + "_chapters.txt", "w") as f:
		f.write(chapters)

	return name + "_chapters.txt"


def merge_all_content(all_file: list[str], output_path: str, input_path: str, lan: str) -> tuple:
	if find_folder(output_path):
		playlist = 0
		single_video = ""
		play_list_or_not = find_videos(input_path)

		for i in all_file:
			if i.endswith((".mkv", ".mp4", "webm")):
				name: str = i.rsplit(".")[0]

				if play_list_or_not:
					print(f"Working on video {playlist}", end="\r")
				else:
					print(single_video)

				merge_task = pymkv.MKVFile(title=formate_name(name).replace("_", " "))

				merge_task.add_track(pymkv.MKVTrack(i, track_id=0, track_name=formate_name(name), language=lan, default_track=True))
				merge_task.add_track(pymkv.MKVTrack(i, track_id=1, track_name=formate_name(name), language=lan, default_track=True))

				single_video += f"'{i}' as a main video file.\n"

				if name + ".jpg" in all_file:
					merge_task.add_attachment(name + ".jpg")
					single_video += f"* >>> cover album.\n"

				if name + ".srt" in all_file:
					merge_task.add_track(pymkv.MKVTrack(input_path + name + ".srt", track_name=formate_name(name), language="eng"))
					single_video += f"* >>> subtitle file.\n"

				if name + ".txt" in all_file:
					if is_chapters_is_there(name):
						single_video += f"* >>> chapters file.\n"
						write_chapters(name)
						merge_task.chapters(input_path + name + "_chapters.txt", lan)

				merge_task.mux(output_path + formate_name(name)+".mp4")
				playlist += 1


os.system(get_type_system()[0])

input_path: str = input("Insert input folder path >> ") + get_type_system()[1]

if find_folder(input_path):
	if find_videos(input_path):  # If present directory is not playlist
		pass
	else:  # If present directory is not a playlist
		os.chdir(input_path)
		all_file: list[str] = os.listdir()
		language = get_lan()
		output_path = input("Insert the output path >> " or "") + get_type_system()[1]

		init = time()
		merge_all_content(all_file, output_path, input_path, language)
		print(" DONE ".center(20, "="))
		print(f"Total time >>> {strftime('%H:%M:%S', gmtime(time() - init))} is taken.")
else:
	exit(f"'{input_path}' --> Is not a folder.")
