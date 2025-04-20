import shutil
import os
import tkinter
import tkinter.messagebox
from datetime import datetime



def GUI():
    root = tkinter.Tk()
    root.title('Backups')
    root.geometry('450x170')


    button1 = tkinter.Button(root, text=' PAT', width=60, height=5, command=Backup1)
    button2 = tkinter.Button(root, text='Dandelion to Onedrive', width=60 ,height=3, command=Backup2)
    global confirm
    confirm = tkinter.Entry(root, width=50, fg='Blue', borderwidth='1')
    
  
    button2.pack()
    button1.pack()
    confirm.pack()

    root.mainloop()

def Backup1():   # Backup the PAT
    if not os.path.exists('WhatToBackup.txt'):
            tkinter.messagebox.showerror('Error', 'WhatToBackup.txt not found.')
            return None
    
    if not os.path.exists('BackupLocations.txt'):
            tkinter.messagebox.showerror('Error', 'BackupLocation.txt not found.')
            return None
    
    with open('WhatToBackup.txt', 'r') as PathLocation:      # Read the Path of the PAT from the txt file
        Path = PathLocation.read()

    if not os.path.exists(Path):
       tkinter.messagebox.showerror('Error', f'{Path} not found.')
       return None
 
    dates =f'{datetime.now().year}-{datetime.now().month}-{datetime.now().day}---{datetime.now().hour}--{datetime.now().minute}--{datetime.now().second}'

    #CopyTo = f'C:/Users/vdspoel.r2025.it/OneDrive - hsrandburg.co.za/IT\Files Transfer/Files/PAT/{dates}'    # Iterate thru txt file and backup to all locations

    with open('BackupLocations.txt', 'r') as file:
         for line in file:
              CopyTo = f'{line}/{dates}'
              shutil.copytree(Path, CopyTo)

    #shutil.copytree(Path, CopyTo)

    confirm.delete(0, len(confirm.get()))
    confirm.insert(0, 'Files have been copied successfully to Backup Locations')
    


def Backup2():  # Backup the Dandelion files to backup locations  
   

    Path = "K:/Graad 11/IT11 Dandel10n Data2024"                    

    if not os.path.exists(Path):
       tkinter.messagebox.showerror('Error', f'{Path} not found.')
       return None

    dates =f'{datetime.now().year}-{datetime.now().month}-{datetime.now().day}---{datetime.now().hour}--{datetime.now().minute}--{datetime.now().second}'

    CopyTo = f'C:/Users/vdspoel.r2025.it/OneDrive - hsrandburg.co.za/IT\Files Transfer/Files/Dandelion/{dates}'  

    shutil.copytree(Path, CopyTo)
    
    confirm.delete(0, len(confirm.get()))
    confirm.insert(0, 'Files have been copied successfully to OneDrive')
    


def main():
    GUI()


main()
