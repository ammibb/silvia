# File: homework2.py

# Your file path should look like:
# python_decal_fa25/yourname/homework2/homework2.py

# Questions (Answer these in the homework2.py file as comments):

# 1) What’s the difference between Git, GitHub, and Git Bash?
#Git Bash is used as a terminal on Windows that allows you to run Git commands, though Mac does not use this. 
#GitHub is a website where Git repositories are at, it allows you to collaborate, share code, backup your repositories and view history. 
#Now, Git is an installed software that lives on your computer and allows you to track changes and has the commands git add, commit, init etc.
# 2) What’s the difference between the terminal and the command line?
#The terminal allows me to communicate with my computer, it works as the interface, where the command line does the work that interprets the commands.
# 3) How does Windows PowerShell differ from Git Bash?
#Windows Powershell does not come with Git commands, where Git Bash has built-in git commands. 
#Powershell already comes with the Windows software, where GitBash is Git for windows. 
# 4) What’s the difference between Anaconda, conda, and Python?
#Anaconda holds both conda and Python. Conda then manages Python, can install python packages and manage Python versions. Python then is the programming language itself and 
#uses all the capabilites under conda and Python. So, Anaconda --> Conda --> Python
# 5) What is VS Code? 
#VS Code is Visual Studio Code. It is a very useful tool as it for 1. Is a code editor/development environment. 2. Lets you write in multiple languages
#3. Has easy to understand software, as it flags any errors, gives you any tips, color codes, etc. 4. There are many more posibilites, it debugs, has an integrated terminal and much more. 
# 6) What is a Jupyter Notebook? How is it different from Jupyter Lab?
#Jupyter Notebook is an online platform. It is common to use in data science as it allows for a mixture of code. You can also write code in cells (editable blocks with code). Now, Jupyter Lab is a mcuh more verstalie version of Jupyter Notebook.
#It allows you to write, edit, and run code in one place. You can have multiple notebooks and is very flexible with its interface. This is ideal for big projects.
# 7) What does ~/ mean?
# the tilde stands for the main/home directory, and the slash allows you to change/ go into files/folders. So together, ~/(file/folder) represents going to a file/folder in your home directory.
# 8) What’s the difference between an absolute path and a relative path?
#The absolute path takes the path from the home/main directory. Whereas the relative path allows you to change from your current directory
# 9) Imagine you're in your "yourname" repo. Write the absolute and relative paths to "course_assignments/homework2".
#relative path : cd .. /course_assigments/homework2   absolute path: cd ~/python_decal_sp26/course_assignments/homework2
# 10) What command lets you move from "course_assignments/homework2/" to "course_assignments/"?
#cd ..
# 11) What would rm ./ do in your current directory? (Don’t try it!)
#since . stands for the current directory, rm ./ removes all the files in the current directory
# 12) What do the following commands do?
# git add : this saves our files and enters the staging area
# git commit: this finally confirms our work and git properly saves everything
# git push: This is used after the pervious commands and allows our local repository to save changes to the remote repository.
# 13) What's the difference between "git add ." and "git add <file>"?
# git add . saves all the files in the repository, whereas the latter only saves the specified file. 
# 14) What do "git status" and "git log -1" do?
#git status shows you the current status of the repository, such as if you have any unsaved work. git log shows the recent commit history, so with the -1, only shows the information for the most latest commit.
# 15) What’s the difference between cloning a repository and pulling from it?
#Cloning a repository makes a full copy of a remote repository, such as one on GitHub. Then, you can pull from this repository, in which you update your local copy with the changes from the remote repository.
#So pulling comes after cloning a repository. 
# 16) What has been your most frustrating bug or error in this class so far? How did you troubleshoot or fix it?
#the most frustrating error I've had so far was when I couldn't figure out my directories and the files in them. So to troubleshoot it, I had asked ChatGPT for help as I wasn't 
#completely familiar with the work I was doing yet, so after some advice, I was able to figure out that I had not placed my folders in the correct spot and was able to move the work arorund.
# 17) What’s a question you still have? What’s something you’re confused about?
#I don't have any questions, it's more of there are stuff I am still not 100% familiar with so they get me confused at times. Otherwise I'll learn in due time.
# 18) Tell me a fun fact!
#Otters hold hands while they sleep so they don't drift away!
# 19) Print your favorite math expression you've learned in Python so far. 
print(11 % 10) #this prints the remainder of the 10/11, so it would be 1. 
# (Hint: Use print() and add a comment explaining what it does.)