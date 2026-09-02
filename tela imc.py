import tkinter as tk
from tkinter import messagebox

def show_next_screen(event = none):
    for widget in
root.winfo_children()
        widget.destroy()

        next_label = tk.label(root, def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        imc = peso / (altura ** 2)
        messagebox.showinfo("Resultado do IMC", f"Seu IMC é: {imc:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

def abrir():
    print('abrir')

def salvar():
    print('salvar')

def ajuda():
    messagebox.showinfo("Ajuda", "Para calcular seu IMC, insira seu peso em quilogramas e sua altura em metros, depois clique no botão 'Calcular IMC'.")

root = tk.Tk()
root.title("Cálculo de IMC")

principal = tk.Menu(root)
arquivo = tk.Menu(principal, tearoff=0)
arquivo.add_command(label='Abrir', command=abrir)
arquivo.add_command(label='Salvar', command=salvar)
principal.add_cascade(label='Arquivo', menu=arquivo)
principal.add_command(label='Ajuda', command=ajuda)
root.config(menu=principal)

imc_frame = tk.Frame(root)
imc_frame.pack(padx=10, pady=10)

label_peso = tk.Label(imc_frame, text="Peso (kg):")
label_peso.grid(row=0, column=0, padx=5, pady=5)
entry_peso = tk.Entry(imc_frame)
entry_peso.grid(row=0, column=1, padx=5, pady=5)

label_altura = tk.Label(imc_frame, text="Altura (m):")
label_altura.grid(row=1, column=0, padx=5, pady=5)
entry_altura = tk.Entry(imc_frame)
entry_altura.grid(row=1, column=1, padx=5, pady=5)

button_calcular = tk.Button(imc_frame, text="Calcular IMC", command=calcular_imc)
button_calcular.grid(row=2, columnspan=2, pady=10))

next_label.pack(expand=True)

root = tk.Tk()
root.title("Projeto Guilherme B. e Yasmim A.")
root.geometry("800x600")

label = tk.Label(root, text= "Projeto Guilherme B. e Yasmim A.", font= ("Arial", 40))
label.pack(expand= True)

root.bind("<space>", show_next_screen)

root.mainloop()