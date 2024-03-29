import os

def rename_files_recursively(folder_path, search_string, 
replace_string):
   for root, dirs, files in os.walk(folder_path):
      for file in files:
         if search_string in file:
            file_path = os.path.join(root, file)
            new_name = file.replace(search_string, 
replace_string)
            new_path = os.path.join(root, new_name)
            os.rename(file_path, new_path)

# usage
rename_files_recursively('./', 'txt', 'html')