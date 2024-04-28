import shutil
import os
 
# path to source directory
src_dir = 'C:\Test_main'
 
# path to destination directory
dest_dir = 'C:\Test_Backup'

files = os.listdir(src_dir)
shutil.copytree(src_dir, dest_dir)

