import tkinter as tk
from tkinter import messagebox
from plyer import notification
import time
import threading

class NotificationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Notification App")
        
        # Title Label and Entry
        tk.Label(root, text="Notification Title:").grid(row=0, column=0, padx=10, pady=10)
        self.title_entry = tk.Entry(root, width=50)
        self.title_entry.grid(row=0, column=1, padx=10, pady=10)
        
        # Message Label and Entry
        tk.Label(root, text="Notification Message:").grid(row=1, column=0, padx=10, pady=10)
        self.message_entry = tk.Entry(root, width=50)
        self.message_entry.grid(row=1, column=1, padx=10, pady=10)
        
        # Interval Label and Entry
        tk.Label(root, text="Notification Interval (minutes):").grid(row=2, column=0, padx=10, pady=10)
        self.interval_entry = tk.Entry(root, width=50)
        self.interval_entry.grid(row=2, column=1, padx=10, pady=10)
        
        # Start Button
        self.start_button = tk.Button(root, text="Start Notifications", command=self.start_notifications)
        self.start_button.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Status Label
        self.status_label = tk.Label(root, text="Status: Idle", fg="red")
        self.status_label.grid(row=4, column=0, columnspan=2, pady=10)

    def start_notifications(self):
        title = self.title_entry.get()
        message = self.message_entry.get()
        try:
            interval = int(self.interval_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for the interval.")
            return
        
        if not title or not message:
            messagebox.showerror("Missing Information", "Please fill in both title and message.")
            return
        
        self.status_label.config(text="Status: Running", fg="green")
        self.start_button.config(state=tk.DISABLED)
        
        # Start the notification thread
        self.notification_thread = threading.Thread(target=self.send_notifications, args=(title, message, interval))
        self.notification_thread.daemon = True
        self.notification_thread.start()

    def send_notifications(self, title, message, interval):
        while True:
            notification.notify(
                title=title,
                message=message,
                app_name='NotificationApp',
                timeout=10
            )
            time.sleep(interval * 60)

if __name__ == "__main__":
    root = tk.Tk()
    app = NotificationApp(root)
    root.mainloop()
