import tkinter as tk
from datetime import datetime
running = False
progressive = True
display = 'Ready!'

counter = int(input("How many minutes do you want to count? "))*60


def counter_label(label):
    def regressive_count():
        global counter
        display = 'Ready!'
        display
        tt = datetime.utcfromtimestamp(counter)
        string = tt.strftime('%H:%M:%S')
        display = string

        label['text'] = display

        # label.after(arg1, arg2) delays by
        # first argument given in milliseconds
        # and then calls the function given as second argument.
        # Generally like here we need to call the
        # function in which it is present repeatedly.
        # Delays by 1000ms=1 seconds and call count again.
        label.after(1000, regressive_count)
        counter -= 1
        if counter < 0:
            Stop()

    # start function of the stopwatch
    regressive_count()


def Start(label):
    global running
    running = True
    counter_label(label)
    start['state'] = 'normal'
    stop['state'] = 'normal'
    reset['state'] = 'normal'

    # Stop function of the stopwatch


def Stop():
    global running
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'
    running = False

    # Reset function of the stopwatch


def Reset(label):
    global counter
    counter = 0
    # If reset is pressed after pressing stop.
    if not running:
        reset['state'] = 'disabled'
        label['text'] = '00:00:00'
    # If reset is pressed while the stopwatch is running.
    else:
        label['text'] = '00:00:00'


root = tk.Tk()
root.title("Stopwatch")

# Fixing the window size.
root.minsize(width=250, height=140)
label = tk.Label(root, text='Ready!', fg='black', font='Verdana 30 bold')
label.pack()
f = tk.Frame(root)
start = tk.Button(f, text='Start', width=6, command=lambda: Start(label))
stop = tk.Button(f, text='Stop', width=6, state='disabled', command=Stop)
reset = tk.Button(f, text='Reset', width=6, state='disabled',
                  command=lambda: Reset(label))
f.pack(anchor='center', pady=5)
start.pack(side='left')
stop.pack(side='left')
reset.pack(side='left')
root.mainloop()
