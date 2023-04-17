# -*- coding: utf-8 -*-
"""
Created on Wed May  4 13:03:48 2022

@author: yuuri0422
"""
#baseのウィンドを生成､グラフの作成などを行う。
import os
import tkinter as tk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from define_file import csv_data_analysis as al
from define_file import file_select as fs
from define_file import file_name_list as fnl
from define_file import output as op

max_ave = []
min_ave = []

fix = 35

base = tk.Tk()
base.geometry('980x565')
base.configure(bg='pale green')
base.title('Hysteresis Loop Normalization')
base.resizable(0,0)

path = os.getcwd()
photo = tk.PhotoImage(file = path + "\\image\\" + "icon.png")
base.iconphoto(True,photo)

output_data_B = []
output_data_B_mT = []
output_data_C = []
output_data_D = []
output_data_E = []
output_data_deg_C = []
output_data_deg_D = []
f_s_name = []
xxx = 0
xx = 1

flag_inversion = 0
ch_data_ini = ch_data_jus = ch_data_res = ch_data_res_mT = 0

N_save = 1
I_save = 0
NI_save = 0

ver = "a.u."
hol = "V(V)"

plt.rcParams["font.size"] = 7
plt.rcParams['figure.subplot.left'] = 0.23
plt.rcParams['figure.subplot.bottom'] = 0.2
plotsize = 1

def data(f_name):
    global sheetB,sheetB_mT,sheetC,sheetD,sheetE,sheetdeg_C,sheetdeg_D
    global output_data_B,output_data_C,output_data_D,output_data_E,output_data_B_mT,output_data_deg_C,output_data_deg_D
    global max_data,min_data,cf_data_x,cf_data_y
    global xxx,f_s_name,flag_inversion
    
    num_d = txt_num.get()
    max_d = txt_max.get()
    min_d = txt_min.get()
    area_d = txt_area_min.get()
    cf_d_x = txt_cf_x.get()
    cf_d_y = txt_cf_y.get()
    min_r = txt_min_.get()
    max_r = txt_max_.get()

    num_data = int(num_d)
    max_data = float(max_d)
    min_data = float(min_d)
    area_data = int(area_d)
    cf_data_x = float(cf_d_x)
    cf_data_y = float(cf_d_y)
    min_range = float(min_r)
    max_range = float(max_r)
    
    area_sell = txt_area_min_sell.get()
    
    sheet = al.analysis(f_name,num_data,max_data,min_data,area_data,cf_data_x,cf_data_y,min_range,max_range,area_sell,flag_inversion,xxx)
    
    sheetB = sheet[0]
    sheetB_mT = sheet[1]
    sheetC = sheet[2]
    sheetD = sheet[3]
    sheetE = sheet[4]
    sheetdeg_C = sheet[5]
    sheetdeg_D = sheet[6]
    
    output_data_B = sheet[7]
    output_data_B_mT = sheet[8]
    output_data_C = sheet[9]
    output_data_D = sheet[10]
    output_data_E = sheet[11]
    output_data_deg_C = sheet[12]
    output_data_deg_D = sheet[13]
    
    xxx = sheet[14]
    f_s_name = sheet[15]

def callback():
    print('プログラムを閉じる')
    
def reset(event=None):
    global xxx,xx,flag_inversion
    
    txt_file.delete(0,tk.END)
    txt_max.delete(0,tk.END)
    txt_min.delete(0,tk.END)
    txt_max_.delete(0,tk.END)
    txt_min_.delete(0,tk.END)
    txt_max.insert(0,0)
    txt_min.insert(0,0)
    txt_max_.insert(0,0)
    txt_min_.insert(0,0)
    
    del f_s_name[:]
    del output_data_B[:]
    del output_data_B_mT[:]
    del output_data_deg_C[:]
    del output_data_deg_D[:]
    del output_data_C[:]
    del output_data_D[:]
    del output_data_E[:]
    
    xxx = 0
    xx = 1
    flag_inversion = 0

def f_select(event=None):
    global filename
    
    txt_file.delete(0,tk.END)
    txt_max.delete(0,tk.END)
    txt_min.delete(0,tk.END)
    txt_max_.delete(0,tk.END)
    txt_min_.delete(0,tk.END)
    txt_max.insert(0,0)
    txt_min.insert(0,0)
    txt_max_.insert(0,0)
    txt_min_.insert(0,0)
    
    filename = fs.file_select()
    txt_file.insert(tk.END,filename)

def file_enter():
    data(filename)

def file_list():
    fnl.namelist(f_s_name,output_data_B,output_data_B_mT,output_data_C,output_data_D,output_data_E,output_data_deg_C,output_data_deg_D,cf_data_x,cf_data_y)

def initial_graph():
    
    fig = plt.figure()
    fig_canvas = FigureCanvasTkAgg(fig,base)
    fig_canvas.draw()
    fig_canvas.get_tk_widget().place(x=5,y=35+fix*5,width=470,height=350)

    plt.xlim(min(sheetB)-0.25,max(sheetB)+0.25)
    plt.ylim(min(sheetC)-0.25,max(sheetC)+0.25)
    plt.grid(True)
    plt.xlabel("H(V)")
    plt.ylabel("Kerr Signal(V)")
    plt.scatter(sheetB,sheetC,s=plotsize,c="b",marker=".",alpha=0.5)
    
    #toolbar = NavigationToolbar2Tk(fig_canvas, base)
    
def justification_graph():
    if cf_data_x == 0:
        fig = plt.figure()
        fig_canvas = FigureCanvasTkAgg(fig,base)
        fig_canvas.draw()
        fig_canvas.get_tk_widget().place(x=5,y=35+fix*5,width=470,height=350)

        plt.xlim(min(sheetB)-0.25,max(sheetB)+0.25)
        if cf_data_y > 0:
            plt.ylim(min(sheetdeg_D)-0.25,max(sheetdeg_D)+0.25)
        else:
            plt.ylim(min(sheetD)-0.25,max(sheetD)+0.25)
        plt.grid(True)
        plt.xlabel("H(V)")
        plt.ylabel("Kerr Signal(V)")
        if cf_data_y > 0:
            plt.scatter(sheetB,sheetdeg_D,s=plotsize,c="b",marker=".",alpha=0.5)
        else:
            plt.scatter(sheetB,sheetD,s=plotsize,c="b",marker=".",alpha=0.5)
        
    elif cf_data_x > 0:
        fig = plt.figure()
        fig.clear()
        fig_canvas = FigureCanvasTkAgg(fig,base)
        fig_canvas.draw()
        fig_canvas.get_tk_widget().place(x=5,y=35+fix*5,width=470,height=350)

        plt.xlim(min(sheetB_mT)-0.3,max(sheetB_mT)+0.3)
        plt.ylim(min(sheetD)-0.25,max(sheetD)+0.25)
        plt.grid(True)
        plt.xlabel(hol)
        plt.ylabel("Kerr Signal(V)")
        plt.scatter(sheetB_mT,sheetD,s=plotsize,c="b",marker=".",alpha=0.5)
    
def result_graph():
    
    if cf_data_x == 0:
        fig = plt.figure()
        fig.clear()
        fig_canvas = FigureCanvasTkAgg(fig,base)
        fig_canvas.draw()
        fig_canvas.get_tk_widget().place(x=5,y=35+fix*5,width=470,height=350)

        plt.xlim(min(sheetB)-0.25,max(sheetB)+0.25)
        plt.ylim(-1.5,1.5)
        plt.grid(True)
        plt.xlabel("H(V)")
        plt.ylabel("Kerr Signal(" + ver + ")")
        plt.scatter(sheetB,sheetE,s=plotsize,c="b",marker=".",alpha=0.5)
        
    elif cf_data_x > 0:
        fig = plt.figure()
        fig.clear()
        fig_canvas = FigureCanvasTkAgg(fig,base)
        fig_canvas.draw()
        fig_canvas.get_tk_widget().place(x=5,y=35+fix*5,width=470,height=350)

        plt.xlim(min(sheetB_mT)-0.3,max(sheetB_mT)+0.3)
        plt.ylim(-1.5,1.5)
        plt.grid(True)
        plt.xlabel(hol)
        plt.ylabel("Kerr Signal(" + ver + ")")
        plt.scatter(sheetB_mT,sheetE,s=plotsize,c="b",marker=".",alpha=0.5)

def save():
    colorlist = ["r", "g", "b", "c", "m", "y", "k",
                "tab:blue","tab:orange","tab:green",
                "tab:red","tab:purple","tab:brown",
                "tab:pink","tab:gray","tab:olive","tab:cyan"]
    
    if ch_data_ini == 1:
        fig = plt.figure()
        fig.clear()
        fig_canvas = FigureCanvasTkAgg(fig,base)
        fig_canvas.draw()
        fig_canvas.get_tk_widget().place(x=500,y=35+fix*5,width=470,height=350)

        plt.xlim(min(output_data_B[0])-0.25,max(output_data_B[0])+0.25)
        plt.ylim(min(output_data_C[0])-0.25,max(output_data_C[0])+0.25)
        plt.grid(True)
        plt.xlabel("H(V)")
        plt.ylabel("Kerr Signal(" + ver + ")")
        for i in range(xxx):
            plt.scatter(output_data_B[i],output_data_C[i],s=plotsize,c=colorlist[i],marker=".",alpha=0.5)
    
    elif ch_data_jus == 1:
        fig = plt.figure()
        fig.clear()
        fig_canvas = FigureCanvasTkAgg(fig,base)
        fig_canvas.draw()
        fig_canvas.get_tk_widget().place(x=500,y=35+fix*5,width=470,height=350)
        
        if cf_data_x > 0:
            plt.xlim(min(output_data_B_mT[0])-0.25,max(output_data_B_mT[0])+0.25)
        else:
            plt.xlim(min(output_data_B[0])-0.25,max(output_data_B[0])+0.25)
        if cf_data_y > 0.00:
            plt.ylim(min(output_data_deg_D[0])-0.25,max(output_data_deg_D[0])+0.25)
        else:
            plt.ylim(min(output_data_D[0])-0.25,max(output_data_D[0])+0.25)
        plt.grid(True)
        plt.xlabel("H(V)")
        plt.ylabel("Kerr Signal(" + ver + ")")
        for i in range(xxx):
            if cf_data_y > 0.00:
                plt.scatter(output_data_B[i],output_data_deg_D[i],s=plotsize,c=colorlist[i],marker=".",alpha=0.5)
            else:
                plt.scatter(output_data_B[i],output_data_D[i],s=plotsize,c=colorlist[i],marker=".",alpha=0.5)
    
    elif ch_data_res == 1:
        fig = plt.figure()
        fig.clear()
        fig_canvas = FigureCanvasTkAgg(fig,base)
        fig_canvas.draw()
        fig_canvas.get_tk_widget().place(x=500,y=35+fix*5,width=470,height=350)

        plt.xlim(min(output_data_B[0])-0.25,max(output_data_B[0])+0.25)
        plt.ylim(-1.5,1.5)
        plt.grid(True)
        plt.xlabel("H(V)")
        plt.ylabel("Kerr Signal(" + ver + ")")
        for i in range(xxx):
            plt.scatter(output_data_B[i],output_data_E[i],s=plotsize,c=colorlist[i],marker=".",alpha=0.5)
    
    elif cf_data_x > 0 and ch_data_res_mT == 1:
        fig = plt.figure()
        fig.clear()
        fig_canvas = FigureCanvasTkAgg(fig,base)
        fig_canvas.draw()
        fig_canvas.get_tk_widget().place(x=500,y=35+fix*5,width=470,height=350)

        plt.xlim(min(output_data_B_mT[0])-0.25,max(output_data_B_mT[0])+0.25)
        plt.ylim(-1.5,1.5)
        plt.grid(True)
        plt.xlabel(hol)
        plt.ylabel("Kerr Signal(" + ver + ")")
        for i in range(xxx):
            plt.scatter(output_data_B_mT[i],output_data_E[i],s=plotsize,c=colorlist[i],marker=".",alpha=0.5)

def inversion(event=None):
    global flag_inversion
    flag_inversion = 1
    del f_s_name[:]
    del output_data_B[:]
    del output_data_B_mT[:]
    del output_data_deg_C[:]
    del output_data_deg_D[:]
    del output_data_C[:]
    del output_data_D[:]
    del output_data_E[:]

def change_data():    

    global ch_data_ini,ch_data_jus,ch_data_res,ch_data_res_mT
    
    change_data = spin_.get()
    
    if change_data == '初期データ':
        ch_data_jus = ch_data_res = ch_data_res_mT = 0
        ch_data_ini = 1
    
    elif change_data == '原点揃え':
        ch_data_ini = ch_data_res = ch_data_res_mT = 0
        ch_data_jus = 1
    
    elif change_data == '規格化(V)':
        ch_data_ini = ch_data_jus = ch_data_res_mT = 0
        ch_data_res = 1
    
    elif change_data == '規格化(係数)':
        ch_data_ini = ch_data_jus = ch_data_res = 0
        ch_data_res_mT = 1

def unit_v(unit):
    global ver
    ver = unit

def unit_h(unit):
    global hol
    hol = unit

def data_output():
    op.data(f_s_name,xxx,sheetC,output_data_B,output_data_B_mT,output_data_D,output_data_E,output_data_deg_D,cf_data_x,cf_data_y,hol,ver)
    op.output_det()  

def data_output_s(self):
    op.data(f_s_name,xxx,sheetC,output_data_B,output_data_B_mT,output_data_D,output_data_E,output_data_deg_D,cf_data_x,cf_data_y,hol,ver)
    op.output_det()        
            
men = tk.Menu(base)
base.config(menu=men)

file_1 = tk.Menu(men,tearoff=0)
men.add_cascade(label='ファイル',menu=file_1)
file_1.add_command(label='ファイルを開く',font=("明朝体","15"),accelerator="Ctrl+O",command=f_select)
base.bind_all("<Control-o>",f_select)
file_1.add_command(label='保存データの指定',font=("明朝体","15"),accelerator="Ctrl+S",command=data_output)
base.bind_all("<Control-s>",data_output_s)
file_1.add_separator()
file_1.add_command(label='閉じる',font=("明朝体","15"),command=callback)

file_2 = tk.Menu(men,tearoff=0)
men.add_cascade(label='オプション',menu=file_2)
file_2.add_command(label='反転',font=("明朝体","15"),accelerator="Ctrl+B",command=inversion)
base.bind_all("<Control-b>",inversion)
file_2.add_command(label='リセット',font=("明朝体","15"),accelerator="Ctrl+R",command=reset)
base.bind_all("<Control-r>",reset)

rad_v = tk.IntVar()
rad_v.set(1)

file_3 = tk.Menu(file_2,tearoff=0)
file_2.add_cascade(label='縦軸',font=("明朝体","15"),menu=file_3)
file_3.add_radiobutton(label=' a.u.',font=("明朝体","15"),value=1,variable=rad_v,command=lambda u_v="a.u.": unit_v(u_v))
file_3.add_radiobutton(label=' M/Ms',font=("明朝体","15"),value=2,variable=rad_v,command=lambda u_v="M/Ms": unit_v(u_v))
file_3.add_radiobutton(label=' V(V)',font=("明朝体","15"),value=3,variable=rad_v,command=lambda u_v="V(V)": unit_v(u_v))
file_3.add_radiobutton(label=' M(emu)',font=("明朝体","15"),value=4,variable=rad_v,command=lambda u_v="M(emu)": unit_v(u_v))
file_3.add_radiobutton(label=' °',font=("明朝体","15"),value=4,variable=rad_v,command=lambda u_v="°": unit_v(u_v))

rad_h = tk.IntVar()
rad_h.set(1)

file_4 = tk.Menu(file_2,tearoff=0)
file_2.add_cascade(label='横軸',font=("明朝体","15"),menu=file_4)
file_4.add_radiobutton(label=' V(V)',font=("明朝体","15"),value=1,variable=rad_h,command=lambda u_h="V(V)": unit_h(u_h))
file_4.add_radiobutton(label=' H(Oe)',font=("明朝体","15"),value=2,variable=rad_h,command=lambda u_h="H(Oe)": unit_h(u_h))
file_4.add_radiobutton(label=' H(mT)',font=("明朝体","15"),value=3,variable=rad_h,command=lambda u_h="H(mT)": unit_h(u_h))
file_4.add_radiobutton(label=' H(T)',font=("明朝体","15"),value=4,variable=rad_h,command=lambda u_h="H(T)": unit_h(u_h))

file_2.add_separator()
file_2.add_command(label='閉じる',font=("明朝体","15"),command=callback)

fonts = ("Times New Roman",15)

lab_file = tk.Label(text='ファイル名：',bg='pale green',font=("明朝体", "15", "bold"))
lab_file.place(x=1,y=1)

txt_file = tk.Entry(font=("明朝体", "15"),width=60)
txt_file.place(x=130,y=2,height=30)

lab_area_min = tk.Label(text='開始セル　：',bg='pale green',font=("明朝体", "15", "bold"))
lab_area_min.place(x=1,y=10+fix)

txt_area_min = tk.Entry(font=fonts,width=7)
txt_area_min_sell = tk.Entry(font=fonts,width=2)
txt_area_min_sell.insert(0,"B")
txt_area_min_sell.place(x=130,y=10+fix,height=30)
txt_area_min.insert(0,22)
txt_area_min.place(x=160,y=10+fix,height=30)

lab_num = tk.Label(text='データの個数：',bg='pale green',font=("明朝体", "15", "bold"))
lab_num.place(x=240,y=10+fix)

txt_num = tk.Entry(font=fonts,width=10)
txt_num.insert(0,30021)
txt_num.place(x=390,y=10+fix,height=30)

lab_max = tk.Label(text='最大値　　：',bg='pale green',font=("明朝体", "15", "bold"))
lab_max.place(x=1,y=10+fix*2)

txt_max = tk.Entry(font=fonts,width=10)
txt_max.insert(0,0)
txt_max.place(x=130,y=11+fix*2,height=30)

lab_min = tk.Label(text='最小値　　：',bg='pale green',font=("明朝体", "15", "bold"))
lab_min.place(x=1,y=10+fix*3)

txt_min = tk.Entry(font=fonts,width=10)
txt_min.insert(0,0)
txt_min.place(x=130,y=11+fix*3,height=30)

lab_max_ = tk.Label(text='最大平均範囲：',bg='pale green',font=("明朝体", "15", "bold"))
lab_max_.place(x=240,y=10+fix*2)

txt_max_ = tk.Entry(font=fonts,width=10)
txt_max_.insert(0,0)
txt_max_.place(x=390,y=11+fix*2,height=30)

lab_min_ = tk.Label(text='最小平均範囲：',bg='pale green',font=("明朝体", "15", "bold"))
lab_min_.place(x=240,y=10+fix*3)

txt_min_ = tk.Entry(font=fonts,width=10)
txt_min_.insert(0,0)
txt_min_.place(x=390,y=11+fix*3,height=30)

lab_cf_x = tk.Label(text='x係数：',bg='pale green',font=("明朝体", "15", "bold"))
lab_cf_x.place(x=510,y=10+fix)

txt_cf_x = tk.Entry(font=fonts,width=10)
txt_cf_x.insert(0,0)
txt_cf_x.place(x=585,y=10+fix,height=30)

lab_cf_y = tk.Label(text='y係数：',bg='pale green',font=("明朝体", "15", "bold"))
lab_cf_y.place(x=510,y=10+fix*2)

txt_cf_y = tk.Entry(font=fonts,width=10)
txt_cf_y.insert(0,0)
txt_cf_y.place(x=585,y=10+fix*2,height=30)

file_enter_button = tk.Button(
    base,text='決定',font=("明朝体","15","bold"),foreground='black',command=file_enter).place(x=585,y=11+fix*3,width=103,height=30)

initial_graph_button = tk.Button(
    base,text='初期データのプロット',font=("明朝体","10","bold"),foreground='black',command=initial_graph).place(x=5,y=(fix*5)-1,width=152,height=30)

justification_graph_button = tk.Button(
    base,text='原点揃えのプロット',font=("明朝体","10","bold"),foreground='black',command=justification_graph).place(x=162,y=(fix*5)-1,width=152,height=30)

result_graph_button = tk.Button(
    base,text='規格化プロット',font=("明朝体","10","bold"),foreground='black',command=result_graph).place(x=320,y=(fix*5)-1,width=152,height=30)

save_button = tk.Button(
    base,text='記録',font=("明朝体","10","bold"),foreground='black',command=save).place(x=655,y=(fix*5)-1,width=70,height=30)

spin_ = tk.StringVar()
spin_data = tk.Spinbox(
    base,state="readonly",textvariable=spin_,value=('選択','初期データ','原点揃え','規格化(V)','規格化(係数)'),font=("明朝体","10","bold"),command=change_data).place(x=500,y=(fix*5)-1,width=152,height=30)

file_select_name_button = tk.Button(
    base,text='ファイル一覧',font=("明朝体","10","bold"),foreground='black',command=file_list).place(x=820,y=(fix*5)-1,width=152,height=30)

fig_data = plt.figure()
fig_canvas = FigureCanvasTkAgg(fig_data,base)
fig_canvas.draw()
fig_canvas.get_tk_widget().place(x=5,y=35+fix*5,width=470,height=350)

plt.xlim(-5,5)
plt.ylim(-5,5)
plt.grid(True)
plt.xlabel("H(V)")
plt.ylabel("Kerr Signal(V)")
plt.scatter(0,0,s=plotsize,c="b",marker=".",alpha=0.5)


fig_save = plt.figure()
fig_canvas = FigureCanvasTkAgg(fig_save,base)
fig_canvas.draw()
fig_canvas.get_tk_widget().place(x=500,y=35+fix*5,width=470,height=350)

plt.xlim(-5,5)
plt.ylim(-5,5)
plt.grid(True)
plt.xlabel("H(V)")
plt.ylabel("Kerr Signal(V)")
plt.scatter(0,0,s=plotsize,c="b",marker=".",alpha=0.5)

base.mainloop()
