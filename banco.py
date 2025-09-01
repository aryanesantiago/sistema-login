import sqlite3
from tkinter import messagebox

class Banco():
    def conecta_db(self):
        self.conn = sqlite3.connect("Sistema_cadastros.db")
        self.cursor = self.conn.cursor()
    
    def desconecta_db(self):
        self.conn.close()

    def cria_tabela(self):
        self.conecta_db()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Usuarios(
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Username TEXT NOT NULL,
                Email TEXT NOT NULL,
                Senha TEXT NOT NULL,
                Confirma_senha TEXT NOT NULL
            )
        """)
        self.conn.commit()
        self.desconecta_db()

    def cadastrar_usuario(self, username, email, senha, confirma_senha):
        try:
            self.conecta_db()
            self.cursor.execute("""
                INSERT INTO Usuarios (Username, Email, Senha, Confirma_senha)
                VALUES (?, ?, ?, ?)
            """, (username, email, senha, confirma_senha))
            self.conn.commit()
        except Exception as e:
            messagebox.showerror("Sistema de login", message=f"Erro no cadastro!\n{e}")
        finally:
            self.desconecta_db()

    def verifica_login(self, username, senha):
        self.conecta_db()
        try:
            self.cursor.execute("SELECT * FROM Usuarios WHERE Username=? AND Senha=?", (username, senha))
            resultado = self.cursor.fetchone()
            return resultado
        except Exception as e:
            messagebox.showerror("Sistema de login", message=f"Erro ao verificar login!\n{e}")
            return None
        finally:
            self.desconecta_db()
