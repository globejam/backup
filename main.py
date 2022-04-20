import os
import shutil
import time

def main():
    deleted_folders_count = 0
    deleted_files_count = 0
    path = "C:\Fahmeeda\Downloads\Videos\Pictures"
    days = 30
    seconds = time.time() - (days * 24 * 60 * 60)

    if os.path.exists(path):
        for root_folder, folders, files in os.walk(path):
            if seconds >= getAgeofFileOrFolder(root_folder):
                remove_folder(root_folder)
                deleted_folders_count += 1
                break
            else:
                for folder in folders:
                    folder_path = os.path.join(root_folder, folder)
                    if seconds >= getAgeofFileOrFolder(folder_path):
                        remove_folder(folder_path)
                        deleted_folders_count += 1
                for file in files:
                    file_path = os.path.join(root_folder, file)
                    if seconds >= getAgeofFileOrFolder(file_path):
                        remove_file(file_path)
                        deleted_files_count += 1
    else:
        print("Error!")
        deleted_files_count += 1
    print(f"Alert! Number of Folder Deleted: {deleted_folders_count}")
    print(f"Alert! Number of Files Deleted: {deleted_files_count}")

def remove_folder(path):
    if not shutil.rmtree(path):
        print("Alert! Folder Removed.")
    else:
        print("Sorry... Unable to remove folder.")

def remove_file(path):
    if not os.remove(path):
        print("Alert! File Deleted.")
    else:
        print("Sorry... Unable to delete file.")

def getAgeofFileOrFolder(path):
    ctime = os.stat(path).st_ctime
    return ctime

main()
