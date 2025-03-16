import os
import customtkinter as ctk

class App:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title('Sistema de Controle de Veículos')
        self.root.geometry('800x600')
        self.root.resizable(False, False)
        self.root.config(bg='#f0f0f0')
        icon_path = os.path.join('src', 'assets', 'car.ico')
        
        if os.path.exists(icon_path):
            self.root.iconbitmap(icon_path)
        
        self.create_widgets()

    def create_widgets(self):
        titulo = ctk.CTkLabel(self.root, text="Sistema de Controle de Veículos", font=("Arial", 20, "bold"))
        titulo.pack(pady=20)

    def start_ui(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = App()
    app.start_ui()
