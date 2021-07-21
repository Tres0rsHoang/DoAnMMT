from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

app = Tk()
app.configure(bg='Black')

app.title("My window, made with python")
img = PhotoImage(file='icon.ico')
app.tk.call('wm', 'iconphoto', app._w, img)
app.geometry("600x400")

name = Entry(app, width=50, bg="blue", fg="black",borderwidth=3)
name.grid(row=1,column=0) #Khong de chung hang voi Entry

def BamVaoNut():
	Ten = Label(app, text=name.get()).grid(row=2,column=0)
def popup():
	#showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
	CauTraLoi = messagebox.showwarning("Day la cai pop-up", "hahaha")
	print(CauTraLoi)
def File():
	app.filename=filedialog.askopenfilename(initialdir="D:\\", title="Chon 1 file di nao", filetypes=(("png file","*.png"),("all file","*.*")))
	TenFile = Label(app,text=app.filename).grid(row=2,column=0)
def Them():
	name.insert(0,"hihi ")

string = Label(app, text="Hihi", fg="#363636").grid(row=0, column=0, padx=10, pady=10)
CaiNut = Button(app, text="Bam vao em di", padx=0, pady=0, command=BamVaoNut, fg="red", bg="yellow").grid(row=10,column=10)
CaiNutTat = Button(app, text="Bam la tat",padx=0,pady=0,command=app.quit).grid(row=11,column=10)
CaiNutBatPopUp = Button(app,text="Bam de bat cai Pop up", padx=0,pady=0,command=popup).grid(row=12,column=10)
CaiNutChonFile = Button(app,text="Bam de chon file", padx=0,pady=0,command=File).grid(row=13,column=10)
ThemChu = Button(app,text="Bam de them chu 'hihi' ", command=Them).grid(row=14,column=10)
app.mainloop()
