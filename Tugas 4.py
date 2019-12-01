data=[]
nomor = 0
while(True) :
    nim=input("Masukkan nim   : ")
    nama=input("Masukkan nama : ")
    tugas=int(input("Masukan tugas: "))
    uts=int(input("Masukan uts : "))
    uas=int(input("Masukkan uas: "))
    akhir=(tugas*.3 + uts*.35 + uas*.35)
    nomor+=1
    data.append([nomor, nim, nama, tugas, uts, uas, akhir])
    ulangi=input("Tambah data (y/t)?")
    if ulangi.lower() == 't':
        break;

print("\nDaftar Nama\n")
print("================================================================")
print("|  NOMOR  |  NIM  |  NAMA  |  TUGAS  |  UTS  |  UAS  |  AKHIR | ")
print("================================================================")
for x in data:
    print("|   {0:4d}  | {1:6s} | {2:7s} | {3:5d} | {4:5d} | {5:5d} | {6}   |".format(x[0], x[1], x[2], x[3], x[4], x[5], x[6]))
