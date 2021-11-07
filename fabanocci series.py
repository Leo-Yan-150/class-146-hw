from tkinter import *

root=Tk()

root.title("Fibonacci")
root.geometry("1000x400")

label_series = Label(root, text="Fibonacci Series:")
label_sum = Label(root)
enter_number = Entry(root)

def Fib():
    innumber = int(enter_number.get())
    num = innumber
    
    fn = 0
    sn = 1
    sum = 0
    sum2 = 0
    counter = 1
    while (counter <= num):
        label_series["text"] += " " + str(sum)
        label_sum["text"] = "Sum: " + str(sum2)
        counter = counter + 1
        fn = sn
        sn = sum
        sum = fn + sn
        sum2 = sum2 + sum
        
    
btn = Button(root, text = "Show Fibonacci Series", command = Fib)

btn.pack()
label_series.pack()
enter_number.pack()
label_sum.pack()
root.mainloop()