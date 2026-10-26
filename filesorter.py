def fileManager():
    import os
    import shutil
    import re
    files = {}
    all = os.listdir()
    for item in all:
        extension = "".join(re.findall(r"\.\w+",item))
        if extension[1:] not in files.keys():
            files[extension[1:]] = item
            os.mkdir(extension[1:] + "_files")
        
        else:
            files[extension[1:]] = item
        destination = extension[1:]+"_files"
        
        shutil.move(item,f"{destination}/{item}")
    
    print(f"Files are now sorted  here is the details \n{files}")
        
if __name__ == "__main__":
    fileManager()