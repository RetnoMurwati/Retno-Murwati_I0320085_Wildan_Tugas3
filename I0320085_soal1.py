#Membuat list teman
list_teman = ['Ica', 'Sylvia', 'Uli', 'Sekar', 'Raysa', 'Alvin', 'Zedi', 'Yuki', 'Divana', 'Hanna']

#Menampilkan list pada index 4,6,7
print("Nama pada index 4 :", list_teman[4])
print("Nama pada index 6 :", list_teman[6])
print("Nama pada index 7 :", list_teman[7])

#Mengganti nama pada list 3,5,9
list_teman[3] = 'Dessy'
list_teman[5] = 'Salma'
list_teman[9] = 'Alfina'

#Menambah dua teman baru
list_teman.extend(['Salsa', 'Nenda'])

#Menampilkan semua teman dengan perulangan
urutan = 0
for data in range(0,12):
    print(list_teman[urutan])
    urutan = urutan + 1

#Menampilkan panjang list
print(len(list_teman))


