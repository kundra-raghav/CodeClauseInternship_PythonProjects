import tkinter as tk
from tkinter import ttk
import time
import winsound

def set_alarm():
    alarm_time = alarm_var.get()
    while True:
        current_time = time.strftime('%H:%M:%S')
        time_label.config(text=current_time)
        if current_time == alarm_time:
            play_alarm_sound()
            break
        root.update()  # Update the main window to refresh the time display

def play_alarm_sound():
    for _ in range(5):  # Play beep sound for 5 times
        winsound.Beep(2500, 1000)  # Frequency: 2500 Hz, Duration: 1 second

def stop_alarm():
    pass  # You can add stop alarm functionality here if needed

def snooze_alarm():
    snooze_duration = 5  # Snooze duration in seconds
    time.sleep(snooze_duration)
    set_alarm()

# Create the main Tkinter window
root = tk.Tk()
root.title("Stylish Alarm Clock")
root.geometry("400x250")

# Styling
style = ttk.Style()
style.configure('TButton', font=('Arial', 12))
style.configure('TLabel', font=('Arial', 16))

# Digital clock display
time_label = ttk.Label(root, text="", anchor='center')
time_label.pack(pady=20)

# Alarm time picker
alarm_var = tk.StringVar()
alarm_var.set(time.strftime('%H:%M:%S'))
alarm_time_picker = ttk.Entry(root, textvariable=alarm_var, font=('Arial', 12), width=8)
alarm_time_picker.pack()

# Set Alarm button
set_alarm_button = ttk.Button(root, text="Set Alarm", command=set_alarm)
set_alarm_button.pack(pady=10)

# Stop Alarm button
stop_alarm_button = ttk.Button(root, text="Stop Alarm", command=stop_alarm)
stop_alarm_button.pack(pady=10)

# Snooze Alarm button
snooze_alarm_button = ttk.Button(root, text="Snooze Alarm", command=snooze_alarm)
snooze_alarm_button.pack(pady=10)

# Run the main event loop
root.mainloop()
