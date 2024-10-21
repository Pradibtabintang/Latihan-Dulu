from . import Operasi

def delete_console():
    read_console()
    while(True):
        print("Silahkan pilih nomor buku yang akan di update")
        no_buku = int(input("Nomor Buku: "))
        data_buku = Operasi.read(index=no_buku)

        if data_buku:
            data_break = data_buku.split(",")
            pk = data_break[0]
            data_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4].strip()
        
        
        # Data yang ingin di Delete
            print("\n"+"="*100)
            print("Data yang ingin anda hapus")
            print(f"2. Penulis\t: {penulis:.40}")
            print(f"3. Tahun\t: {tahun:4}")
            is_done = input("Apakah anda Yakin? ")
            if is_done == "y" or is_done == "Y":
                Operasi.delete(no_buku)
                break
        else: 
            print("Nomor tidak valid, silahkan masukan lagi")

    
    print("Data berhasil di hapus")

def update_console():
    read_console()
    while(True):
        print("Silahkan pilih nomor buku yang akan di update")
        no_buku = int(input("Nomor Buku: "))
        data_buku = Operasi.read(index=no_buku)

        if data_buku:
            break
        else: 
            print("Nomor tidak valid, silahkan masukan lagi")
        
    data_break = data_buku.split(",")

    if len(data_break) >= 5:
        pk = data_break[0]
        data_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4].strip()

        while(True):
        # Data yang ingin di Update
            print("\n"+"="*100)
            print("Silahkan pilih data apa yang ingin anda ubah")
            print(f"1. Judul\t: {judul:.40}")
            print(f"2. Penulis\t: {penulis:.40}")
            print(f"3. Tahun\t: {tahun:4}")

        # Memilih mode untuk update
            user_option = input("Pilih data [1,2,3]: ")
            print("\n"+"="*100)
            match user_option:
                case "1": judul = input("Judul\t: ")
                case "2": penulis = input("Penulis\t: ")
                case "3": 
                    while(True):
                        try:
                            tahun = int(input("Tahun\t: "))
                            if len(str(tahun)) == 4:
                                break
                            else:
                                print("Tahun harus angka, silahkan masukan tahun lagi (yyyy)")
                        except:
                            print("Tahun harus angka, silahkan masukan tahun lagi (yyyy)")
                case _: print("index invalid")
        
            print("Data Baru Anda")
            print(f"1. Judul\t: {judul:.40}")
            print(f"2. Penulis\t: {penulis:.40}")
            print(f"3. Tahun\t: {tahun:4}")
            is_done = input("Apakah Selesai (y/n)? ")
            if is_done == "y" or is_done == "Y":
                break
    
        Operasi.update(no_buku,pk,data_add,tahun,judul,penulis)
    else:
        print(f"Data tidak valid: {data_break}")

def create_console():
    print("\n\n"+"="*100)
    print("Silahkan tambah data buku\n")
    penulis = input("Penulis\t: ")
    judul = input("Judul\t: ")
    while(True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun harus angka, silahkan masukan tahun lagi (yyyy)")
        except:
            print("Tahun harus angka, silahkan masukan tahun lagi (yyyy)")

    Operasi.create(tahun,judul,penulis)
    print("\nBerikut adalah data baru anda")
    read_console()

def read_console():
    data_file = Operasi.read()
    
    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    # Header
    print("\n"+"="*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-"*100)

    #Data
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        if len(data_break) >= 5:    
            pk = data_break[0]
            date_add = data_break[1]
            judul = data_break[2]
            penulis = data_break[3]
            tahun = data_break[4]
            print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}",end="")
        else:
            print(f"Data tidak valid: {data_break}")
    
    # Footer
    print("="*100+"\n")
