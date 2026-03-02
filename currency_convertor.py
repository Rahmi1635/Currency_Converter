

import requests
from tkinter import *
from tkinter.ttk import Combobox
import json



window=Tk()
window.geometry("500x600+500+100")
window.config(bg="cyan")
window.title("Currency Translation")

window_title=Label(window,text="CURRENCY TRANSLATION",font="Verdana 17 bold",bg="cyan")
window_title.pack(padx=5,pady=30)

api_key="YOUR API"

api_url=f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"  

try:
    response=requests.get(api_url).json()
    rate=sorted(list(response["conversion_rates"].keys()))
except:
    print("Api Hatası!!!")
    rate=[]


num=StringVar()

def calculate_currency():
    try:
        from_curr=source_money.get()
        to_curr=target_money.get()
        _amount=float(num.get())
     

        rates = response["conversion_rates"]
        total=(_amount / rates[from_curr]) * rates[to_curr]

        result.configure(text=f"Result: {total:.2f} {to_curr}")

    except Exception as ex:
        result.config(text="Hata: Geçersiz miktar! veya Seçim ")
       
    
def turn_over():

    from_curr=source_money.get()
    to_curr=target_money.get()

    source_money.set(to_curr)
    target_money.set(from_curr)

    calculate_currency()



source_money=Combobox(window,width=40,height=10,values=rate,state="readonly")
source_money.set("USD")
source_money.pack(padx=20,pady=20)

reverse_btn=Button(window,text="⇅",font="Verdana 14 bold",command=turn_over)
reverse_btn.pack(padx=20,pady=20)

target_money=Combobox(window,width=40,height=10,values=rate,state="readonly")
target_money.set("TRY")
target_money.pack(padx=20,pady=20)

amount=Entry(textvariable=num,font="Verdana 14")
amount.pack(padx=20,pady=20)
num.set("1")


calculate_btn=Button(window,text="Calculate",activebackground="green",width=15,height=2,font="Verdana 12 italic",command=calculate_currency)
calculate_btn.pack(padx=20,pady=20)

result=Label(window,text="CALCULATING...",font="Times 13 bold",bg="white",width=30)
result.pack(padx=20,pady=20)


window.mainloop()