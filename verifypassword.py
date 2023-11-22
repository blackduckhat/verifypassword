import string
from tkinter import *


root = Tk()


class Funcclearglobal:
    def func_compiled_in_functionmsg(self):
        self.entry_password.delete(0, END)
        self.label_msg.destroy()


class ApplicationPegasus(Funcclearglobal):
    def __init__(self):
        self.root = root
        self.display()
        self.entry_and_buttons_normies()
        root.mainloop()

    def display(self):
        self.root.title("verifypassword")
        self.root.configure(background="black",
                            cursor="arrow")
        self.root.geometry("800x600")
    # Função para o botão de Verificar.

    def function_msg(self):
        self.point_range = []
        self.point_lettersnumbers = []
        self.point_caracter_especial = []
        self.lettersnumbers = string.printable[0:94]
        self.point_count = 0
        # Todos os dados foram baseados em minha expectativa de senha forte.
        for unit_range in self.entry_password.get():
            if len(self.entry_password.get()) >= 8:
                self.point_count += 1
                self.point_range.append(self.point_count)
                if unit_range in self.lettersnumbers:
                    self.quantity_numbersletters = self.entry_password.get()
                    self.count_both = self.quantity_numbersletters.count(unit_range)
                    self.point_lettersnumbers.append(self.count_both)
                    if unit_range in self.lettersnumbers[62:94]:
                        self.quantity_caracter = self.entry_password.get()
                        self.count_caracter = self.quantity_caracter.count(unit_range)
                        self.point_caracter_especial.append(self.count_caracter)
                    if sum(self.point_lettersnumbers) >= 5 and sum(self.point_caracter_especial) >= 1:
                        self.label_msg = Label(self.root, text="/> Sua senha é forte", bg="black", fg="green2")
                        self.label_msg.place(relx=0.345, rely=0.31)
                    else:
                        self.label_msg = Label(self.root, text="/> Sua senha é boa", bg="black", fg="green2")
                        self.label_msg.place(relx=0.345, rely=0.31)
            else:
                self.label_msg = Label(self.root,
                                       text="/> Senha é menor que 8 caracteres",
                                       bg="black",
                                       fg="green2")
                self.label_msg.place(relx=0.345, rely=0.31)

    def entry_and_buttons_normies(self):
        self.verify_password = Label(self.root,
                                      text="Teste sua Senha",
                                      cursor="hand2",
                                      bg="gray9",
                                      fg="green2",)
        self.verify_password.place(relx=0.35, rely=0.2, relwidth=0.31)
        self.entry_password = Entry(self.root,
                                    bg="gray8",
                                    fg="green2")
        self.entry_password.place(relx=0.35, rely=0.27, relwidth=0.31)
        self.button_verify = Button(self.root,
                                    text="Verificar",
                                    bd=2,
                                    bg="gray9",
                                    fg="green2",
                                    command=self.function_msg,
                                    cursor="hand2")
        self.button_verify.place(relx=0.68, rely=0.2, relwidth=0.1)
        self.button_clear_all = Button(self.root,
                                       text="Limpar",
                                       bd=2,
                                       bg="gray9",
                                       fg="green2",
                                       cursor="hand2", command=self.func_compiled_in_functionmsg)
        self.button_clear_all.place(relx=0.68, rely=0.26, relwidth=0.1)


ApplicationPegasus()
