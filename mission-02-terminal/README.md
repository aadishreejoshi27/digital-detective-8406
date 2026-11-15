--> Task 2.1

> current-directory display(pwd)- it prints the path of the folder we are currently working in. i observed.. /user/aadishree/digital-detective-8406

> directory listing(ls)- lists all files and folders inside the current directory. i observed.. all the folders from mission 00 to mission 08 and each one havings its own README.md file

> detailed listing (ls-la or ls-l)- lists all the files and folders in the long format including the ones which are hidden. i observed.. all the files and folder with each of them having their one line information about their permissions (rwx)

> change directory (cd..)- moves up to the parent directory.

> create directory (mkdir)- creates a new folder 

> create empty file (touch)- creates a new file inside the current directory.

> copy file (cp)- copies the content of a file into a new file while keeping the original file same.

> move/transfer file (mv)- renames or moves a file 

> display file content (cat)- prints a file's contents. 


--> Task 2.2

> The main difference between replacing a file's content and adding text to the end is that when we replace the content the previous content gets earsed while when we add the text to the end we keep the previous content intact and only add new content.

> The difference between copying and moving a file is when we copy the original file stays where it is. while in moving the location of the file changed to new one. 

> The current directory display (pwd) tells us where in the folder/file structure are we currently working.

> A directory listing operation is useful to check what all files and folders already exists helping us to avoid errors like creating same folders/files twice or deleting something which wasn't supposed to be deleted. 


--> Task 2.3

> When we simply use the ls command we only get the names of the files and folders inside the current directory. But when we use ls -la command we also get the information about the permissions allowed for each file and folder and even the hidden content if any.

> (ls -l | head) The pipe symbol joins two commands in such a way that the output of the command on the left becomes the input for the command on the right side of the pipe. 