#csvファイルをフォルダから選択する制御を行っている。
import os
from tkinter import filedialog as fl

path = os.getcwd()

def file_select(event=None):
    typ = [('csvファイル','*.csv')]
    dir = path
    fle = fl.askopenfilename(filetypes=typ, initialdir=dir)
    
    return fle
