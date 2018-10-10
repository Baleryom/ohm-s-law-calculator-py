from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('500x180')
root.title("Unit Converter Calculator")

formula1 = Label(root,text="Voltage(V) = Current(I) * Resistance(R)").grid(sticky=W)

messagebox.showinfo("Greetings","Please fill any 2 forms ")
lblVoltage = Label(root,text="Voltage(V)").grid(row=4,sticky=W)
lblCurrent = Label(root,text="Current(I)").grid(row=5,sticky=W)
lblResistance = Label(root,text="Resistance(R)").grid(row=6,sticky=W)
lblPower = Label(root,text="Power(P)").grid(row=7,sticky=W)

V = StringVar()
I = StringVar()
R = StringVar()
P = StringVar()


entryV = Entry(root,textvariable=V).grid(row=4,column=2)
testV = V.get()
#if not isinstance(testV,int):
 #       messagebox.showerror("Error!", "Please use integers only!")

entryI = Entry(root,textvariable=I).grid(row=5,column=2)
testI = I.get()
#if not isinstance(testI,int):
 #       messagebox.showerror("Error!","Please use integers only!")
entryR = Entry(root,textvariable=R).grid(row=6,column=2)
testR = R.get()
#if not isinstance(testR,int):
 #       messagebox.showerror("Error!","Please use integers only!")
entryP = Entry(root,textvariable=P).grid(row=7,column=2)
testP = P.get()
#if not isinstance(testP,int):
 #       messagebox.showerror("Error!","Please use integers only!")

Label(root,text="Volts").grid(column=4,row=4,sticky=W)
Label(root,text="Amps").grid(column=4,row=5,sticky=W)
Label(root,text="Ohms").grid(column=4,row=6,sticky=W)
Label(root,text="Watts").grid(column=4,row=7,sticky=W)

def Reset():
    V.set("")
    I.set("")
    R.set("")
    P.set("")

def Calculate():

    if len(R.get()) == 0 and len(P.get()) == 0:
        R.set(eval(str(eval(str(V.get())))+"/"+str(eval(str(I.get())))))
        P.set(eval(str(eval(str(V.get()))) + "*" + str(eval(str(I.get())))))

    if len(R.get()) == 0 and len(I.get()) == 0:
        R.set(eval(str(eval(str(V.get())))+"*"+str(V.get()) + "/" + str(eval(str(P.get())))))
        I.set(eval(str(eval(str(P.get()))) + "/" + str(eval(str(V.get())))))

    if len(I.get()) == 0 and len(P.get()) == 0:
        I.set(eval(str(eval(str(V.get()))) + "/" + str(eval(str(R.get())))))
        P.set(eval(str(eval(str(V.get())))+"*"+str(V.get()) + "/" + str(eval(str(R.get())))))

    if len(V.get()) == 0 and len(P.get()) == 0:
        V.set(eval(str(eval(str(I.get()))) + "*" + str(eval(str(R.get())))))
        P.set(eval(str(eval(str(I.get()))) + "*" + str(I.get()) + "*" + str(eval(str(R.get())))))

    if len(V.get()) == 0 and len(R.get()) == 0:
        V.set(eval(str(eval(str(P.get()))) + "/" + str(eval(str(I.get())))))
        R.set(eval(str(eval(str(I.get()))) + "*" + str(I.get()) + "/" + str(eval(str(P.get())))))

btn = Button(root,text="Calculate",command=Calculate).grid(row=9,column=2)
reset = Button(root,text="Reset",command=Reset).grid(row=9,sticky=W)

root.mainloop()