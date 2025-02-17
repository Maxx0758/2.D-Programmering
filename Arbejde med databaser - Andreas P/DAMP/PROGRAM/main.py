import sys, os


def nav_to_folder_w_file(folder_path: str):
  abs_file_path = os.path.abspath(__file__)                # Absolute Path of the module
  file_dir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
  parent_dir = os.path.dirname(file_dir)                   # Directory of the Module directory
  new_path = os.path.join(parent_dir, folder_path)   # Get the directory for StringFunctions
  sys.path.append(new_path)


# APP---------------------------------------------------------
nav_to_folder_w_file('PROGRAM/APP')
import loading
# ------------------------------------------------------------

loading.start()