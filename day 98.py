print("cara menggunakan break and continue dalam perulangan for")
print("menggunakan break")
for nilai in range(10):
    if nilai == 5:
      break
    print(nilai)
#penjelasannya: break artinya di sini adalah kita menghentikan secara paksa dari perulangan
#yang kita jalankan. oleh karena itu apa bila kita ingin di dalam perululangan tidak menampilkan
#semua nilai dari batsannya kita dapat menggunakan break
print("menggunakan continue")
for nilai in range(10):
    if nilai == 5:
      continue
    print(nilai)
#penpenjelasannya : continue artinya adalah kita menskip nilai dari yang di jalankan,jadi
    #apabila kita ingin di dalam perulangan kita tidak ingin menampilakan angka 5 maka kita
    #dapat mengginakan continue
print("for yang menggunakan list")
nama=["naya","awal","dina","lisa","luppi","salsa"]
for isi in(nama):
    print(isi)