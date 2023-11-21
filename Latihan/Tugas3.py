# Tambah list element
lista  = [1, 2, 3, 4, 5]
print("ListA\n", lista)
listb  = [6, 7, 8]
print("ListB Sebelum di tambahkan :\n", listb, "\n")

lista  = [1 ,2 ,3 ,4 ,5]
print("ListA\n", lista)
listb  = [6 ,7 ,8 ]
listb.insert(2,lista[0:2])  
print("ListB Sesudah di tambahkan :\n", listb, "\n")

# Menambahkan list B dengan nilai string
listb.append("String")
print("ListB :\n", listb,"\n")

# Menambahkan list B dengan 3 Nilai
listb.extend([10, 12, 14])
print("Mendambahkan ListB dengan 3 nilai :\n", listb,"\n")

# Menggabungkan ListA dan ListB 
listN = lista + listb
print("Gabungan listA & ListB: \n", listN)
