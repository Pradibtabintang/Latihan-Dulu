from time import time
from CRUD import Database
from CRUD.Util import random_string
import time
import os

def delete(no_buku):
    with open(Database.DB_NAME, 'r') as file:
        lines = file.readlines()
    
    # Pastikan untuk menghapus indeks yang diinginkan
    if 0 < no_buku <= len(lines):
        lines.pop(no_buku - 1)  # Menghapus baris yang sesuai dengan no_buku

    # Menyimpan kembali ke file sementara
    with open("data_temp.txt", 'w') as file_temp:
        file_temp.writelines(lines)

    # Menghapus file asli sebelum mengganti nama
    if os.path.exists(Database.DB_NAME):
        os.remove(Database.DB_NAME)

    # Mengganti nama file sementara menjadi file asli
    os.rename("data_temp.txt", Database.DB_NAME)

def update(no_buku,pk,data_add,tahun,judul,penulis):
    data = Database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = data_add
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):] 
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):] 
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

    panjang_data = len(data_str)

    try:
        with(open(Database.DB_NAME,'r+',encoding="utf-8")) as file:
            file.seek(panjang_data*(no_buku-1))
            file.write(data_str)
    except:
        print("Erro Dalam Update Data ")

def create(tahun,judul,penulis):
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%Sz",time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):] 
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):] 
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

    try:
        with open(Database.DB_NAME,'a',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data sulit di tambahkan bos, gagal lagi")

def create_first_data():
    penulis = input("Penulis: ")
    judul = input("Judul: ")
    while(True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun harus angka, silahkan masukan tahun lagi (yyyy)")
        except:
            print("Tahun harus angka, silahkan masukan tahun lagi (yyyy)")

    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%Sz",time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):] 
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):] 
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    print(data_str)
    try:
        with open(Database.DB_NAME,'w',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Udah lah gagal bosss")

def read(**kwargs):
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            jumlah_buku = len(content)
            if "index" in kwargs:
                index_buku = kwargs["index"]-1
                if index_buku < 0 or index_buku > jumlah_buku: 
                    return False 
                else:
                    return content[index_buku]
            else:
                return content
    except:
        print("Membaca database error")
        return False