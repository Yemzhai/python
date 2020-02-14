
def isExist(input):
     if os.path.exists(input): return True
     else: return False

def workWithFile():
    print("YOU WORK WITH FILE\nChoose your action\n"
                "!Should watch witch file exist witch not: SHOW LIST?\n"
                "\t1: list of all file\n"
                "\t2: delete file\n"
                "\t3: rename file\n"
                "\t4: add content to this file\n"
                "\t5: rewrite content of this file\n"
                "\t6: return to the parent directory \n"
                "\t7: EXIT"
        )
    choose = int(input())
    if(choose == 1):
        direc = "C:/Users/77474/Desktop/coding/python/for_lab_3"
        for i in os.listdir(direc):
            if os.path.isfile(os.path.join(direc, i)):
                print(i)
        # files = os.listdir()
        # print(files)
    elif(choose == 2):
        print("write witch file you want to delete");
        file = str(input());
        if(isExist(file)): 
            os.remove(file)
            print(file+' removed!\n')
        else: print("The file doesn't exist\n")
    elif(choose == 3):
        print("write witch file you want to rename");
        file = str(input());
        if (isExist(file)): 
            print("Enter a new name for file")
            newName = str(input())
            os.rename(file, newName)
            print(file+' renamed!\n')
        else: print("The file doesn't exist\n")
    elif(choose == 4):
        print("In witch file you want to add content");
        file = str(input())
        if(isExist(file)): 
            print("Please write what you want to add")
            newContent = str(input())
            with open(file, 'a+') as myFile:
                myFile.write(newContent+'\n')
            print("New content added!\n")
        else: print("The file doesn't exist\n")
    elif(choose == 5):
        print("In witch file you want to add content");
        file = str(input())
        if(isExist(file)): 
            print("Please write what you want to rewrite")
            newContent = str(input())
            with open(file, 'w+') as myFile:
                myFile.write(newContent+'\n')
            print("You rewrite content of this file\n")
        else: print("The file doesn't exist\n")
    elif(choose == 6):
        path = os.getcwd()  
        parent = os.path.dirname(path)
        # parent = os.path.dirname(parent)
        # print("You parent directory is ", path)
        print("You parent directory is ", parent)
    elif(choose == 7): return 7

def workWithDirectory():
    print("YOU WORK WITH DIRECTORY\nChoose your action\n"
                "!Should watch witch directorycls exist witch not: SHOW LIST?\n"
                "\t0: show listn\n"
                "\t1: rename directory\n"
                "\t2: print number of files in it\n"
                "\t3: print number of directories in it\n"
                "\t4: list content of the directory\n"
                "\t5: add file to this directory\n"
                "\t6: add new directory to this directory \n"
                "\t7: EXIT"
        )
    choose = int(input())
    if(choose == 0):
        print(os.listdir())
    if(choose == 1):
        print("write which directory you want to rename");
        direc = str(input());
        if (isExist(direc)): 
            print("Enter a new name for directory")
            newName = str(input())
            os.rename(direc, newName)
            print(direc+' renamed!\n')
        else: print("The directory doesn't exist\n")
    elif(choose == 2):
        print("With which directory you want to work?")
        direc = str(input())
        if(isExist(direc)):
            cnt = 0
            for i in os.listdir(direc):
                if os.path.isfile(os.path.join(direc, i)):
                    # print(i)
                    cnt += 1
            print("Number of files is directory", direc ,cnt,'\n')
        else: print("The directory doesn't exist\n")
    elif(choose == 3):
        print("With which directory you want to work?")
        direc = str(input())
        if(isExist(direc)):
            cnt = 0
            for i in os.listdir(direc):
                if os.path.isdir(os.path.join(direc, i)):
                    # print(i)
                    cnt += 1;
            print("Number of directory is directory", direc ,cnt,'\n')
        else: print("The directory doesn't exist\n")
    elif(choose == 4):
        print("With which directory you want to work?")
        direc = str(input())
        if(isExist(direc)):
            print(os.listdir(direc), '\n')
        else: print("The directory doesn't exist\n")
    elif(choose == 5):
        print("With which directory you want to work?")
        direc = str(input())
        if(isExist(direc)):
            print("Please write a name of a new file")
            file = str(input())
            newFile = open(os.path.join(direc, file), 'w')
            newFile.close();
            print("You created file ", file, "in directory ", direc, '\n');
        else: print("The directory doesn't exist\n")
    elif(choose == 6): 
        print("With which directory you want to work?")
        direc = str(input())
        if(isExist(direc)):
            print("Please write a name of a new directory")
            drc = str(input())
            path = os.path.join(direc, drc)
            os.mkdir(path)
            print("You created directory ", drc, "in directory ", direc, '\n');
        else: print("The directory doesn't exist\n")
    elif(choose == 7): return 7


import os
import re

path = "C:/Users/77474/Desktop/coding/python/for_lab_3"
os.chdir(path)
while(True):
    print("Which of them you wanna work\n"
            "1: Whith file\n"
            "2: Whith directory"
        )
    inpt = int(input());
    if(inpt == 1 or inpt == 2):
        while(True):
            if(inpt == 1):
                if(workWithFile() == 7): 
                    clear = os.system('cls');
                    break
            elif(inpt == 2):
                if(workWithDirectory() == 7): 
                    clear = os.system('cls');
                    break
    else:  clear = os.system('cls');


        
