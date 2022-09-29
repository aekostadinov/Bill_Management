from tkinter import *

root = Tk()
root.geometry("1000x500")
root.title("Bill Management")
root.resizable(False,False)

def Reset():
    entry_coca_cola.delete(0,END)
    entry_pizza.delete(0, END)
    entry_whiskey.delete(0, END)
    entry_draft_beer.delete(0, END)
    entry_pork_ribs.delete(0, END)
def Total():
    try: num_1 = int(Coca_cola.get())
    except: num_1 = 0

    try: num_2 = int(Pizza.get())
    except: num_2 = 0

    try: num_3 = int(Pork_Ribs.get())
    except: num_3 = 0

    try: num_4 = int(Whiskey.get())
    except: num_4 = 0

    try: num_5 = int(Draft_Beer.get())
    except: num_5 = 0

    cola_total_price = num_1 * 1
    pizza_total_price = num_2 * 12
    pork_ribs_total_price = num_3 * 15
    whiskey_total_price = num_4 * 10
    draft_beer_total_price = num_5 * 2.5

    Total_label = Label(bill_frame,font=("arial",20,"bold"),text='Total', width=20, bg='black',fg='white')
    Total_label.place(x=10, y=70)

    entry_total = Entry(bill_frame,font=("arial",20,"bold"),textvariable= Total_bill, bd=6,width=15,bg='cyan')
    entry_total.place(x=20,y=100)

    total_price = cola_total_price + pizza_total_price + pork_ribs_total_price + whiskey_total_price + draft_beer_total_price
    string_bill = str(total_price)
    Total_bill.set(string_bill)

### MENU ###
frame = Frame(root, bg='cyan', highlightbackground="black", highlightthickness=3, width=300, height=410)
frame.place(x=5, y=80)

Label(frame, text="Menu", font=("normal", 40, "bold"), fg="black", bg='cyan').place(x=80, y=0)
Label(frame, font=("Lucida Calligraphy", 15, "bold"), text="Coca Cola -------------- 1.00$/1pc", fg="black",bg='cyan').place(x=10, y=80)
Label(frame, font=("Lucida Calligraphy", 15, "bold"), text="Draft Beer ----------- 2.50$/500ml", fg="black",bg='cyan').place(x=10, y=110)
Label(frame, font=("Lucida Calligraphy", 15, "bold"), text="Whiskey -------------- 10.00$/50ml", fg="black",bg='cyan').place(x=10, y=140)
Label(frame, font=("Lucida Calligraphy", 15, "bold"), text="Pizza ------------- 12.00$/big one", fg="black",bg='cyan').place(x=10, y=170)
Label(frame, font=("Lucida Calligraphy", 15, "bold"), text="Pork Ribs ------------ 15.00$/400g", fg="black",bg='cyan').place(x=10, y=200)

### ENTRY TABLE ###
entry_frame = Frame(root,bd=5,height=300,width=50,bg="cyan")
entry_frame.pack()

Coca_cola = StringVar()
Draft_Beer = StringVar()
Whiskey = StringVar()
Pizza = StringVar()
Pork_Ribs = StringVar()
Total_bill = StringVar()

### BILL ###

bill_frame = Frame(root,bg='cyan',width=300,height=410,highlightthickness=3,highlightbackground='black')
bill_frame.place(x=690,y=80)

Bill = Label(bill_frame,text='Bill',font=("arial",40,"bold"),bg='cyan')
Bill.place(x=100,y=10)

### Label's of entry table ###
Coca_cola_label = Label(entry_frame, font=("arial", 20, 'bold'),bg='cyan', text="Coca Cola", width=12, fg='blue4')
Draft_beer_label = Label(entry_frame, font=("arial", 20, 'bold'),bg='cyan', text="Draft beer", width=12,fg='blue4')
Whiskey_label = Label(entry_frame, font=("arial", 20, 'bold'),bg='cyan', text="Whiskey", width=12, fg='blue4')
Pizza_label = Label(entry_frame, font=("arial", 20, 'bold'),bg='cyan', text="Pizza", width=12, fg='blue4')
Pork_ribs_label = Label(entry_frame, font=("arial", 20, 'bold'),bg='cyan', text="Pork ribs", width=12, fg='blue4')
Coca_cola_label.grid(row=4, column=0)
Draft_beer_label.grid(row=5, column=0)
Whiskey_label.grid(row=6, column=0)
Pizza_label.grid(row=7, column=0)
Pork_ribs_label.grid(row=8, column=0)

### Entry ###
entry_coca_cola = Entry(entry_frame,font=("arial",20,"bold"),textvariable=Coca_cola,bd=6,width=8,bg='white')
entry_draft_beer = Entry(entry_frame,font=("arial",20,"bold"),textvariable=Draft_Beer,bd=6,width=8,bg='white')
entry_whiskey = Entry(entry_frame,font=("arial",20,"bold"),textvariable=Whiskey,bd=6,width=8,bg='white')
entry_pizza = Entry(entry_frame,font=("arial",20,"bold"),textvariable=Pizza,bd=6,width=8,bg='white')
entry_pork_ribs = Entry(entry_frame,font=("arial",20,"bold"),textvariable=Pork_Ribs,bd=6,width=8,bg='white')
entry_coca_cola.grid(row=4,column=1)
entry_draft_beer.grid(row=5,column=1)
entry_whiskey.grid(row=6,column=1)
entry_pizza.grid(row=7,column=1)
entry_pork_ribs.grid(row=8,column=1)

### buttons ###

btn_resset = Button(entry_frame,text='Reset',bg='cyan',fg='black',font=("arial",20,'bold'),command=Reset,bd=5)
btn_resset.grid(row=9,column=0)

btn_total_bill = Button(entry_frame,text='Total Bill:',bg='cyan',fg='black',font=("arial",20,'bold'),command=Total,bd=5)
btn_total_bill.grid(row=9,column=1)


root.mainloop()