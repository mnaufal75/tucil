import string
import re

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


def VigenereExtendedEncrypt(kalimat, kunci):
    i = 0
    cipher = ''
    for char in kalimat:
        if (char in string.printable):
            cipher += chr((ord(char) + ord(kunci[i])) % 256)
            if (i < len(kunci) - 1):
                i += 1
            else:
                i = 0
        else:
            cipher += char
    print(cipher)


def VigenereExtendedDecrypt(kalimat, kunci):
    i = 0
    cipher = ''
    for char in kalimat:
        if (char in string.ascii_letters):
            cipher += chr((ord(char) - ord(kunci[i])) % 256)
            if (i < len(kunci) - 1):
                i += 1
            else:
                i = 0
        else:
            cipher += char
    print(cipher)


def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))


def PlayfairEncrypt(kalimat, kunci):
    cipher = ''
    kalimat = re.sub("[^A-Z]+", "", kalimat)
    kunci = re.sub("[^A-Z]+", "", kunci)
    print(kalimat)
    print(kunci)
    kunciList = []
    kunciList = list(dict.fromkeys(kunci))
    for i in alphabet:
        if (i not in kunci and i != 'J'):
            kunciList.append(i)
    kunciList = [kunciList[i:i + 5] for i in range(0, len(kunciList), 5)]

    i = 0
    kalimat = list(kalimat)
    while (i < len(kalimat)):
        if (i == len(kalimat) - 1):
            None
        elif (kalimat[i] == kalimat[i + 1]):
            kalimat.insert(i + 1, 'X')
        # print(i, ' ', len(kalimat), ' ', kalimat[i], ' ', kalimat[i + 1])
        i += 2
    if (len(kalimat) % 2 == 1):
        kalimat.append('X')

    for (a, b) in zip(kalimat[0::2], kalimat[1::2]):
        indexA = index_2d(kunciList, a)
        indexB = index_2d(kunciList, b)
        # print('{} {}'.format(indexA, indexB))
        if (indexA[0] == indexB[0]):
            if (indexA[1] == 4):
                cipher += kunciList[indexA[0]][0]
                cipher += kunciList[indexB[0]][indexB[1] + 1]
            elif (indexB[1] == 4):
                cipher += kunciList[indexA[0]][indexA[1] + 1]
                cipher += kunciList[indexB[0]][0]
            else:
                cipher += kunciList[indexA[0]][indexA[1] + 1]
                cipher += kunciList[indexB[0]][indexB[1] + 1]
        elif (indexA[1] == indexB[1]):
            if (indexA[0] == 4):
                cipher += kunciList[0][indexA[1]]
                cipher += kunciList[indexB[0] + 1][indexB[1]]
            elif (indexB[0] == 4):
                cipher += kunciList[indexA[0] + 1][indexA[1]]
                cipher += kunciList[0][indexB[1]]
            else:
                cipher += kunciList[indexA[0] + 1][indexA[1]]
                cipher += kunciList[indexB[0] + 1][indexB[1]]
        else:
            cipher += kunciList[indexA[0]][indexB[1]]
            cipher += kunciList[indexB[0]][indexA[1]]
    print(cipher)


def PlayfairDecrypt(cipher, kunci):
    kalimat = ''
    cipher = re.sub("[^A-Z]+", "", cipher)
    kunci = re.sub("[^A-Z]+", "", kunci)
    kunciList = []
    kunciList = list(dict.fromkeys(kunci))
    for i in alphabet:
        if (i not in kunci and i != 'J'):
            kunciList.append(i)
    kunciList = [kunciList[i:i + 5] for i in range(0, len(kunciList), 5)]

    for (a, b) in zip(cipher[0::2], cipher[1::2]):
        indexA = index_2d(kunciList, a)
        indexB = index_2d(kunciList, b)
        # print('{} {}'.format(indexA, indexB))
        if (indexA[0] == indexB[0]):
            if (indexA[1] == 0):
                kalimat += kunciList[indexA[0]][4]
                kalimat += kunciList[indexB[0]][indexB[1] - 1]
            elif (indexB[1] == 0):
                kalimat += kunciList[indexA[0]][indexA[1] - 1]
                kalimat += kunciList[indexB[0]][4]
            else:
                kalimat += kunciList[indexA[0]][indexA[1] - 1]
                kalimat += kunciList[indexB[0]][indexB[1] - 1]
        elif (indexA[1] == indexB[1]):
            if (indexA[0] == 0):
                kalimat += kunciList[4][indexA[1]]
                kalimat += kunciList[indexB[0] - 1][indexB[1]]
            elif (indexB[0] == 0):
                kalimat += kunciList[indexA[0] - 1][indexA[1]]
                kalimat += kunciList[4][indexB[1]]
            else:
                kalimat += kunciList[indexA[0] - 1][indexA[1]]
                kalimat += kunciList[indexB[0] - 1][indexB[1]]
        else:
            kalimat += kunciList[indexA[0]][indexB[1]]
            kalimat += kunciList[indexB[0]][indexA[1]]
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
    pil = input("Masukkan 'enc' atau 'dec': ")
    kunci = input("Masukkan key: ")
    if (pil == 'enc'):
        VigenereExtendedEncrypt(kalimat, kunci)
    elif (pil == 'dec'):
        VigenereExtendedDecrypt(kalimat, kunci)
elif (pilihan == '3'):
    pil = input("Masukkan 'enc' atau 'dec': ")
    kunci = input("Masukkan key: ")
    if (pil == 'enc'):
        PlayfairEncrypt(kalimat, kunci)
    elif (pil == 'dec'):
        PlayfairDecrypt(kalimat, kunci)
else:
    None
