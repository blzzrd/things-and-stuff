# Import the OS Module, the Time Module, and the System Module.
import os, time, sys

# Get the current working directory
current_path = os.getcwd()

# Get the current time.
now = time.time()

# os.listdir returns a list of files/dirs in the specified directory.
files_removed = 0
for files in os.listdir(current_path):
	# Go through each of the files and create an absolute file path.
	f = os.path.join(current_path, files)
	
	# Check to see if the file is older than 14 days. (in seconds):
	if os.stat(f).st_mtime < now - (14 * 24 * 60 * 60):
		# .st_atime = time of last access.
		# .st_ctime = time of last change.
		# .st_mtime = time of last modification.
		
		# If the object is a file, delete it.
		if os.path.isfile(f):
			os.remove(f)
			files_removed += 1

# Print out your output.
print("{} files removed.".format(files_removed))
		

