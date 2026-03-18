#1. Git is the version control system locally installed on the computer, whereas GitHub is a web-based service and can host your repository online.
#Terminal is the application that holds the command line. So the command line is what executes whatever we write into it.
#A local repository is one that lives in your personal computer, where as a remote repository is one that can be accessed outside of the personal computer.
#4. Version control is a system tha tracks and manages changes to software code or documents over time.
#5. Staging Area is the step in which files are ready to be picked in order to move onto the next stage of committing the changes.
#6. Git add is a command to add changes from the working directory into the staging area, and gets it ready to be committed.
#7. Git commit saves all the changes, where -m allows for a message which is useful for tracking what we have done.
#8. Git push then puts all the work into the remote repository .
#9. Git status shows you what files were modified, staged, or not being tracked.
#10. Git pull is used to to obtain and download content from a remote repository and upload/update the changes into the local repository.
#11. Pwd- this prints the current working directory, so whichever folder you are in. 
#12. ls is used to list the content in a folder/directory. 
#13. cd is short for change directory, so it allows you to move from a parent folder/directory into directory within it.
#14. nano is a text editor you use inside the terminal.
#15. touch allows you to create files, this also doesn't automatically open it.
#16. mv is used to move content into different directorires or places, it can move files, folders, etc.
#17. rm is used to remove files or directories permanently.
#18. cat: cat is short for concatenate, this can display the content of files, combine mutliple files, or create a new file(which inserts you into said file).

#3.2 QUESTIONS
#1. pwd 
#2. ls 
#3. To move into correct repository: cd ../brianna_repo    To pull the latest changes: git add, git commit -m "updated h2.py", git push
#4. mv homework.py ../judy_decal/homework
#5 cd homework1 
#6 cat homework.py
#7. git add, git push -m "done w homework", git commit 
#8. This error meannt that theere were new commits in the remote repository that were not present in the local branch, thus to fix this, simply call git pull (pulls and merges any changes into the local repository).
#9 cd ~/Recent

#3.3


#3.4
def checkDataType(data):
    return(f"{type(data).__name__}") #this gives me a shortcut to return only a class type's name.

#4.2
def evenOrOdd(number):
    if number%2==0:
        return("Even")
    else: 
        return("Odd")

#5
def sumWithLoop(numbers):
    sum=0
    for i in range(len(numbers)):
        sum+=numbers[i]
    return sum

#6.1
def duplicateList(list): #using insert in place of append as insert moves the previous element one over
    holder=""
    newlist=list.copy()
    place=0
    for i in range(len(list)):
        holder=list[i]
        newlist.insert(place, holder)
        place+=2
    return(newlist)

#6.2
def square(num):
    return(num*num)

hello=["a","b","c","d","h"]
print(duplicateList(hello))