import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import sqlite3
from tkinter import messagebox

def conectar():
    return sqlite3.connect("aluguel_carros.db")


def criar_banco():
    conn = conectar()
    cursor = conn.cursor()
    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS clientes (
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT UNIQUE NOT NULL,
        telefone TEXT
    );

    CREATE TABLE IF NOT EXISTS veiculos (
        id_veiculo INTEGER PRIMARY KEY AUTOINCREMENT,
        modelo TEXT NOT NULL,
        placa TEXT UNIQUE NOT NULL,
        status TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS alugueis (
        id_aluguel INTEGER PRIMARY KEY AUTOINCREMENT,
        id_cliente INTEGER,
        id_veiculo INTEGER,
        data_inicio TEXT,
        data_fim TEXT,
        FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
        FOREIGN KEY (id_veiculo) REFERENCES veiculos(id_veiculo)
    );
    """)
    conn.commit()
    conn.close()


def cadastrar_cliente():
    def salvar():
        nome = nome_entry.get()
        cpf = cpf_entry.get()
        telefone = tel_entry.get()
        try:
            conn = conectar()
            conn.execute("INSERT INTO clientes (nome, cpf, telefone) VALUES (?, ?, ?)", (nome, cpf, telefone))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Cliente cadastrado!")
            win.destroy()
        except:
            messagebox.showerror("Erro", "CPF ja cadastrado")

    win = ttk.Toplevel(title="Cadastrar Cliente")
    win.geometry("300x200")
    nome_entry = ttk.Entry(win, width=25)
    cpf_entry = ttk.Entry(win, width=25)
    tel_entry = ttk.Entry(win, width=25)
    ttk.Label(win, text="Nome:").pack()
    nome_entry.pack(pady=3)
    ttk.Label(win, text="CPF:").pack()
    cpf_entry.pack(pady=3)
    ttk.Label(win, text="Telefone:").pack()
    tel_entry.pack(pady=3)
    ttk.Button(win, text="Salvar", command=salvar, bootstyle="success").pack(pady=10)

def cadastrar_veiculo():
    def salvar():
        modelo = modelo_entry.get()
        placa = placa_entry.get()
        try:
            conn = conectar()
            conn.execute("INSERT INTO veiculos (modelo, placa, status) VALUES (?, ?, 'Disponivel')", (modelo, placa))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Veiculo cadastrado!")
            win.destroy()
        except:
            messagebox.showerror("Erro", "Placa ja cadastrada")

    win = ttk.Toplevel(title="Cadastrar Veiculo")
    win.geometry("300x180")
    modelo_entry = ttk.Entry(win, width=25)
    placa_entry = ttk.Entry(win, width=25)
    ttk.Label(win, text="Modelo:").pack()
    modelo_entry.pack(pady=3)
    ttk.Label(win, text="Placa:").pack()
    placa_entry.pack(pady=3)
    ttk.Button(win, text="Salvar", command=salvar, bootstyle="success").pack(pady=10)

def listar_clientes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id_cliente, nome, cpf FROM clientes")
    clientes = cursor.fetchall()
    conn.close()
    win = ttk.Toplevel(title="Clientes")
    for c in clientes:
        ttk.Label(win, text=f"ID: {c[0]} | Nome: {c[1]} | CPF: {c[2]}").pack(anchor="w", padx=10)

def listar_veiculos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id_veiculo, modelo, placa FROM veiculos WHERE status = 'Disponivel'")
    veiculos = cursor.fetchall()
    conn.close()
    win = ttk.Toplevel(title="Veiculos Disponiveis")
    for v in veiculos:
        ttk.Label(win, text=f"ID: {v[0]} | Modelo: {v[1]} | Placa: {v[2]}").pack(anchor="w", padx=10)

def alugar_veiculo():
    def alugar():
        try:
            conn = conectar()
            conn.execute("INSERT INTO alugueis (id_cliente, id_veiculo, data_inicio, data_fim) VALUES (?, ?, ?, ?)",
                         (id_cli.get(), id_vei.get(), dt_ini.get(), dt_fim.get()))
            conn.execute("UPDATE veiculos SET status = 'Alugado' WHERE id_veiculo = ?", (id_vei.get(),))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Veiculo alugado!")
            win.destroy()
        except:
            messagebox.showerror("Erro", "Verifique os dados")



    win = ttk.Toplevel(title="Alugar Veiculo")
    win.geometry("300x250")
    id_cli = ttk.Entry(win, width=25)
    id_vei = ttk.Entry(win, width=25)
    dt_ini = ttk.Entry(win, width=25)
    dt_fim = ttk.Entry(win, width=25)
    ttk.Label(win, text="ID Cliente:").pack()
    id_cli.pack(pady=3)
    ttk.Label(win, text="ID Veiculo:").pack()
    id_vei.pack(pady=3)
    ttk.Label(win, text="Data Inicio:").pack()
    dt_ini.pack(pady=3)
    ttk.Label(win, text="Data Fim:").pack()
    dt_fim.pack(pady=3)
    ttk.Button(win, text="Confirmar", command=alugar, bootstyle="info").pack(pady=10)

criar_banco()
app = ttk.Window(title="Sistema de Aluguel de Carros", themename="cosmo")
app.geometry("420x500")
app.resizable(False, False)

ttk.Label(app, text="MENU PRINCIPAL", font=("Segoe UI", 18, "bold")).pack(pady=25)

ttk.Button(app, text="Cadastrar Cliente", width=30, command=cadastrar_cliente, bootstyle="primary-outline").pack(pady=6)
ttk.Button(app, text="Cadastrar Veiculo", width=30, command=cadastrar_veiculo, bootstyle="success-outline").pack(pady=6)
ttk.Button(app, text="Listar Clientes", width=30, command=listar_clientes, bootstyle="info-outline").pack(pady=6)
ttk.Button(app, text="Listar Veiculos Disponiveis", width=30, command=listar_veiculos, bootstyle="warning-outline").pack(pady=6)
ttk.Button(app, text="Alugar Veiculo", width=30, command=alugar_veiculo, bootstyle="secondary-outline").pack(pady=6)
ttk.Button(app, text="Sair", width=30, command=app.destroy, bootstyle="danger-outline").pack(pady=30)

app.mainloop()