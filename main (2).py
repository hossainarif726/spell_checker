#!/usr/bin/env python
# coding: utf-8

# In[30]:


from tkinter import *
from spelling import *
from tkinter import messagebox
from dictionary import Dictionary


def spelling():
    a = SpellChecker("./words.txt")
    word = spell_check.get()
    d = str(a.check(word))
    dictionary = Dictionary(word)
    
    if word == "" or d is None:
        messagebox.showerror("Please enter a valid word")
        
    else:
        spelling.delete("1.0", "end")
        synonyms.delete("1.0", "end")
        antonyms.delete("1.0", "end")
        
        spelling.insert("end", d)
        s = dictionary.synonyms()
        synonyms.insert("end", s)
        a = dictionary.antonyms()
        antonyms.insert("end", a)
        
    
def refresh():
    spell_check.delete("0", "end")
    spelling.delete("1.0", "end")
    synonyms.delete("1.0", "end")
    antonyms.delete("1.0", "end")
    
    
window = Tk()
window.title("Spell checker")
window.geometry("880x600+170+0")
window.config(background="lightgreen")

text_heading = Label(window,text="Enter Word", font=("Arial",16, "bold"),bg="#98ff98")
text_heading.grid(row=0,column=1,padx=10, pady=10)

spell_check = Entry(window, width=22, bd="2", font="18", relief=RIDGE)
spell_check.grid(row=1,column=1,padx=10, pady=10)

check_button = Button(window, text="check",command=spelling,font=("Arial"))
check_button.grid(row=2,column=1)

f1 = Frame(window, bg="#98ff98")
f1.grid(row=7, column=1)

refresh_button = Button(f1, text="refresh",width=6, command=refresh, font=("Arial",15,"bold"))
refresh_button.pack(side= LEFT,padx=10, pady=20)

exit_button = Button(f1,text="exit", width=6, command=window.destroy, font=("Arial",15,"bold"))
exit_button.pack(side= LEFT,padx=10, pady=20)

lbl_spelling = Label(window, text="Correct Spelling", font=("Verdana", 13, "bold"), bg="#0e3a53",fg="white",width=12)
spelling = Text(window, width=70, height=4, relief=GROOVE,bd=4, font=("Arial",13),wrap=WORD)

lbl_syn = Label(window, text="Synonyms", font=("Verdana", 13, "bold"), bg="#0e3a53",fg="white",width=12)
synonyms = Text(window, width=70, height=4, relief=GROOVE,bd=4, font=("Arial",13),wrap=WORD)

lbl_ant = Label(window, text="Antonyms", font=("Verdana", 13, "bold"), bg="#0e3a53",fg="white",width=12)
antonyms = Text(window, width=70, height=4, relief=GROOVE,bd=4, font=("Arial",13),wrap=WORD)

lbl_spelling.grid(row=3,column=0,padx=10,pady=10)
spelling.grid(row=3,column=1,padx=10,pady=10)
lbl_syn.grid(row=4,column=0,padx=10,pady=10)
synonyms.grid(row=4,column=1,padx=10,pady=10)
lbl_ant.grid(row=5,column=0,padx=10,pady=10)
antonyms.grid(row=5,column=1,padx=10,pady=10)




window.mainloop()


# In[ ]:




