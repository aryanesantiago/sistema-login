from tkinter import *
import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image
from banco import Banco

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.banco = Banco()
        self.banco.cria_tabela()
        self.configuracoes_janela_inicial()
        self.tela_login()

    def configuracoes_janela_inicial(self):
        self.geometry("700x400")
        self.title("Sistema de Login")
        self.resizable(False, False)
    
    def tela_login(self):
        if hasattr(self, "frame_cadastro"):
            self.frame_cadastro.place_forget()
            self.limpa_entry_cadastro()
        self.limpa_entry_login()

        img = Image.open("image.png")
        self.img = CTkImage(light_image=img, dark_image=img, size=(300, 300))
        self.lb_img = ctk.CTkLabel(self, text=None, image=self.img)
        self.lb_img.grid(row=1, column=0, padx=10)

        self.title_label = ctk.CTkLabel(
            self, 
            text="Faça seu login ou cadastre-se na nossa\nplataforma para acessar os nossos serviços!",
            font=("Century Gothic", 14, 'bold')
        )
        self.title_label.grid(row=0, column=0, pady=10, padx=0)

        self.frame_login = ctk.CTkFrame(self, width=350, height=380)
        self.frame_login.place(x=350, y=10)

        self.lb_title = ctk.CTkLabel(self.frame_login, text="Faça o seu Login", font=("Century Gothic", 22, 'bold'))
        self.lb_title.grid(row=0, column=0, padx=10, pady=10)

        self.username_login_entry = ctk.CTkEntry(
            self.frame_login, width=300, placeholder_text="Seu nome de usuário..",
            font=("Century Gothic", 16, 'bold'), corner_radius=15, border_color="purple"
        )
        self.username_login_entry.grid(row=1, column=0, padx=1, pady=10)

        self.senha_login_entry = ctk.CTkEntry(
            self.frame_login, width=300, placeholder_text="Sua senha..",
            font=("Century Gothic", 16, 'bold'), corner_radius=15, border_color="purple", show="*"
        )
        self.senha_login_entry.grid(row=2, column=0, padx=1, pady=10)

        self.ver_senha_login = ctk.CTkCheckBox(
            self.frame_login, text="Clique para ver a senha",
            font=("Century Gothic", 14, 'bold'), corner_radius=20,
            command=self.toggle_senha_login
        )
        self.ver_senha_login.grid(row=3, column=0, padx=1, pady=10)

        self.btn_login = ctk.CTkButton(
            self.frame_login, width=300, text="Fazer login".upper(),
            font=("Century Gothic", 16, 'bold'), fg_color="purple",
            corner_radius=15, hover_color="#9400D3", command=self.verifica_login
        )
        self.btn_login.grid(row=4, column=0, padx=1, pady=10)
        
        self.span = ctk.CTkLabel(
            self.frame_login, text="Não tem conta? clique no botão abaixo para se cadastrar",
            font=("Century Gothic", 10)
        )
        self.span.grid(row=5, column=0, padx=10, pady=10)

        self.btn_cadastro = ctk.CTkButton(
            self.frame_login, width=300, text="Fazer cadastro".upper(),
            font=("Century Gothic", 16, 'bold'), fg_color="#52215A",
            corner_radius=15, command=self.tela_cadastro, hover_color="#9400D3"
        )
        self.btn_cadastro.grid(row=6, column=0, padx=1, pady=10)

    def toggle_senha_login(self):
        if self.ver_senha_login.get():
            self.senha_login_entry.configure(show="")
        else:
            self.senha_login_entry.configure(show="*")

    def tela_cadastro(self):
        self.frame_login.place_forget()
        self.limpa_entry_login()

        self.frame_cadastro = ctk.CTkFrame(self, width=350, height=380)
        self.frame_cadastro.place(x=350, y=10)

        self.lb_title = ctk.CTkLabel(self.frame_cadastro, text="Faça o seu Cadastro", font=("Century Gothic", 22, 'bold'))
        self.lb_title.grid(row=0, column=0, padx=10, pady=10)
      
        self.username_cadastro_entry = ctk.CTkEntry(
            self.frame_cadastro, width=300, placeholder_text="Seu nome de usuário",
            font=("Century Gothic", 16, 'bold'), corner_radius=15, border_color="purple"
        )
        self.username_cadastro_entry.grid(row=1, column=0, padx=1, pady=10)

        self.email_cadastro_entry = ctk.CTkEntry(
            self.frame_cadastro, width=300, placeholder_text="E-mail de usuário",
            font=("Century Gothic", 16, 'bold'), corner_radius=15, border_color="purple"
        )
        self.email_cadastro_entry.grid(row=2, column=0, padx=1, pady=10)

        self.senha_cadastro_entry = ctk.CTkEntry(
            self.frame_cadastro, width=300, placeholder_text="Senha de usuário",
            font=("Century Gothic", 16, 'bold'), corner_radius=15, border_color="purple", show="*"
        )
        self.senha_cadastro_entry.grid(row=3, column=0, padx=1, pady=10)

        self.confirma_senha_entry = ctk.CTkEntry(
            self.frame_cadastro, width=300, placeholder_text="Confirme sua senha",
            font=("Century Gothic", 16, 'bold'), corner_radius=15, border_color="purple", show="*"
        )
        self.confirma_senha_entry.grid(row=4, column=0, padx=1, pady=10)

        self.ver_senha_cadastro = ctk.CTkCheckBox(
            self.frame_cadastro, text="Clique para ver a senha",
            font=("Century Gothic", 14, 'bold'), corner_radius=20,
            command=self.toggle_senha_cadastro
        )
        self.ver_senha_cadastro.grid(row=5, column=0, padx=1, pady=10)

        self.btn_cadastrar = ctk.CTkButton(
            self.frame_cadastro, width=300, text="Cadastrar".upper(),
            font=("Century Gothic", 16, 'bold'), fg_color="#52215A",
            corner_radius=15, hover_color="#9400D3", command=self.cadastrar_usuario
        )
        self.btn_cadastrar.grid(row=6, column=0, padx=1, pady=10)
      
        self.btn_login_back = ctk.CTkButton(
            self.frame_cadastro, width=300, text="Voltar ao login".upper(),
            font=("Century Gothic", 16, 'bold'), fg_color="purple",
            corner_radius=15, hover_color="#9400D3", command=self.tela_login
        )
        self.btn_login_back.grid(row=7, column=0, padx=1, pady=10)

    def toggle_senha_cadastro(self):
        if self.ver_senha_cadastro.get():
            self.senha_cadastro_entry.configure(show="")
            self.confirma_senha_entry.configure(show="")
        else:
            self.senha_cadastro_entry.configure(show="*")
            self.confirma_senha_entry.configure(show="*")

    def limpa_entry_cadastro(self):
        try:
            self.username_cadastro_entry.delete(0, END)
            self.email_cadastro_entry.delete(0, END)
            self.senha_cadastro_entry.delete(0, END)
            self.confirma_senha_entry.delete(0, END)
        except AttributeError:
            pass

    def limpa_entry_login(self):
        try:
            self.username_login_entry.delete(0, END)
            self.senha_login_entry.delete(0, END)
        except AttributeError:
            pass

    def cadastrar_usuario(self):
        username = self.username_cadastro_entry.get()
        email = self.email_cadastro_entry.get()
        senha = self.senha_cadastro_entry.get()
        confirma_senha = self.confirma_senha_entry.get()

        if not (username and email and senha and confirma_senha):
            ctk.CTkMessageBox.show_error("Erro", "Preencha todos os campos!")
            return
        elif len(username) < 4:
            ctk.CTkMessageBox.show_warning("Erro", "O nome de usuário deve ter pelo menos 4 caracteres.")
            return
        elif len(senha) < 4:
            ctk.CTkMessageBox.show_warning("Erro", "Sua senha é muito curta.")
            return
        elif senha != confirma_senha:
            ctk.CTkMessageBox.show_error("Erro", "Senhas não conferem")
            return

        self.banco.cadastrar_usuario(username, email, senha, confirma_senha)
        self.limpa_entry_cadastro()

    def verifica_login(self):
        username = self.username_login_entry.get()
        senha = self.senha_login_entry.get()

        resultado = self.banco.verifica_login(username, senha)
        if resultado:
            ctk.CTkMessageBox.show_info("Sucesso", f"Bem-vindo, {username}!")
        else:
            ctk.CTkMessageBox.show_error("Erro", "Usuário ou senha inválidos")
        self.limpa_entry_login()


if __name__ == "__main__":
    app = App()
    app.mainloop()
