
from tkinter import *
from tkinter import filedialog
import subprocess
import tkinter.messagebox
import os

main=Tk()
main.title('Exe Generator')
main.geometry('200x150')
filecheck=BooleanVar()
consolecheck=BooleanVar()
iconcheck=BooleanVar()
global out_PATH,out_File,out_Console,out_pathtoicon,out_checkicon
out_PATH,out_File,out_Console,out_pathtoicon,out_checkicon='please insert path to py file','--onefile','--console','please insert path to icon file',0
def browsefile():
	global out_PATH
	pyPATH=filedialog.askopenfilename(title='Select a Py file',filetypes=(('Py files','*.py'),('All files','*.*')))
	PATH='"'+pyPATH+'"'
	out_PATH=PATH
def filechecker():
	global out_File
	if filecheck.get()==True:
		File='--onedir'
		out_File=File
	elif filecheck.get()==False:
		File='--onefile'
		out_File=File
def consolechecker():
	global out_Console
	if consolecheck.get()==True:
		Console='--windowed'
		out_Console=Console
	elif consolecheck.get()==False:
		Console='--console'
		out_Console=Console
def iconchecker():
	global out_pathtoico,out_checkicon,icobut
	def chooseicon():
		global out_pathtoicon
		iconfile=filedialog.askopenfilename(title='Select a icon file',filetypes=(('Ico files','*.ico'),('All files','*.*')))
		pathtoicon='"'+iconfile+'"'
		out_pathtoicon=pathtoicon
	if iconcheck.get()==True:
		icobut.destroy()
		checkicon=0
		out_checkicon=checkicon
	elif iconcheck.get()==False:
		icobut=Button(main,text='Choose icon',command=chooseicon)
		icobut.place(x=80,y=89)
		checkicon=1
		out_checkicon=checkicon
def final():
	if out_PATH=='please insert path to py file':
		tkinter.messagebox.showinfo('Insert path to python file',message='Please insert path to python file')
	
	else:
		direct=filedialog.askdirectory(title='Choose an output folder')
		Fdirect='cd '+direct
		mess='Output file in '+direct
		if out_checkicon==1:
			if out_pathtoicon=='please insert path to icon file':
				tkinter.messagebox.showinfo('Insert path to icon file',message='Please insert path to icon file')
			else:
				def haveicon():
					cm='pyinstaller '+out_File+' '+out_Console+' '+'--icon'+' '+out_pathtoicon+' '+out_PATH
					print('scrip:',cm)
					Adirect=Fdirect+'&'+cm
					os.system(Adirect)
					tkinter.messagebox.showinfo('Convert done',message=mess)
				haveicon()
		elif out_checkicon==0:
			def donthaveicon():
				cm='pyinstaller '+out_File+' '+out_Console+' '+out_PATH
				print('scrip:',cm)
				Adirect=Fdirect+'&'+cm
				os.system(Adirect)
				tkinter.messagebox.showinfo('Convert done',message=mess)
			donthaveicon()	
Checkbutton(main,text='One File',variable=filecheck,onvalue=False,offvalue=True,command=filechecker).place(x=20,y=47)
Checkbutton(main,text='Console',variable=consolecheck,onvalue=False,offvalue=True,command=consolechecker).place(x=20,y=68)
ico=Checkbutton(main,text='Icon',variable=iconcheck,onvalue=False,offvalue=True,command=iconchecker)
ico.place(x=20,y=89)
ico.deselect()
Button(main,text='Browse',command=lambda: browsefile()).place(x=20,y=25)
Label(main,text='Path to py file').place(x=20,y=4)
Button(main,text='Create!',command=final).place(x=20,y=120)
Button(main,text='Install Pyinstaller',command=lambda: os.system('pip install pyinstaller')).place(x=80,y=120)
main.mainloop()

