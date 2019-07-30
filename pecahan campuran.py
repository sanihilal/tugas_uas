import math
import os


def Penjumlahan_dua_buah_bilangan():
    print("Penjumlahan dua buah bilangan")
    print(" ")
    print("Masukkan angka pecahan pertama")
    e = int(input())
    a = int(input())
    print("-")
    b = int(input())
    print("Masukkan angka pecahan kedua")
    f = int(input())
    c = int(input())
    print("-")
    d = int(input())
    g = (b*e)+a
    h = (d*f)+c
    print("jadi penjumlahannya = ","", a,"        ",c)
    print("                     ",e,"-    +"," "    ,f,"- ")
    print("                      ","", b,"        ",d)
    print(" ")
    print("bentuk sederhananya = ","",g,"      ",h)
    print("                        -    +    -")
    print("                      ","",b, "       ",d)
    print(" ")
    print("Hasil = ", ((g * d) + (b * h)))
    print("         -")
    print("        ", (b * d))
    print(" ")
    print("hasil desimalnya = ",((g * d) + (b * h))/(b * d))


def Pengurangan_dua_buah_bilangan():
    print("Pengurangan dua buah bilangan")
    print(" ")
    print("Masukkan angka pecahan pertama")
    a = int(input())
    print("-")
    b = int(input())
    print("Masukkan angka pecahan kedua")
    c = int(input())
    print("-")
    d = int(input())
    print("Hasil : ", ((a * d) - (b * c)))
    print("         -")
    print("        ", (b * d))
    print(" ")


def Perkalian_dua_buah_bilangan():
    print("Perkalian dua buah bilangan")
    print(" ")
    print("Masukkan angka pecahan pertama")
    a = int(input())
    print("-")
    b = int(input())
    print("Masukkan angka pecahan kedua")
    c = int(input())
    print("-")
    d = int(input())
    print("Hasil : ", (a * c))
    print("         -")
    print("        ", (b * d))
    print(" ")


def Pembagian_dua_buah_bilangan():
    print("Pembagian dua buah bilangan")
    print(" ")
    print("Masukkan angka pecahan pertama")
    a = int(input())
    print("-")
    b = int(input())
    print("Masukkan angka pecahan kedua")
    c = int(input())
    print("-")
    d = int(input())
    print("Hasil : ", (a * d))
    print("         -")
    print("        ", (b * c))
    print(" ")


# -------------------------------
while 1:
    print("Kalkulator Sederhana")
    print(" ")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

    # -------------------------------

    pilihan = int(input("\nPilihan: "))
    if pilihan == 1:
        Penjumlahan_dua_buah_bilangan()
    elif pilihan == 2:
        Pengurangan_dua_buah_bilangan()
    elif pilihan == 3:
        Perkalian_dua_buah_bilangan()
    elif pilihan == 4:
        Pembagian_dua_buah_bilangan()
    elif pilihan == 5:
        print("")
        print("Terima kasih Broo....")
        print("")
        os.system('pause')
        break
    else:
        print("Pilihan salah")
        print("")