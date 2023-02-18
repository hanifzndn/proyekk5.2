
import os

def tambah_kontak():
    nama = input("Masukkan nama: ")
    nomor_hp = input("Masukkan nomor telepon: ")
    with open("phone_book.txt", "a") as file:
        file.write(nama + ": " + nomor_hp + "\n")

def hapus_kontak():
    nama = input("Masukkan nama kontak yang akan dihapus: ")
    with open("phone_book.txt", "r") as file:
        lines = file.readlines()
    with open("phone_book.txt", "w") as file:
        for line in lines:
            if line.split(":")[0] != nama:
                file.write(line)

def update_kontak():
    nama = input("Masukkan nama kontak yang akan diperbarui: ")
    with open("phone_book.txt", "r") as file:
        lines = file.readlines()
    with open("phone_book.txt", "w") as file:
        for line in lines:
            if line.split(":")[0] != nama:
                file.write(line)
            else:
                nama_baru = input("Masukkan nama baru: ")
                nomor_hp_baru = input("Masukkan nomor telepon baru: ")
                file.write(nama_baru + " : " + nomor_hp_baru + "\n")

def tampilkan_kontak():
    with open("phone_book.txt", "r") as file:
        contacts = file.read()
        print("[DAFTAR KONTAK]")
        print(contacts)
        
while True:
    print("====[Phone Book]===")
    print("1. Tambahkan kontak baru")
    print("2. Hapus kontak")
    print("3. Update kontak")
    print("4. Tampilkan kontak")
    print("5. Keluar")
    print("===================")

    
    choice = input("Pilih Menu : ")
    if choice == "1":
        tambah_kontak()
    elif choice == "2":
        hapus_kontak()
    elif choice == "3":
        update_kontak()
    elif choice == "4":
        tampilkan_kontak()
    elif choice == "5":
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
