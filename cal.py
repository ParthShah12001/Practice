try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

keys=[[('C',1),('CE',1)],
      [('7'), ]]
mainWindow = tkinter.Tk()
mainWindow.geometry('480x480-8-200')
mainWindow['padx']=10
pri=tkinter.Entry(mainWindow,width=40)
pri.grid(row=0,column=0)




mainWindow.mainloop()