import os, yt_dlp, pymkv, sys


def get_type_system() -> tuple:
	if sys.platform == "win":
		return "cls", "\\"

	elif sys.platform == "linux":
		return "clear", "/"

	else:
		exit("Unsupported system.")


def find_folder(path) -> bool:
	if os.path.exists(path):
		if os.path.isdir(path):
			return True

		else:
			return False

	else:
		exit(f"'{path}' --> Is not a directory of your computer.")


def load_json(link) -> dict():
	ydl_opts = {}

	with yt_dlp.YoutubeDL(ydl_opts) as ydl:
		info = ydl.extract_info(link, download=False)
		return ydl.sanitize_info(info)


def find_videos(path) -> bool:
	all_videos = [n for n in os.listdir(path) if n.endswith((".mkv", ".mp4"))]
	if len(all_videos) == 1:
		return False

	elif len(all_videos) > 1:
		return True

	else:
		exit(f"There is no file video file in --> '{path}'")


def is_chapters(json_data) -> list[str]:
	if not json_data['chapter'] == None:
		pass


input_path: str = input("Insert input folder path >> ") + get_type_system()[1]

if find_folder(input_path):
	os.chdir(input_path)
	all_file: list[str] = os.listdir()
	url: str = input("Insert Video url >> " or "")

	if find_videos(input_path):
		for i in all_file: #  If it is a playlist:
			if i.endswith((".mkv", ".mp4")):
				name: str = i.rsplit(".")[0]

				if name + ".jpg" in all_file:
					pass

				if name + ".srt" in all_file:
					pass

				if url != "":
					if load_json(url)['chapters'] != None:
						print("Found chapters")

	else:
		print("There is only 1 videos.")
else:
	exit(f"'{input_path}' --> Is not a folder.")

