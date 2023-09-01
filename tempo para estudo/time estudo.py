import tkinter as tk
from tkinter import ttk
import threading
import time

def take_break(self):
    break_duration = 5 * 60  # 5 minutos de descanso em segundos
    self.sessions.append(break_duration)
    self.update_timer_thread = threading.Thread(target=self.update_timer)
    self.update_timer_thread.start()
class StudyTimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contador de Tempo de Estudo")

        self.sessions = []
        self.current_session = None
        self.running = False

        self.label = tk.Label(root, text="Tempo de estudo:", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.timer_label = tk.Label(root, text="25:00", font=("Helvetica", 36))
        self.timer_label.pack()

        self.duration_minutes = tk.IntVar()
        self.duration_minutes.set(25)
        self.entry = ttk.Entry(root, textvariable=self.duration_minutes)
        self.entry.pack(pady=5)

        self.start_button = ttk.Button(root, text="Iniciar", command=self.start_timer)
        self.start_button.pack()

        self.pause_button = ttk.Button(root, text="Pausar", command=self.pause_timer)
        self.pause_button.pack()

        self.resume_button = ttk.Button(root, text="Retomar", command=self.resume_timer)
        self.resume_button.pack()

    def start_timer(self):
        if not self.running:
            session_duration = self.duration_minutes.get()
            self.sessions.append(session_duration * 60)
            self.running = True
            self.update_timer_thread = threading.Thread(target=self.update_timer)
            self.update_timer_thread.start()

    def pause_timer(self):
        self.running = False

    def resume_timer(self):
        if not self.running:
            self.running = True
            self.update_timer_thread = threading.Thread(target=self.update_timer)
            self.update_timer_thread.start()

    def update_timer(self):
        while self.sessions:
            self.current_session = self.sessions.pop(0)
            while self.current_session > 0 and self.running:
                minutes, seconds = divmod(self.current_session, 60)
                time_format = f"{minutes:02}:{seconds:02}"
                self.timer_label.config(text=time_format)
                time.sleep(1)
                self.current_session -= 1
            self.timer_label.config(text="00:00")
            self.running = False

def update_timer(self):
    while self.sessions:
        self.current_session = self.sessions.pop(0)
    message = "Tempo de Estudo"
    if self.current_session <= 0:
        message = "Descansando"
        while self.current_session > 0 and self.running:
            minutes, seconds = divmod(self.current_session, 60)
            time_format = f"{minutes:02}:{seconds:02}"
            self.timer_label.config(text=f"{message}: {time_format}")
            time.sleep(1)
            self.current_session -= 1
        self.timer_label.config(text="00:00")
    if self.sessions:
        self.take_break()  # Inicia o período de descanso
    self.running = False
def main():
    root = tk.Tk()
    app = StudyTimerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
