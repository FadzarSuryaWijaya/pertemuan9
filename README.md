# lab4py
# TUGAS PRAKTIKUM 4
## Latihan 1
- Input
# Membuat list dengan 5 elemen
    - my_list = [10, 20, 30, 40, 50]

## AKSES LIST
# Mengakses dan menampilkan elemen ke-3
    - print("Elemen ke-3:", my_list[2])

# Mengambil nilai elemen ke-2 sampai elemen ke-4
    - subset = my_list[1:4]
    - print("Elemen ke 2 sampai ke 4:", subset)
    
# Mengambil elemen terakhir
    - last_element = my_list[-1]
    - print("Elemen terakhir:", last_element)

## UBAH ELEMENT LIST
# ubah elemen ke 4 dengan nilai lainnya
    - my_list[3] = 45
    - print("List setelah mengubah elemen ke 4:", my_list)

# ubah elemen ke 4 sampai dengan elemen terakhir
    - my_list[3:] = [50, 60, 70]
    - print("List setelah mengubah elemen ke 4 sampai dengan elemen terakhir:", my_list)

## TAMBAH ELEMENT LIST
# Tambah elemen list
# Ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)
    - list_A = my_list[:2]
    - list_B = list_A.copy()

# Tambahkan list B dengan nilai string
    - B.append("Hello")

# Tambahkan list B dengan 3 nilai
    - list_B.extend([3, 6, 9])

# Gabungkan list B dengan list A
    - combined_list = list_B + list_A
    
# Tampilkan hasil
    - print("List A:", list_A)
    - print("List B:", list_B)
    - print("Gabungan List B dengan List A:", combined_list)

## Output



## Penjelasan

# TUGAS PRAKTIKUM 4
## Latihan 1
- Input
# Membuat list dengan 5 elemen
    - my_list = [10, 20, 30, 40, 50]

## AKSES LIST
# Mengakses dan menampilkan elemen ke-3
    - print("Elemen ke-3:", my_list[2])

# Mengambil nilai elemen ke-2 sampai elemen ke-4
    - subset = my_list[1:4]
    - print("Elemen ke 2 sampai ke 4:", subset)
    
# Mengambil elemen terakhir
    - last_element = my_list[-1]
    - print("Elemen terakhir:", last_element)

## UBAH ELEMENT LIST
# ubah elemen ke 4 dengan nilai lainnya
    - my_list[3] = 45
    - print("List setelah mengubah elemen ke 4:", my_list)

# ubah elemen ke 4 sampai dengan elemen terakhir
    - my_list[3:] = [50, 60, 70]
    - print("List setelah mengubah elemen ke 4 sampai dengan elemen terakhir:", my_list)

## TAMBAH ELEMENT LIST
# Tambah elemen list
# Ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)
    - list_A = my_list[:2]
    - list_B = list_A.copy()

# Tambahkan list B dengan nilai string
    - B.append("Hello")

# Tambahkan list B dengan 3 nilai
    - list_B.extend([3, 6, 9])

# Gabungkan list B dengan list A
    - combined_list = list_B + list_A
    
# Tampilkan hasil
    - print("List A:", list_A)
    - print("List B:", list_B)
    - print("Gabungan List B dengan List A:", combined_list)

## Output



## Penjelasan

1. List pertama (list_A) diinisialisasi dengan nilai [1, 2, 3, 4, 5].
2. Dua bagian pertama dari list_A diambil dan disalin ke list_B menggunakan slicing (list_A[:2]).
3. Tiga nilai string ("string1" dan "string2") ditambahkan ke list_B menggunakan metode append.
4. Tiga nilai (3, 4, dan 5) ditambahkan ke list_B menggunakan metode extend.
5. List B (list_B) sekarang berisi dua bagian pertama dari list A, dua nilai string, dan tiga nilai tambahan.
6. List B (list_B) kemudian digabungkan ke list A (list_A) menggunakan metode extend.
7. Hasilnya dicetak untuk dilihat.

## Praktikum 4

## Input



# LIST
    print("\nMasukkan data mahasiswa:")
    nama = input("Nama        : ")
    nim = int(input("NIM         : "))
    nilai_tugas = int(input("Nilai Tugas : "))
    nilai_uts = int(input("Nilai UTS   : "))
    nilai_uas = int(input("Nilai UAS   : "))

# Input
    data_mahasiswa.append({
        'Nama': nama,
        'NIM': nim,
        'Nilai Tugas': nilai_tugas,
        'Nilai UTS': nilai_uts,
        'Nilai UAS': nilai_uas,
        'Nilai Akhir': nilai_akhir
    })

    tambah_data = input("\nTambah Data(y/t)? ").lower()
    if tambah_data != 'y':
        break

# Output

    print("\n{:=^85}".format(""))
    print("| No | {:<21} | {:^10} | {:^15} | {:^5} | {:^5} | {:^5} |".format("Nama", "NIM", "Tugas", "UTS", "UAS", "Akhir"))
    print("{:=^85}".format(""))

    for idx, mahasiswa in enumerate(data_mahasiswa, start=1):
    print("| {:<2} | {:<10} | {:^10} | {:^15} | {:^5} | {:^5} | {:.2f} |".format(idx, mahasiswa['Nama'], mahasiswa['NIM'],
                                                                                    mahasiswa['Nilai Tugas'], mahasiswa['Nilai UTS'],
                                                                                    mahasiswa['Nilai UAS'], mahasiswa['Nilai Akhir']))
    print("{:=^85}".format(""))


## Output



## Flowchart



## Penjelasan

1. Program dimulai dengan menginisialisasi list data_mahasiswa untuk menyimpan data mahasiswa.
2. Didefinisikan fungsi hitung_nilai_akhir untuk menghitung nilai akhir berdasarkan proporsi yang diberikan.
3. Program menggunakan perulangan while True untuk terus meminta input data.
4. Pengguna diminta untuk memasukkan nama, nilai tugas, nilai UTS, dan nilai UAS.
5. Nilai akhir dihitung menggunakan fungsi hitung_nilai_akhir dan data dimasukkan ke dalam list.
6. Program menanyakan apakah pengguna ingin menambahkan data lagi, dan perulangan berlanjut jika jawabannya 'y'.
7. Setelah selesai memasukkan data, program menampilkan daftar data mahasiswa dalam format tabel sederhana.

