<h1 style="text-align:center; color:black">Files Sorter</h1>
Files Sorter is a single python file script that Automatically Sort files in the current working directory based on their extensions it creates a new directory (folder) for every type of file extension then move the file from current directory to the created directory every new directory is name extension_files.
The script uses 3 python modules

- re
- os
- shutil

> **re** for finding the extension of files one one re function is used *re.findall()*
> 
> **os** for finding files in the current directory using *os.listdir()*
>
> **shutil** for moving files between directories usng *shutil.move()*
>

Apart from that I have used Python dictionary to save what files have been stored where the script print the dictionary so you can see what files have been moved

#### Running the Script

to run script first clone this repo using git bash or cmd
```cmd
git clone https://github.com/ahmadktk032/File-Sorter.git
```

Navigate to that directory then run the following command

```cmd
python filesorter.py
```

create by **Ahmad** <br>LinkedIn https://www.linkedin.com/in/ahmadktk1
___