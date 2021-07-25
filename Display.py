from tkinter import *
from tkinter import ttk
from tkinter import filedialog
global folder_path

newapp = Tk()

newapp.geometry("500x400")

newapp.title("registry")

linkfile = Entry(newapp, width=55)
linkfile.grid(row=0, column=0, padx = 10)

def browse_button():
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    linkfile.insert(0, filename)

folder_path = StringVar()

linkfile = Entry(newapp, width=55)
linkfile.grid(row=0, column=0, padx = 10)

Browser = Button(newapp, text="Browser...", command=browse_button, padx = 28)
Browser.grid(row=0, column=1, padx = 10)    
 
txt = Entry(newapp)
txt.grid(row=2, column=0, pady=10, ipady=30, ipadx=105)

GuiNoiDung = Button(newapp, text="Gui noi dung", padx = 20, pady = 28)
GuiNoiDung.grid(row=2, column=1, padx = 10)

frame = LabelFrame(newapp, text="Sua gia tri truc tiep")
frame.grid(row=3, columnspan = 4, padx = 0, pady = 0)

option = [
		"Get value",
		"Set value",
		"Delete value",
		"Create key",
		"Delete key"
]

option2 = [
		"String",
		"Binary",
		"DWORD",
		"QWORD",
		"Multi-string",
		"Expandable String"
]



def show(event):

	Val = LabelFrame(frame)

	Value2 = Entry(Val, width = 24)
	Value2.insert(0, "Name value")
	Value2.grid(row=0, column=0)

	Value3 = Entry(Val, width = 25)
	Value3.insert(0, "Value")
	Value3.grid(row=0, column=1)

	Value4 = ttk.Combobox(Val, value=option2)
	Value4.insert(0, "Kiểu dữ liệu")
	Value4.grid(row=0, column=2, padx=4)

	Val.grid(row=5, padx=0, pady=0)

	if SetValue.get() == "Get value":
		Value2.destroy()
		Value3.destroy()
		Value4.destroy()

		Value2 = Entry(frame, width = 24)
		Value2.insert(0, "Name value")
		Value2.grid(row=2, column=0, sticky = W)

	elif SetValue.get() == "Set value":
		Value2.destroy()
		Value3.destroy()
		Value4.destroy()

		ValueS2 = Entry(frame, width = 24)
		ValueS2.insert(0, "Name value")

		ValueS3 = Entry(frame, width = 25)
		ValueS3.insert(0, "Value")

		ValueS4 = ttk.Combobox(frame, value=option2)
		ValueS4.insert(0, "Kiểu dữ liệu")

		ValueS3.grid(row=2, column=0, sticky = N)
		ValueS4.grid(row=2, column=0, sticky = E, padx=4)
	elif SetValue.get() == "Delete value":
		Value3.destroy()
		Value4.destroy()
	elif SetValue.get() == "Create key":
		Value2.destroy()


SetValue = ttk.Combobox(frame, value=option)
SetValue.insert(0, "Chọn chức năng")
SetValue.bind("<<ComboboxSelected>>", show)
SetValue.grid(row=0,column=0,ipadx=160, sticky=W)

Value1 = Entry(frame, width=77)
Value1.insert(0, "Đường dẫn")
Value1.grid(row=1, column=0, pady=10)

txt = Entry(frame)
txt.grid(row=3, column=0, pady=10, ipady=30, ipadx=172)

Gui = Button(frame, text="xẻ")
Gui.grid(row=4, column=0, sticky=SW, ipadx = 30)

Xoa = Button(frame, text="mổ")
Xoa.grid(row=4, column=0, sticky=NE,ipadx = 30)

newapp.mainloop()