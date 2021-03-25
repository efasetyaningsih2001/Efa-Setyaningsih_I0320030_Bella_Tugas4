#Spesifikasi usia = 21 dan telah lulus ujian kualifikasi
usia = 21
usia_siswa = int(input("Berapa usia kamu? : "))

if usia_siswa > usia:
    StatusUjian = input("Apakah Anda sudah lulus ujian kualifikasi (Y / T)? : ")
    if StatusUjian == "Y":
        print("Anda dapat mendaftar di kursus")
    elif StatusUjian != "Y":
        print("Anda tidak dapat mendaftar di kursus")
else :
    print("Anda tidak dapat mendaftar di kursus")



