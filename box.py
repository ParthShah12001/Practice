try:
    import tkinter
except ImportError:
    import Tkinter as tkinter
import os
mainWindow = tkinter.Tk()
mainWindow.geometry('640x480-8-200')
label = tkinter.Label(mainWindow,text = "Tkinter gird demo")
label.grid(row =0 ,column = 0,columnspan=3)
mainWindow.columnconfigure(0,weight=1)
mainWindow.columnconfigure(1,weight=1)
mainWindow.columnconfigure(2,weight=3)
mainWindow.columnconfigure(3,weight=3)
mainWindow.columnconfigure(4,weight=3)
mainWindow.rowconfigure(0,weight=1)
mainWindow.rowconfigure(1,weight=10)
mainWindow.rowconfigure(2,weight=1)
mainWindow.rowconfigure(3,weight=3)
mainWindow.rowconfigure(4,weight=3)

fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1,column=0,rowspan=2,sticky='ns')
fileList.config(border=1,relief ="sunken")
for zone in os.listdir('/Windows/System32'):
    fileList.insert(tkinter.END,zone)

listscroll = tkinter.Scrollbar(mainWindow,orient=tkinter.VERTICAL,command=fileList.yview)
listscroll.grid(row=1,column=1,rowspan=2,sticky='nsw')
fileList['yscrollcommand']=listscroll.set

optionFram = tkinter.LabelFrame(mainWindow,text="File Details")
optionFram.grid(row=1,column=2,sticky="ne")

 
rbValue =tkinter.IntVar()
rbValue.set(3)
radio1 = tkinter.Radiobutton(optionFram,text="Filename", value=1 ,variable=rbValue)
radio2 = tkinter.Radiobutton(optionFram,text="Path", value=2 ,variable=rbValue)
radio3 = tkinter.Radiobutton(optionFram,text="Data", value=3 ,variable=rbValue)
radio1.grid(row=0,column=0,sticky="w")
radio2.grid(row=1,column=0,sticky="w")
radio3.grid(row=2,column=0,sticky="w")

resultLabel = tkinter.Label(mainWindow,text = "Result")
resultLabel.grid(row=2,column=2,sticky="nw")
result=tkinter.Entry(mainWindow)
result.grid(row=2,column=2,sticky='sw')

timeFrame=tkinter.LabelFrame(mainWindow,text="Time")
timeFrame.grid(row=3,column=0,sticky="new")

hourSpin=tkinter.Spinbox(timeFrame,width=2,value=tuple(range(1,24)))
minuteSpin=tkinter.Spinbox(timeFrame,width=2,from_=0, to=59)
secondSpin=tkinter.Spinbox(timeFrame,width=2,from_=0, to=59)
hourSpin.grid(row=0,column=0)
tkinter.Label(timeFrame,text=":").grid(row=0,column=1)
minuteSpin.grid(row=0,column=2)
tkinter.Label(timeFrame,text=":").grid(row=0,column=3)
secondSpin.grid(row=0,column=4)
timeFrame['padx']=36


dateFrame=tkinter.Frame(mainWindow)
dateFrame.grid(row=4,column=0,sticky="new")
dayLabel = tkinter.Label(dateFrame,text="Day")
monthLabel = tkinter.Label(dateFrame,text="Month")
yearLabel = tkinter.Label(dateFrame,text="Year")
dayLabel.grid(row=0,column=0,sticky='w')
monthLabel.grid(row=0,column=1,sticky='w')
yearLabel.grid(row=0,column=2,sticky='w')

day=tkinter.Spinbox(dateFrame,width=5,from_=1,to=31)
month = tkinter.Spinbox(dateFrame,width=5,values=("jan","feb","mar","april","May","jun","jul","aug","sep","oct","nov","dec"))
year = tkinter.Spinbox(dateFrame,width=5,from_=2000 ,to=2009)
day.grid(row=1,column=0)
month.grid(row=1,column=1)
year.grid(row=1,column=2)
dateFrame['padx']=35


okButton = tkinter.Button(mainWindow,text="ok")
cancleButton = tkinter.Button(mainWindow,text="Cancle",command=mainWindow.quit)
okButton.grid(row=4,column=3,sticky='e')
cancleButton.grid(row=4,column=4,sticky='w')



mainWindow.mainloop()










