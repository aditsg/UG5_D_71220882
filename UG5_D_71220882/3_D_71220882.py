import math


jarak_awal = int(input('masukan jarak awal (dalam meter) : '))

if jarak_awal == 'stop':
    print("program dihentikan")
        
ke_5 = int(input('masukan sudut elevasi pada menit ke-5 (dalam derajat) : '))
ke_6 = int(input('masukan sudut elevasi pada menit ke-6 (dalam derajat) : '))
rumus = jarak_awal * math.tan(ke_5)
rumus2 = jarak_awal * math.tan(ke_6) - (ke_5)
rumus1 = rumus2 * math.tan(ke_6)

print('ketinggian drone pada menit ke-5 adalam',rumus,'meter')
print('selisih ketinggian drone saat menit ke-5 dan ke-8 adalah',rumus1)







