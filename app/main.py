import tkinter as tk

def inicializar_aplicacao():
    
    janela = tk.Tk()
    
    janela.title("Bem-vindo ao PetShop Amiguinhos")
    
    janela.geometry("1024x768")
    
    janela.configure(bg="#f4f7fb")
    
    janela.resizable(False, False)
    
    
    titulo = tk.Label(
        janela,
        text="Bem-vindo ao PetShop Amiguinhos",
        font=("Arial", 24, "bold"),
        bg="#f4f7fb",
        fg="#1F2937"
    )
    
    titulo.pack(pady=40)
    
    subtitulo = tk.Label(
        janela,
        text="Sistema Simples de Gestão de Clientes e Pets",
        font=("Arial", 16),
        bg="#f4f7fb",
        fg="#1F2937"
    )
    
    subtitulo.pack(pady=20)
    
    
    janela.mainloop()