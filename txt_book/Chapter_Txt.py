import os
from rich.console import Console

output_paht = input("Inset the output path > ")  # will take input for working directory from the user.
os.chdir(output_paht)  # Will chagne the directory to output_path.

all_file = os.listdir()  # Will list all file or floer of working directory.

n = 0
for i in all_file:  # will loop all file that is present in the directory.
	if i.endswith(".mp4"):  # Will find file that is ending with ".mp4" word.
		file_name = i.split(".")[0]  # Will remover ".mp4" from the file name.
		n += 1

if n != 1:
	'''If ther is not file that is endwith '.mp4' or multipel file 
	in working directory. The program will automaticli exit.'''
	Console().print(f"\nThere are '{n}' [color(13) bold]'.mp4'[/] file in [color(9)]'{os.getcwd()}'[/] :eyes: directory\n")
	exit()

open(f"{file_name}_Chater.txt", "w") # Will make sure that "file chater.txt" is empity.


def write():

	chapter = 1
	while(True):
		time = input(f"\nInset the time of chapter {chapter} > ")
		if time == "": # If The value of tiem is empity then file will close. 
			os.system("clear")
			Console().print(f'[color(2)]Totle chapters are {chapter} done[/]')
			exit()
		else:
			with open(f'{file_name} Chater.txt', 'a') as file:
				name = input(f"Inset the name of chapter {chapter} > ")
				file.write(str(f'CHAPTER{chapter}={time}.000\n')) # Will write the timeing of chapter.
				file.write(str(f'CHAPTER{chapter}NAME={name.title()}\n')) # Will write the chagne name.
				chapter += 1

write()