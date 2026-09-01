import tkinter as tk

def inicializar_aplicacao():
    
    janela = tk.Tk()
    
    janela.title("Bem-vindo ao PetShop Amiguinhos")
    
    janela.geometry("700x400")
    
    titulo = tk.Label(
        janela,
        text="Bem-vindo ao PetShop Amiguinhos",
        font=("Arial", 24, "bold")
    )
    
    titulo.pack(pady=140)
    
    janela.mainloop()