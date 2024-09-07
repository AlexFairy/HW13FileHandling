#Expected Outcome: 
# The script should correctly list all files and subdirectories in the specified directory. 
# Handle exceptions for invalid paths or inaccessible directories.

import os

def list_directory_contents(path='.'):
  try:
    for x in os.listdir(path):
      all_files = os.path.join(path, x)
      if os.path.isdir(all_files):
        list_directory_contents(all_files)
      else:
        print(all_files)
  except PermissionError:
    print("You don't have permission to write to this file.")
  except Exception as e:
    print(f"A general error occured: {e}")

specific_path = './'
list_directory_contents(specific_path)
  



try:
  with open('my_garden.txt', 'a') as file:
    file.write("\nNew garden log entry")
except PermissionError:
  print("You don't have permission to write to this file.")
except IOError:
  print("An issue occured while writing the file.")
except Exception as e:
  print(f"A general error occured: {e}")
