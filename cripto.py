alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def Search(huruf):
	return alphabet.find(huruf)
	
def VigenereSimpleEncrypt(kalimat, kunci):
	i = 0
	cipher = ''
	for char in kalimat:
		if (char in alphabet):
			cipher += chr(((Search(char) + Search(kunci[i])) % 26) + 65)
			if (i < len(kunci) - 1):
				i += 1
			else:
				i = 0
		else:
			cipher += char
	print(cipher)

def VigenereSimpleDecrypt(cipher, kunci):
	i = 0
	kalimat = ''
	for char in cipher:
		if (char in alphabet):
			kalimat += chr(((Search(char) - Search(kunci[i])) % 26) + 65)
			if (i < len(kunci) - 1):
				i += 1
			else:
				i = 0
		else:
			kalimat += char
	print(kalimat)

kalimat = input("Masukkan sebuah kalimat: ")
print("Masukkan 1 untuk menggunakan Vigenere Cipher standard")
print("Masukkan 2 untuk menggunakan Vigenere Cipher extended")
print("Masukkan 3 untuk menggunakan Playfair Cipher")
print("")
pilihan = input("Masukkan pilihan: ")
if (pilihan == '1'):
	pil = input("Masukkan 'enc' atau 'dec': ")
	kunci = input("Masukkan key: ")
	if (pil == 'enc'):
		VigenereSimpleEncrypt(kalimat, kunci)
	elif (pil == 'dec'):
		VigenereSimpleDecrypt(kalimat, kunci)
elif (pilihan == '2'):
	None
elif (pilihan == '3'):
	None
else:
	None
