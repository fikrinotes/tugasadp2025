nilai = float(input('masukkan nilai rata-rata: '))

if nilai > 95:
    print('''kategori: 
          1. memiliki prestasi akademik
          2. tidak memili prestsi akademik''')
    kategori = int(input('masukkan kategori: '))
    if kategori == 1:
        print('mendapatkan beasiswa full 100%')
    else:
        print('tidak mendapatkan beasiswa full 100%')
elif 90<=nilai<=95:
    print('''kategori: 
          1. memiliki prestasi akademik
          2. tidak memili prestsi akademik''')
    kategori = int(input('masukkan kategori: '))
    if kategori == 1:
        print('mendapatkan beasiswa 75%')
    else:
        print('mendapatkan beasiswa 50%')
else:
    print('tidak layak mendapatkan beasiswa')

        