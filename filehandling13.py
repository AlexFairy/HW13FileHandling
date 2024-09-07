#Expected Outcome: 
# The script should correctly list all files and subdirectories in the specified directory. 
# Handle exceptions for invalid paths or inaccessible directories.

#My study notes included to help my understand the program when I get back to overlooking the assignment again
import os

def list_directory_contents(path='.'):
  try:
    for x in os.listdir(path): #Note: OS.LISTDIR() for listing contents of a directory
      all_files = os.path.join(path, x) #Note: Join gets iterables and places them in a string
      if os.path.isdir(all_files): #Note: OS.PATH.ISDIR() for a directory
        list_directory_contents(all_files) #the function/parameter
      else:
        print(all_files)
  except PermissionError:
    print("You don't have permission to write to this file.")
  except Exception as e:
    print(f"A general error occured: {e}")

specific_path = './' #Apporpiate format for file reading. 
list_directory_contents(specific_path)
