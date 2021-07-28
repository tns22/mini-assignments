import tkinter
window = tkinter.Tk()

height = tkinter.StringVar()
weight = tkinter.StringVar()
output = tkinter.StringVar()

tkinter.Label(window, text='Height: ').grid(sticky=tkinter.E)
tkinter.Label(window, text='Weight: ').grid(sticky=tkinter.E)
heightEntry = tkinter.Entry(window, textvariable=height)
weightEntry = tkinter.Entry(window, textvariable=weight)
outputLabel = tkinter.Label(window, textvariable=output)

window.mainloop()
def calculateClick():
    print(int(703 * float(height) / float(weight)^2))
heightEntry.grid(row=0, column=1)
weightEntry.grid(row=1, column =1)
outputLabel.grid(row=0, column=2, rowspan=2)
calculatebutton= tkinter.Button(window, text='Calculate BMI', command=calculateClick)
calculatebutton.grid(row=3, column=0, columnspan=3, sticky= tkitner.N + tkinter.E + tkinter.S + tkinter.W)
