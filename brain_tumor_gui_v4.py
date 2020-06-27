import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import tkinter.font as font
from PIL import ImageTk, Image
import threshold_inline as th
import Normalize_Copy as norm
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar2Tk
from matplotlib.figure import Figure
from csv import reader
import random
from skillstriping import skill_image,ShowImage
from FileDirectory import path_finder
import tkinter.messagebox

root = tk.Tk()
root.title('Brain Tumor Classification')
root.geometry("1100x650")
filename=""

labelFrame = tk.LabelFrame(root,text = "Open a file", width=500, height=50, bd=5)
labelFrame.place(x=70,y=10)

option_frame = tk.LabelFrame(root, text="Options", width=300, height=400, bd=5)
option_frame.place(x=350,y=10)

preprocess_image_frame = tk.LabelFrame(root, text="Preprocess Image", width=810, height=250, bd=5)
preprocess_image_frame.place(x=700, y=10)

original_image_frame = tk.LabelFrame(root, text="Original Image", width=300, height=300, bd=5)
original_image_frame.place(x=10, y=110)

normalize_image_frame = tk.LabelFrame(root, text="Normalize Image", width=810, height=250, bd=5)
normalize_image_frame.place(x=700, y=270)

text_csv_frame = tk.LabelFrame(root, text="SVM_MAX", width=80, height=80, bd=5)
text_csv_frame.place(x=660, y=620)

parent_label_frame = tk.LabelFrame(root, text="Classify", width=100, height=80, bd=5)
parent_label_frame.place(x=660, y=720)

classify_image_frame = tk.LabelFrame(root, text="Classify Image", width=740, height=250, bd=5)
classify_image_frame.place(x=770, y=530)

graph_frame = tk.LabelFrame(root, text="Graph", width=640, height=360, bd=5)
graph_frame.place(x=10, y=420)


def fileDialog():
    global filename
    filename = filedialog.askopenfilename(initialdir = "D:study material\\Python\\prog\\Projects\\brain_tumour",title = "Select A File",filetype = (("jpeg", "*.jpg"), ("png","*.png"), ("All Files","*.*")))
    print(filename)
    original_image = ImageTk.PhotoImage((Image.open(filename)).resize((280, 270), Image.ANTIALIAS));
    original_image_label = tk.Label(original_image_frame, image=original_image)
    original_image_label.image = original_image
    original_image_label.place(x=0, y=0)


def preprocess_function():
    global filename
    image1 = th.img_thresh(filename)
    preprocess_image_1 = ImageTk.PhotoImage(image=Image.fromarray(image1))
    preprocess_image_1_label = tk.Label(preprocess_image_frame, image=preprocess_image_1)
    preprocess_image_1_label.image = preprocess_image_1
    preprocess_image_1_label.place(x=30, y=0)
    text1 = tk.Text(preprocess_image_frame, height=1, width=15)
    text1.place(x = 150,y=205)
    text1.insert(tk.END, "Threshold image")
    text1.tag_add("color", "1.0", "14.9")
    text1.tag_configure('color',background="black", foreground="white")
    

    image2 = skill_image(filename)
    preprocess_image_2 = ImageTk.PhotoImage(image=Image.fromarray(image2))
    preprocess_image_2_label = tk.Label(preprocess_image_frame, image=preprocess_image_2)
    preprocess_image_2_label.image = preprocess_image_2
    preprocess_image_2_label.place(x=430, y=0)

    text2= tk.Text(preprocess_image_frame, height=1, width=18)
    text2.place(x = 550,y=205)
    text2.insert(tk.END, "Cleared Pixel")
    text2.tag_add("color", "1.0", "14.9")
    text2.tag_configure('color',background="black", foreground="white")

   
def normalize_function():
    global filename
    img = norm.normalize(filename)
    normalize_image1 = ImageTk.PhotoImage(image=Image.fromarray(img))
    normalize_image_1_label = tk.Label(normalize_image_frame, image=normalize_image1)
    normalize_image_1_label.image = normalize_image1
    normalize_image_1_label.place(x=30, y=0)

    text1 = tk.Text(normalize_image_frame, height=1, width=16)
    text1.place(x = 150,y=205)
    text1.insert(tk.END, "Normalized image")
    text1.tag_add("color", "1.0", "14.9")
    text1.tag_configure('color',background="black", foreground="white")

##    global filename
##    normalize_image1 = norm.normalize(filename)
##    normalize_image1 = ImageTk.PhotoImage(image=Image.fromarray(normalize_image1))
##    normalize_image_1_label = tk.Label(normalize_image_frame, image=normalize_image1)
##    normalize_image_1_label.image = normalize_image1
##    normalize_image_1_label.place(x=430, y=0)

##    text2= tk.Text(normalize_image_frame, height=1, width=18)
##    text2.place(x = 550,y=205)
##    text2.insert(tk.END, "Classified image 2")
##    text2.tag_add("color", "1.0", "14.9")
##    text2.tag_configure('color',background="black", foreground="white")
    

def classify_function():

    global filename
    
    for widget in text_csv_frame.winfo_children():
       widget.destroy()

    filename1 = filedialog.askopenfilename(initialdir = "D:study material\\Python\\prog\\Projects\\brain_tumour",title = "Select Image 1",filetype = (("jpeg", "*.jpg"), ("png","*.png"), ("All Files","*.*")))
    classify_image_1 = ImageTk.PhotoImage((Image.open(filename1)).resize((350, 215), Image.ANTIALIAS));
    classify_image_1_label = tk.Label(classify_image_frame, image=classify_image_1)
    classify_image_1_label.image = classify_image_1
    classify_image_1_label.place(x=30, y=0)

    text1 = tk.Text(classify_image_frame, height=1, width=18)
    text1.place(x = 150,y=205)
    text1.insert(tk.END, "Classified image 1")
    text1.tag_add("color", "1.0", "14.9")
    text1.tag_configure('color',background="black", foreground="white")

    filename2 = filedialog.askopenfilename(initialdir = "D:study material\\Python\\prog\\Projects\\brain_tumour",title = "Select Image 2",filetype = (("jpeg", "*.jpg"), ("png","*.png"), ("All Files","*.*")))
    classify_image_2 = ImageTk.PhotoImage((Image.open(filename2)).resize((350, 215), Image.ANTIALIAS));
    classify_image_2_label = tk.Label(classify_image_frame, image=classify_image_2)
    classify_image_2_label.image = classify_image_2
    classify_image_2_label.place(x=370, y=0)

    text2 = tk.Text(classify_image_frame, height=1, width=18)
    text2.place(x = 550,y=205)
    text2.insert(tk.END, "Classified image 2")
    text2.tag_add("color", "1.0", "14.9")
    text2.tag_configure('color',background="black", foreground="white")

    with open('SVM.csv','r') as svm_data:
        csv_reader = reader(svm_data)
        list_of_rows = list(csv_reader)
    

    y_axis = []
    x_axis = []
    xmax,ymax=(0,float(list_of_rows[1][0]))
    for i in range(1,len(list_of_rows)):
        x_axis.append(i)
        data = float(list_of_rows[i][0])
        y_axis.append(data)
        if data>ymax:
            xmax=i
            ymax=data
            
    max_val_label = tk.Label(text_csv_frame, text=str(ymax),padx=10,font=('times', 15, 'bold'))
    max_val_label.pack()

    parent_name = path_finder(filename)
    if parent_name==-1:
        tkinter.messagebox.showinfo("ERROR!!","Path Specified is not found")
        parent_label = tk.Label(parent_label_frame, text="ERROR!!",padx=5,font=('times', 12, 'bold'))
    else:
        parent_label = tk.Label(parent_label_frame, text=parent_name,padx=5,font=('times', 12, 'bold'))
    parent_label.pack()
   

def graph_function():

    with open('SVM.csv','r') as svm_data:
        csv_reader = reader(svm_data)
        list_of_rows = list(csv_reader)

    

    y_axis1 = []
    y_axis2 = []
    y_axis3 = []
    y_axis = []
    x_axis = []
    xmax,ymax=[0,0,0],[float(list_of_rows[1][0]),float(list_of_rows[1][1]),float(list_of_rows[1][2])]
    for i in range(2,len(list_of_rows)):
        x_axis.append(i)
        data = [float(x) for x in list_of_rows[i]]
        y_axis.append(data)
        if data[0]>ymax[0]:
            xmax[0]=i
            ymax[0]=data[0]
        if data[1]>ymax[1]:
            xmax[1]=i
            ymax[1]=data[1]
        if data[2]>ymax[2]:
            xmax[2]=i
            ymax[2]=data[2]

    for i in y_axis:
        y_axis1.append(i[0])
        y_axis2.append(i[1])
        y_axis3.append(i[2])

    fig = Figure(figsize=(9, 5), dpi=70)
    ax = fig.add_subplot(111)
    line,=ax.plot(x_axis,y_axis1)
    line,=ax.plot(x_axis,y_axis2)
    line,=ax.plot(x_axis,y_axis3)
    ax.legend(['SVM','COL1','COL2'],loc="lower right")
    fig.text(0.5, 0.04, 'Index', ha='center', va='center')
    fig.text(0.06, 0.5, 'SVM Values', ha='center', va='center', rotation='vertical')
    fig.text(0.5,0.95 , 'SVM', ha='center', va='top')
    ax.annotate('('+str(xmax[0])+','+str(ymax[0])+')', xy=(xmax[0], ymax[0]), xytext=(xmax[0], ymax[0]+5),arrowprops=dict(facecolor='green', shrink=0.005))
    ax.annotate('('+str(xmax[1])+','+str(ymax[1])+')', xy=(xmax[1], ymax[1]), xytext=(xmax[1], ymax[1]+5),arrowprops=dict(facecolor='red', shrink=0.005))
    ax.annotate('('+str(xmax[2])+','+str(ymax[2])+')', xy=(xmax[2], ymax[2]), xytext=(xmax[2], ymax[2]+5),arrowprops=dict(facecolor='blue', shrink=0.005))
    
    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP,expand=1)

def quit_function():
    root.destroy()

def reset_function():
    for widget in original_image_frame.winfo_children():
       widget.destroy()
    for widget in preprocess_image_frame.winfo_children():
       widget.destroy()
    for widget in normalize_image_frame.winfo_children():
       widget.destroy()
    for widget in classify_image_frame.winfo_children():
       widget.destroy()
    for widget in text_csv_frame.winfo_children():
       widget.destroy()
    for widget in parent_label_frame.winfo_children():
       widget.destroy()
    for widget in graph_frame.winfo_children():
       widget.destroy()

    
myFont = font.Font(family='Helvetica', size=15, weight='bold')
browse_font = font.Font(family='Helvetica', size=15)

button = tk.Button(labelFrame,text = "Browse a file",command = fileDialog,font = browse_font,bg='#0052cc', fg='#ffffff')
button.grid(column = 0,row = 1,ipady=5, ipadx=5,padx=4,pady=4)

preprocess_button = tk.Button(option_frame,text = "Preprocess Image",command = preprocess_function,font = myFont,bg='#0052cc', fg='#ffffff')
preprocess_button.place(x = 20,y=10,width = 250,height = 40)

normalize_button = tk.Button(option_frame,text = "Normalize Image",command = normalize_function,font = myFont,bg='#0052cc', fg='#ffffff')
normalize_button.place(x = 20,y=70,width = 250,height = 40)

classify_button = tk.Button(option_frame,text = "Classify Image",command = classify_function,font = myFont,bg='#0052cc', fg='#ffffff')
classify_button.place(x = 40,y=130,width = 200,height = 40)

graph_button = tk.Button(option_frame,text = "Graph",command = graph_function,font = myFont,bg='#0052cc', fg='#ffffff')
graph_button.place(x = 40,y=190,width = 200,height = 40)

reset_button = tk.Button(option_frame,text = "Reset",command = lambda root=root:reset_function(),font = myFont,bg='#0052cc', fg='#ffffff')
reset_button.place(x = 40,y=250,width = 200,height = 40)

exit_button = tk.Button(option_frame,text = "Exit",command = lambda root=root:quit_function(),font = myFont,bg='#0052cc', fg='#ffffff')
exit_button.place(x = 40,y=310,width = 200,height = 40)


root.mainloop()
