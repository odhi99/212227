from tkinter import *

class CaesarCipherGUI:
    def __init__(self, master):
        self.master = master
        master.title("Caesar Cipher")

        self.label1 = Label(master, text="Masukkan pesan:")
        self.label1.grid(row=0, column=0)

        self.entry1 = Entry(master, width=50)
        self.entry1.grid(row=0, column=1, columnspan=2)

        self.label2 = Label(master, text="Masukkan kunci:")
        self.label2.grid(row=1, column=0)

        self.entry2 = Entry(master, width=50)
        self.entry2.grid(row=1, column=1, columnspan=2)

        self.button1 = Button(master, text="Enkripsi", command=self.encrypt)
        self.button1.grid(row=2, column=1)

        self.button2 = Button(master, text="Dekripsi", command=self.decrypt)
        self.button2.grid(row=2, column=2)

        self.label3 = Label(master, text="Hasil:")
        self.label3.grid(row=3, column=0)

        self.result = Text(master, height=5, width=50)
        self.result.grid(row=4, column=0, columnspan=3)

    def encrypt(self):
        plaintext = self.entry1.get()
        key = int(self.entry2.get())
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                char = chr((ord(char) + key - 65) % 26 + 65)
            ciphertext += char
        self.result.delete(1.0, END)
        self.result.insert(END, ciphertext)

    def decrypt(self):
        ciphertext = self.entry1.get()
        key = int(self.entry2.get())
        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                char = chr((ord(char) - key - 65) % 26 + 65)
            plaintext += char
        self.result.delete(1.0, END)
        self.result.insert(END, plaintext)

root = Tk()
my_gui = CaesarCipherGUI(root)
root.mainloop()