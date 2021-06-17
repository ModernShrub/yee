from tkinter import *

root=Tk()
root.title("Ascii")

root.geometry("400x400")
root.configure(background = 'white')

enter_word = Entry(root)
enter_word.place(relx=0.5,rely=0.4,anchor=CENTER)

label = Label(root, text = "Name in Ascii : ", bg="light yellow", fg="black")

label1 = Label(root, text = "Encrypted form : ", bg="yellow", fg="black")

def asciiConverter():
    input_word = enter_word.get()
    crypt = ""
    final = ""
    
    for letter in input_word :
        
        label["text"] += str(ord(letter)) + "  "
        crypt = int(ord(letter) - 1)
        label1['text'] += chr(crypt) + "  "
        
def clear():
  label['text'] = "Name in Ascii :  "
  label1['text'] = "Encrypted form :  "
  enter_word.delete(0, 'end')     
        


btn=Button(root,text="Show name in Ascii",command=asciiConverter, bg='gold', fg = 'black')
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

btnq=Button(root,text="Reset",command=clear, bg='gold', fg = 'black')
btnq.place(relx=0.5,rely=0.6,anchor=CENTER)

label.place(relx=0.5,rely=0.7,anchor=CENTER)

label1.place(relx=0.5,rely=0.8,anchor=CENTER)

root.mainloop()