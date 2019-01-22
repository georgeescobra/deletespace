import os 

path = os.getcwd()
filenames = os.listdir(path)
for filename in filenames:
	 os.rename(os.path.join(path, filename), os.path.join(path, filename.replace(' ', '')))

#this program deletes spaces from the name for files and directories
#it is a lot easier to go to the directories and call files in terminal
#if there are no spaces in name

#in order to use:
#just put the program in the directory you want to change the names with 
#then just run the program in command line "python deletespace.py" 
