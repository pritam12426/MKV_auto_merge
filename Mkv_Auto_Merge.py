print("Loading...")
import os
import yt_dlp
import pymkv
import sys
from time import time, strftime, gmtime

# TODO: add merging command in merge_all_file function. for pymkv


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


def load_json(link: str) -> dict:
	ydl_opts = {}

	with yt_dlp.YoutubeDL(ydl_opts) as ydl:
		info = ydl.extract_info(link, download=False)
		return ydl.sanitize_info(info)


def find_videos(path) -> bool:
	all_videos = [n for n in os.listdir(path) if n.endswith((".mkv", ".mp4", "webm"))]
	if len(all_videos) == 1:
		return False

	elif len(all_videos) > 1:
		return True

	else:
		exit(f"There is no file video file in --> '{path}'")


# def is_chapters(data: dict) -> list[str]:
# 	if data.get('chapters') != None:
# 		return data.get('chapters')


# def add_meta_data(data: dict):
# 	pass


def merge_all_file(all_file: list[str], output_path: str, input_path: str, lan: str) -> None:
	if find_folder(output_path):

		for i in all_file:
			if i.endswith((".mkv", ".mp4", "webm")):
				name: str = i.rsplit(".")[0]

				merge_task = pymkv.MKVFile(title=formate_name(name))

				merge_task.add_track(pymkv.MKVTrack(i, track_id=0, track_name=formate_name(name), language=lan, default_track=True))
				merge_task.add_track(pymkv.MKVTrack(i, track_id=1, track_name=formate_name(name), language=lan, default_track=True))

				if name + ".jpg" in all_file:
					merge_task.add_attachment(name + ".jpg")

				if name + ".srt" in all_file:
					merge_task.add_track(pymkv.MKVTrack(input_path + name + ".srt", track_name=formate_name(name), language="eng"))

				merge_task.mux(output_path + formate_name(name)+".mp4")


os.system(get_type_system()[0])

input_path: str = input("Insert input folder path >> ") + get_type_system()[1]

if find_folder(input_path):
	if find_videos(input_path):
		pass

	else:
		os.chdir(input_path)
	all_file: list[str] = os.listdir()
	language = get_lan()
	# url: str = input("Insert Video url >> " or "")
	output_path = input("Insert the output path >> " or "") + get_type_system()[1]

	init = time()
	merge_all_file(all_file, output_path, input_path, language)
	print(" DONE ".center(20, "="))
	print(f"Total time >>> {strftime('%H:%M:%S', gmtime(time() - init))} is taken.")

else:
	exit(f"'{input_path}' --> Is not a folder.")
