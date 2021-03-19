dict ={'Nama': 'Retno Murwati',
       'Hobi': ['Menonton film', 'Mendengarkan musik', 'Memasak'],
       'Social Media': ['Instagram : @retn0_', 'Twitter : inisyalRe', 'Line : Re25068664'],
       'Lagu Kesukaan':['For life', 'What U Do', 'Peterpan'],
       'Makanan Favorit': ['Pempek', 'Mie Ayam', 'Roti Bakar']}
print(dict)

#Mengubah Salah Satu Hobi dan Sosial Media
dict['Hobi'][1] = ('Membaca')
dict['Social Media'][2] = ('ID Telegram : @inisyalRe')

#Menghapus Dua Makanan Favorit
del dict['Makanan Favorit'][0:2]

#Menambahkan Satu Hobi
dict['Hobi'].append('Makan')
print(dict)
