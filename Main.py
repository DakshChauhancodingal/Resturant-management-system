import  tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.title("Restaurant system ")
root.geometry("600x550")
menu={"Pizza":3,"fries":2,"cold drink":4,"hot dog":2}
quantites={}
tk.Label(root,text="Restaurant system",font=("Arial",18,"bold")).pack(pady=15)
for item,price in menu.items():
    frame=tk.Frame(root)
    frame.pack(pady=15)
    tk.Label(frame,text=f"{item}-$(price)",width=20,anchor="w").pack(side="left")
    entry=tk.Entry(frame,width=5)
    entry.pack(side="left")
    quantites[item]=entry
def place_order():
    total=0
    summary="Order summary:\n\n"
    for item,entry in quantites.items():
        if entry.get().isdigit():
            quantity=int(entry.get())
            cost=quantity*menu[item]
            total +=cost
            if quantity > 0:
                summary+= f"{item}:{quantity}x ${menu[item]}=${cost}\n"
    if total >0:
        summary+=f"\nTotal Cost: ${total}"
        messagebox.showinfo("Order Placed",summary)
    else:
        messagebox.showerror("Error,Please order at least one item")
tk.Button(root,text="Place order",command=place_order,font=("Arial",12,"bold")).pack(pady=20)
root.mainloop()