# import tkinter

# window = tkinter.Tk()
# window.geometry("900x800")
# window.title("Translator")
# window.config(bg="#4682B4")

# window.mainloop()

#2
import tkinter
import turtle
window = tkinter.Tk()
window.geometry("900x800")
window.title("Translator")
window.config(bg="#4682B4")

a=tkinter.Label(
    window,
    text='eren niger',
    font=('algarian',15),
    bg='white',
)
a.pack(pady=50)

translator_lbl=tkinter.Label(text='translate',bg='#4682B4',fg='white',font=('Algerian',20))
translator_lbl.place(x=70,y=80)

translator_entry=tkinter.Entry(font=('Algerian',20),bg='white',fg='#4682B4')
translator_entry.place(x=250,y=80)


translator_lbl=tkinter.Label(text='perevod',bg='#4682B4',fg='white',font=('Aalgerian',20))
translator_lbl.place(x=110,y=150)

one_ent=tkinter.Entry(
    font=('Algerian',20)
)
one_ent.place(x=250,y=150)

one_btn=tkinter.Button(
    text='перевести',
    font=('Batang',10),
    bg='red',
    fg='white',
   
)
one_btn.place(x=120,y=200)

one_ent=tkinter.Entry(font=('Algerian',20))
one_ent.place(x=250,y=250)


window.mainloop()


