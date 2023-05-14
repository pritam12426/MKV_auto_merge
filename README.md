# What is it?

**MKV AUTO MERGE** is a command-line interface `CLI` application written in Python. Its primary purpose is to merge video files more efficiently than any graphical user interface ``GUI`` version available. 

The program accepts the file path of the raw video as input and displays which files `can be` merged with it.

## Main Features
MKV AUTO MERGE is a powerful tool that offers a range of features to make video merging fast and efficient. 

Some of its key features include the ability to merge chapter subtitle cover album, as well as automatic recognition of corresponding files for a raw video from a specified folder. 

The application can also automatically detect chapter time and its corresponding chapter name, which can save users a significant amount of time and effort.

With these features, MKV AUTO MERGE provides an effective solution for anyone who needs to merge video files quickly and easily.

## Supported system are
* linux
* macos
* windows (version 7 or later)

## Documentation

### To use mkv auto merge

To ensure successful merging, it is important to keep all the files that need to be merged with the raw video file in the same folder. Additionally, the folder names should match the name of the raw video file.

<details>
  <summary><b>Consider this image for better understanding. </b></summary>
<blockquote><a href="https://github.com/pritam12426/MKV_auto_merge"><img src="https://user-images.githubusercontent.com/84720825/235667397-d77f4e54-6f55-4a4c-b36f-64ed1ccdf531.png"/></a> <p><b>The image shows a folder named "example" that contains four files. The folder has been used as an example to illustrate the importance of keeping all the files that need to be merged in the same folder.By doing this, the user can ensure that all relevant files are in one place and can be accessed easily during the merging process.This approach can help to save time and reduce the risk of errors, particularly when dealing with larger video files or multiple files that need to be merged together.By following this best practice, users can ensure that their merging process is as smooth and efficient as possible.</b></p></blockquote>
</details>

---
## Consider few points while adding chapter in a text file.

* Add all time stamps in a `.txt` file with name as same as raw video file.
* Make sure that the content of the `.txt` file is in the following format:

```
00:00 Intro
03:03 What is YAML
07:20 Data serialization
16:47 What is YAML
19:20 Benefits of YAML
23:10 Demo of YAML file
24:09 Creating a YAML file
24:38 Key datatype
26:16 List datatype
27:08 Block style
28:00 Checking YAML syntax
01:29:03 Differentiate 
```

- Make sure that the maximum time of chapter a is less than the length of the raw video file.
- It is mandatory to add chapters in the `	.txt` file in ascending order.
- The maximum capacity of adding chapter in a raw video file is <kbd>99:60:59</kbd>

## How to get it

### To get started with MKV AUTO MERGE, clone the repl using the following command in your terminal:

### Install mkvtoolnix in your system

#### [MKV Merge](https://mkvtoolnix.download/downloads.html)

```sh
git clone https://github.com/pritam12426/MKV_auto_merge.git
cd  MKV_auto_merge
```

#### Then install the required packages using pip:

```sh
pip install -r Requirments.txt
```

### To run MKV AUTO MERGE on your system:

#### For Linux and macOS, use this command:

```sh
python3 MKV_auto_merge.py
```
#### For Windows, use this command:

```sh
python MKV_auto_merge.py
```

Press <kbd>Ctrl</kbd> or <kbd>Command</kbd> + <kbd>c</kbd> to terminating the processes.

## Known issues

* Currently this application not able to add multiple track for video, subtitle, sound at a time.
*  

## Contribution

MKV AUTO MERGE is an open-source project, and contributions are always welcome. If you have any suggestions or would like to report a bug, please feel free to submit an issue or pull request on the [Project's GitHub repository.](https://github.com/pritam12426/MKV_auto_merge/issues)


