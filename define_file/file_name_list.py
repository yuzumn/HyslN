#データを読み込んだcsvファイルを表示するウィンドを生成､制御している。
import tkinter as tk

sub = None

def namelist(f_name,B_data,B_mT_data,C_data,D_data,E_data,degC_data,degD_data,cf_x,cf_y):
    global sub,chk
    global output_data_B,output_data_B_mT,output_data_C,output_data_D,output_data_E,output_data_deg_C,output_data_deg_D
    global cf_data_x,cf_data_y
    
    output_data_B = B_data
    output_data_B_mT = B_mT_data
    output_data_C = C_data
    output_data_D = D_data
    output_data_E = E_data
    output_data_deg_C = degC_data
    output_data_deg_D = degD_data
    
    cf_data_x = cf_x
    cf_data_y = cf_y
    
    chk = {}
    colorlist = ["red", "green", "blue", "cyan", "magenta", "gold3", "black",
                "dodger blue","orange","lime green",
                "red2","purple","brown",
                "pink","gray","olive","dark turquoise"]
    
    if sub == None or not sub.winfo_exists():
        sub = tk.Toplevel()
        sub.geometry("320x400")
        sub.title("ファイル一覧")
        sub.configure(bg='pale green')
        sub.resizable(0,0)
        file_delet_button = tk.Button(
            sub,text='削除',font=("明朝体","10","bold"),foreground='black',command=lambda filename=f_name: file_delet(filename)).place(x=235,y=365,width=80,height=30)
        
        frame = tk.Frame(
            sub,relief=tk.SUNKEN,bd=2).place(x=1,y=3,width=230,height=395)
        
        canvas = tk.Canvas(sub,width=225,height=390,bg="white")
        canvas.place(x=1,y=4.5)
        #canvas.grid(row=1,rowspan=len(f_s_name),column=0,columnspan=5)
        
        for i in range(len(f_name)):
            chk[i] = tk.BooleanVar()
            chk_f = tk.Checkbutton(sub,variable=chk[i],text=f_name[i],font=("明朝体","17","bold"),fg=colorlist[i],bg="white")
            chk_f.place(x=3,y=7+10*i*4)

def file_delet(f_s_name):
    global chk
    for i in range(len(f_s_name)):
        if chk[i].get() == True:
            del f_s_name[i]
            del output_data_B[i]
            del output_data_C[i]
            del output_data_D[i]
            del output_data_E[i]
            if cf_data_x > 0:
                del output_data_B_mT[i]
            if cf_data_y > 0:
                del output_data_deg_C[i]
                del output_data_deg_D[i]
    sub.update()
