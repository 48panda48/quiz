from tkinter import *
master = Tk()
var1 = IntVar()
Checkbutton(master, text="Do Questions in Order", variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text="Repeat wrong questions", variable=var2).grid(row=1, sticky=W)
e = Entry(master,width=6)
Label(master, text="Time(secs):").grid(row=0,column=1)
e.grid(row=0,column=2)

e.delete(0, END)
e.insert(0, "Infinite")
e2 = Entry(master)
e2.grid(row=1,column=1,columnspan=3)
e2.delete(0, END)
e2.insert(0, "Filename.qz")
t = Text(master, height=20, width=40)
t.grid(column=4,row=1,rowspan=2,sticky=W+E+N+S)
t2 = Text(master, height=20, width=40)
t2.grid(column=5,row=1,rowspan=2,sticky=W+N+S+E)
master.columnconfigure(4,weight=1)
master.columnconfigure(5,weight=1)
master.rowconfigure(2,weight=1)
Label(master, text="Questions").grid(row=0,column=4,sticky=E)
Label(master, text="Anwsers").grid(row=0,column=5,sticky=W)

def compileQuiz():
    text=""
    if var1.get()==1 or var2.get()==1 or e.get()!="Infinite":
        count=0
        if var1.get()==1:
            count+=1
        if var2.get()==1:
            count+=1
        if e.get()!="Infinite":
            count+=1
        text+=["","1 option\n","2 options\n","3 options\n"][count]
        if var1.get()==1:
            text+="in order\n"
        if var2.get()==1:
            text+="repeat wrong at end\n"
        if e.get()!="Infinite":
            try:
                text+=f"timed {int(e.get())}\n"
            except ValueError:
                class CompilationError(Exception):
                    pass
                raise CompilationError("please input a number...")
    for q,a in zip(t.get(1.0,END).splitlines(),t2.get(1.0,END).splitlines()):
        text += q.replace("\t"," ")+"\t"+a.replace("\t"," ")+"\n"
    with open(e2.get(),"w+") as f:
        f.write(text)
    print("DONE")
b=Button(master,text="Compile",command=compileQuiz)
b.grid(column=3,row=0)
def loop():
    t.tag_configure("right", justify='right')
    t.tag_add("right", 1.0, "end")
    master.after(10,loop)
master.after(100,loop)
mainloop()
