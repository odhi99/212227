import tkinter as tk

# Inisialisasi rotor dan konfigurasi awal
rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"

reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

rotor_positions = [0, 0, 0]

# Fungsi untuk mengenkripsi pesan
def encrypt_message():
    plaintext = input_text.get().upper()
    encrypted_text = ""
    
    for char in plaintext:
        if char.isalpha():
            encrypted_char = encrypt_char(char)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    
    output_text.set(encrypted_text)

# Fungsi untuk mengenkripsi satu karakter
def encrypt_char(char):
    rotor1_pos, rotor2_pos, rotor3_pos = rotor_positions
    char_index = ord(char) - ord('A')
    
    # Putar rotor ke posisi berikutnya
    rotor1_pos = (rotor1_pos + 1) % 26
    rotor_positions[0] = rotor1_pos
    
    # Enkripsi karakter melalui rotor 1, rotor 2, rotor 3, dan reflector
    char = rotor1[(char_index + rotor1_pos) % 26]
    char = rotor2[(ord(char) - ord('A') + rotor2_pos) % 26]
    char = rotor3[(ord(char) - ord('A') + rotor3_pos) % 26]
    char = reflector[ord(char) - ord('A')]
    char = rotor3.index(char)
    char = chr((char - rotor3_pos + 26) % 26 + ord('A'))
    char = rotor2.index(char)
    char = chr((char - rotor2_pos + 26) % 26 + ord('A'))
    char = rotor1.index(char)
    char = chr((char - rotor1_pos + 26) % 26 + ord('A'))
    
    return char

# Membuat jendela tkinter
window = tk.Tk()
window.title("Enigma Cipher")
window.geometry("400x200")

# Label dan input teks
tk.Label(window, text="Masukkan pesan:").pack()
input_text = tk.StringVar()
input_entry = tk.Entry(window, textvariable=input_text)
input_entry.pack()

# Tombol untuk mengenkripsi
encrypt_button = tk.Button(window, text="Enkripsi", command=encrypt_message)
encrypt_button.pack()

# Hasil enkripsi
output_text = tk.StringVar()
output_label = tk.Label(window, textvariable=output_text)
output_label.pack()

# Memulai jendela GUI
window.mainloop()
