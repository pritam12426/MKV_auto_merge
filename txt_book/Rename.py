from getpass import getuser  # Importing getuser from getpass: this is 'getuser' return user name of system
from rich.table import Table  # Importing Table object from rich module
from rich.console import Console  # Importing Console object from rich module
import os  # Importing os module


def newName(old_name):  # Creating a function with name 'newName'

    global folder  # Assigning a local variable to global variable of name 'folder'
    global hidden  # Assigning a local variable to global variable of name 'hidden'
    global files  # Assigning a local variable to global variable of name 'files'

    if not old_name.startswith("."):  # If 'old_name' dose not start with '.' dot.

        if os.path.isfile(old_name):  # Check if 'old_name' is a file
            # Below this line: This will assignee 2 variable with 'name' and 'extension'
            # File name will 'assine' to name varible. Note: 'name' varable only carry file name not extension like '.txt', '.pdf' ect.
            name, extension = old_name.split(".")[:-1], old_name.split(".")[-1].lower() 
            name = "_".join(name).title()
            name = name.replace(" ", "_")
            new_names = f"{name}.{extension}"
            os.rename(old_name, new_names)
            files += 1

        elif os.path.isdir(old_name):
            new_names = old_name.replace(" ", "_").lower()
            os.rename(old_name, new_names)
            folder += 1

    else:
        hidden += 1


if os.getcwd() == os.environ["HOME"] or os.getcwd().startswith("c:"):  # If you 'path' Variable is a 'home directory'
    exit(Console().print(
        f"Sorry, this [bold color(9)]'{os.getcwd()}'[/] is a [bold color(5)]'Home'[/] directory of user [bold color(51)]'{getuser().capitalize()}'[/]. :skull:"))

all_file = os.listdir()  # Will list all 'file' and 'folder' of Present working dir

if ".git" in all_file:
    exit(Console().print(
        f"Sorry, this [bold color(9)]'{os.getcwd()}'[/] :eyes: is a [bold color(5)]'Git repository'[/]. :skull: :gun:"))

Console().print(
    f"Still you wants to continue there are '{len(all_file)}' items in '{os.getcwd()}' :eyes:", style="color(51)", end=" ")
permission = input("this directory [y/n] > ")
if permission == "n":
    exit(Console().print(f"Canceled for directory '[color(21)]{os.getcwd()}[/]' :no_mouth:"))

folder = 0  # Assigning a Variable with name 'folder'
hidden = 0  # Assigning a variable with name 'hidden'
files = 0  # Assigning a variable with name 'files'

for old_name in all_file:
    newName(old_name)

# Below this line: just printing operation info in a table. For more go to 'r'
table = Table(title=f"About '{os.getcwd().split('/')[-1].lower()}' directory")

table.add_column("All items", style="color(51)")
table.add_column("Folder", style="color(11)")
table.add_column("Files", style="color(10)")
table.add_column("Hidden", style="bold color(9)")

table.add_row(f"{len(all_file)}", f"{folder}", f"{files}", f"{hidden}")

exit(Console().print(table))
