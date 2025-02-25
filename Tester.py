# Import module 
from tkinter import *
from tkinter import ttk
import time
  
# Create object 
root = Tk() 
  
# Adjust size 
root.geometry( "300x250" ) 
root.title("Currency Converter")
  
# Change the label text 
def show():
    amount = amount_entry.get()
    label1.config(text=f"From: {clicked1.get()}")
    label2.config(text=f"To: {clicked2.get()}")
    label3.config(text=f"Amount: {amount}")
    f = open("input.txt", "w")
    f.write(f"{clicked1.get()} {clicked2.get()} {amount}")
    f.close
    f = open("input.txt", "r")
    time.sleep(.6)
    result = f.read()
    label4.config(text=f"Converted: {result}")
    f.close
  
# Dropdown menu options 
options = [
    "ADA", "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARB", "ARS", "AUD",
    "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BNB",
    "BND", "BOB", "BRL", "BSD", "BTC", "BTN", "BWP", "BYN", "BYR", "BZD",
    "CAD", "CDF", "CHF", "CLF", "CLP", "CNY", "COP", "CRC", "CUC", "CUP",
    "CVE", "CZK", "DAI", "DJF", "DKK", "DOP", "DOT", "DZD", "EGP", "ERN",
    "ETB", "ETH", "EUR", "FJD", "FKP", "GBP", "GEL", "GGP", "GHS", "GIP",
    "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR",
    "ILS", "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD", "JOD", "JPY",
    "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK",
    "LBP", "LKR", "LRD", "LSL", "LTC", "LTL", "LVL", "LYD", "MAD", "MDL",
    "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MUR", "MVR", "MWK", "MXN",
    "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "OP",
    "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD",
    "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL",
    "SOL", "SOS", "SRD", "STD", "SVC", "SYP", "SZL", "THB", "TJS", "TMT",
    "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU",
    "UZS", "VEF", "VND", "VUV", "WST", "XAF", "XAG", "XAU", "XCD", "XDR",
    "XOF", "XPD", "XPF", "XPT", "XRP", "YER", "ZAR", "ZMK", "ZMW", "ZWL"
]
  
clicked1 = StringVar()
clicked1.set("Original Currency")  # Default value

clicked2 = StringVar()
clicked2.set("Converted Currency")  # Default value

# Create Dropdown menu
drop1 = ttk.Combobox(root, textvariable=clicked1, values=options, state="readonly", height=10)
drop1.pack(pady=5)

drop2 = ttk.Combobox(root, textvariable=clicked2, values=options, state="readonly", height=10)
drop2.pack(pady=5)
  
amount_label = Label(root, text="Enter Amount:")
amount_label.pack()

amount_entry = Entry(root)
amount_entry.pack(pady=5)

# Create button, it will change label text 
button = Button( root , text = "Calculate" , command = show ).pack() 
  
# Create Label 
label1 = Label(root, text="Currency 1: ")
label1.pack()

label2 = Label(root, text="Currency 2: ")
label2.pack()

label3 = Label(root, text="Amount: ")
label3.pack()

label4 = Label(root, text="Converted: ")
label4.pack()
  
# Execute tkinter 
root.mainloop() 