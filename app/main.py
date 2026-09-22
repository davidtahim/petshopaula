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
    
    button_frame = tk.Frame(janela, bg="#f4f7fb")
    button_frame.pack(pady=20)
    
    tk.Button(
        button_frame,
        text="Gerenciar Clientes",
        font=("Arial", 14),
        bg="black",
        fg="white",
        width=20,
        height=2,
        command=lambda: print("Gerenciar Clientes")
    ).grid(row=0, column=0, padx=10, pady=10)
    
    tk.Button(
        button_frame,
        text="Gerenciar Pets",
        font=("Arial", 14),
        bg="black",
        fg="white",
        width=20,
        height=2,
        command=lambda: print("Gerenciar Pets")
    ).grid(row=0, column=1, padx=10, pady=10)
    
    tk.Button(
        button_frame,
        text="Sair",
        font=("Arial", 14),
        bg="black",
        fg="white",
        width=20,
        height=2,
        command=janela.quit
    ).grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
    
    janela.clientes_page = tk.Frame(janela, bg="#f4f7fb", padx=10, pady=10)
    janela._build_clientes_page()
    
    def _build_clientes_page(janela):
        titulo = tk.Label(
            janela.clientes_page,
            text="Página de Gerenciamento de Clientes",
            font=("Arial", 20, "bold"),
            bg="#f4f7fb",
            fg="#1F2937"
        )
        
        titulo.pack(anchor="w", pady=20)
        
        form = tk.Frame(janela.clientes_page, bg="#f4f7fb")
        form.pack(anchor="w", pady=10)
        
        janela.clientes_entries = {}
        labels = ["ID","Nome", "Telefone", "Email"]
        
        for idx, label in enumerate(labels):
            tk.Label(form, text=label, font=("Arial", 14), bg="#f4f7fb", fg="#1F2937").grid(row=idx, column=0, sticky="w", pady=5)
            entry = tk.Entry(form, font=("Arial", 14), width=30)
            entry.grid(row=idx, column=1, pady=5)
            janela.clientes_entries[label] = entry
       form.columnconfigure(1, weight=1)      
    
    janela.mainloop()