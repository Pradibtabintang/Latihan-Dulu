import os
import CRUD as CRUD
import emoji


if __name__ == "__main__":
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    print("HELLO STAFF STAR !!!😊\n")
    print("SELAMAT DATANG")
    print("Di UNISTAR LIBRARY\n")
    print("SELAMAT BEKERJA 🙌")
    print("=================================")

    # // Check database itu ada atau tidak
    CRUD.init_console()

    while(True):
        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")
        print("HELLO STAFF STAR !!!😊\n")
        print("SELAMAT DATANG")
        print("Di UNISTAR LIBRARY\n")
        print("SELAMAT BEKERJA 🙌")
        print("=================================")
        print(f"1. Read Data")
        print(f"2. Create Data")
        print(f"3. Update Data")
        print(f"4. Delate Data")

        user_option = input("Pilih Menu Yang Mana Kak ADMIN:")

        print("\n=================================\n")

        match user_option:
            case "1": print("Read Data")
            case "2": print("Create Data")
            case "3": print("Update Data")
            case "4": print("Delate Data")
            
        print("\n=================================\n")

        is_done = input("Ada yang ingin dikerjakan kembali KAKAK ADMIN (Ya/No)?")
        if is_done == "N" or is_done == "n" or is_done == "No" or is_done == "no":
            break

    print("PROGAM BERAKHIR, SELAMAT BERISTIRAHAT KAKAK ADMIN 👌")



    