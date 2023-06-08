from tkinter import *

window = Tk()
window.title('simple-interest')
window.geometry("400x400")
window.configure(bg = 'white')

def calculateInterest():
    principal = float(prEntry.get())
    rate = float(rEntry.get())
    time = float(tEntry.get())

    i = (principal*rate*time)/100
    interest = round(i,2)

    message = Label(resultFrame, text = "Interest = " + interest, bg = 'grey', font = ("Calibri", 12), width = 55)
    message.place(x = 20, y = 40)
    message.pack()



headingLabel = Label(window, text = "Simple Interest Calculator", fg = 'black', bg = 'white', font = ('Calibri', 20), bd = 5)
headingLabel.place(x = 50, y = 10)

prLabel = Label(window, text = "Enter Principal:", fg = 'black', font = ('Calibri', 10), bd = 3)
prLabel.place(x = 20, y = 90)

prEntry = Entry(window, text = '', bd = 2, width = 27)
prEntry.place(x = 130, y = 93)

rLabel = Label(window, text = "Enter Rate per annum:", fg = 'black', font = ('Calibri', 10), bd = 3)
rLabel.place(x = 5, y = 130)

rEntry = Entry(window, text = '', bd = 2, width = 27)
rEntry.place(x = 150, y = 133)

tLabel = Label(window, text = "Enter Time:", fg = 'black', font = ('Calibri', 10), bd = 3)
tLabel.place(x = 20, y = 173)

tEntry = Entry(window, text = "", bd = 2, width = 27)
tEntry.place(x = 110, y = 176)

resultFrame = LabelFrame(window, text = "Result", bg = "grey", font = ("Calibri", 12))
resultFrame.pack(padx = 20, pady = 20)
resultFrame.place(x = 20, y = 250)

showResultLabel = Label(resultFrame, text = "Your result", bg = 'grey', font = ("Calibri", 12), width = 55)
showResultLabel.place(x = 20, y = 20)
showResultLabel.pack()

enter = Button(window, text = "Calculate", fg = 'black', bg = "#87a9d6", command = calculateInterest)
enter.place(x = 140, y = 210)

window.mainloop()