tahta = [[" _1_ ", " _2_ ", " _3_ "], [" _4_ ", " _5_ ", " _6_ "], [" _7_ ", " _8_ ", " _9_ "]]


oyuncunun_isareti = "  O  "
bilgisayarin_isareti = "  X  "
hamle_sirasi = 0
yersecenek = [1, 2, 3, 4, 5, 6, 7, 8, 9]
while True:
    print("\n" * 3)
    for i in tahta:
        print("\t".expandtabs(30), *i, end="\n" * 3)

    if yersecenek == []:
        print("oyun bitti####")
        if [tahta[0][0], tahta[1][1], tahta[2][2]] == ["  O  ", "  O  ", "  O  "]:
            print('OYUNU KAZANDINIZ###')

        elif [tahta[0][2], tahta[1][1], tahta[2][0]] == ["  O  ", "  O  ", "  O  "]:
            print('OYUNU KAZANDINIZ###')

        break


#oyuncu oyunu ancak caprazdan kazanabilir.digerlerine bilgisayar izin vermeyecektir.capraz kontrolu-------
    elif [tahta[0][0],tahta[1][1],tahta[2][2]]==["  O  ","  O  ","  O  "]:
        print('OYUNU KAZANDINIZ###')
        break
    elif [tahta[0][2], tahta[1][1], tahta[2][0]] == ["  O  ", "  O  ", "  O  "]:
        print('OYUNU KAZANDINIZ###')
        break
#--------------------------------------


    elif hamle_sirasi % 2 == 0:  # cift sirali hamle sirasi oyuncunun,tek hamle sayisi bilgisayarin
        isaret = oyuncunun_isareti
        print(yersecenek, "den")
        yer = int(input("bir konum sec:"))

        if yer not in yersecenek:
            print(
                "bos olan yerlerden tercih yapiniz..")  # daha once hamle yapilan yerler ya da yanlis rakam harf girisi


        else:
            yersecenek.remove(yer)  # yapilan secimden dolayi kullanilan haneyi iptal et.burasi tekrar kullanilamaz
            x = (yer - 1) // 3  # bu kisim tablodaki yatay satir numarasini bulmak icin
            y = (
                            yer - 1) % 3  # bu kisim tablodaki dusey sutun numarasini bulmak icin(tektek iflerle yazilinca 9 if gerekli
            hamle_sirasi += 1  # hamle sayisi bir artinca tek sayi oldu ve sirayi bilgisayara verecek
            tahta[x][y] = isaret  # hamle sirasi oyuncuda oyuzden O isareti konulacak



    elif hamle_sirasi % 2 == 1:  # bu kisim bilgisayara sira geldiginde nasil davranacagini acikliyor
        isaret = bilgisayarin_isareti  # bilgisayar oynarken isaret X
        print("bilgisayarin hamlesi...")

#0.satir kontrolu------------------
        if tahta[0].count(oyuncunun_isareti) == 2 and tahta[0].count(bilgisayarin_isareti) == 0:  # 0.satirda iki tane O varsa karsi hamle asagida: bos sutun bul

            for i in [0, 1, 2]:
                if tahta[0][i] != oyuncunun_isareti:        #0.satirda iki tane O vardi kalan bosu bul
                    tahta[0][i] = bilgisayarin_isareti      #bos olan yere bilgisayarin isaretini koy
                    hamle_sirasi += 1                       #hamle sirasini 1 artir sira oyuncuya gecsin
                    yer = (3 * 0 + i) + 1                   #doldurulan yerin tabloda numarasi nedir
                    yersecenek.remove(yer)                  #bu yere bir daha hamle yapilamaz.seceneklerden cikar
                    break

#1.satir kontrolu-------------------
        elif tahta[1].count(oyuncunun_isareti) == 2 and tahta[1].count(bilgisayarin_isareti) == 0:  # 1.satirda iki tane O varsa karsi hamle asagida: bos sutun bul

            for i in [0, 1, 2]:

                if tahta[1][i] != oyuncunun_isareti:                #1.satirda iki tane O vardi kalan bosu bul
                    tahta[1][i] = bilgisayarin_isareti              #bos olan yere bilgisayarin isaretini koy
                    hamle_sirasi += 1                               #hamle sirasini 1 artir sira oyuncuya gecsin
                    yer = (3 * 1 + i) + 1                           #doldurulan yerin tabloda numarasi nedir
                    yersecenek.remove(yer)                          #bu yere bir daha hamle yapilamaz.seceneklerden cikar
                    break

#2.satir kontrolu---------------------
        elif tahta[2].count(oyuncunun_isareti) == 2 and tahta[2].count(bilgisayarin_isareti) == 0:  # 2.satirda iki tane O varsa karsi hamle asagida: bos sutun bul


            for i in [0,1,2]:
                if tahta[2][i]!=oyuncunun_isareti:              #2.satirda iki tane O vardi kalan bosu bul...
                    tahta[2][i]=bilgisayarin_isareti
                    hamle_sirasi += 1
                    yer = (3 * 2 + i) + 1
                    yersecenek.remove(yer)
                    break

#0.sutun kontrolu-----------------
        elif [tahta[0][0],tahta[1][0],tahta[2][0]].count(oyuncunun_isareti)==2 and [tahta[0][0],tahta[1][0],tahta[2][0]].count(bilgisayarin_isareti) == 0:

            for i in [0,1,2]:
                if tahta[i][0]!=oyuncunun_isareti:              #0.sutunda iki tane O vardi kalan bosu bul...
                    tahta[i][0]=bilgisayarin_isareti            #bu sutunda bos olan haneye bilgisayar isaret koysun
                    hamle_sirasi += 1                           ##hamle sirasini 1 artir sira oyuncuya gecsin
                    yer = (3 * i + 0) + 1                       #doldurulan yerin tabloda numarasi nedir
                    yersecenek.remove(yer)                      #bu yere bir daha hamle yapilamaz.seceneklerden cikar
                    break

#1.sutun kontrolu----------------------
        elif [tahta[0][1], tahta[1][1], tahta[2][1]].count(oyuncunun_isareti) == 2 and [tahta[0][1], tahta[1][1],
                                                                                        tahta[2][1]].count(
                bilgisayarin_isareti) == 0:

            for i in [0, 1, 2]:
                if tahta[i][1] != oyuncunun_isareti:  # 1.sutunda iki tane O vardi kalan bosu bul...
                    tahta[i][1] = bilgisayarin_isareti  # bu sutunda bos olan haneye bilgisayar isaret koysun
                    hamle_sirasi += 1  ##hamle sirasini 1 artir sira oyuncuya gecsin
                    yer = (3 * i + 1) + 1  # doldurulan yerin tabloda numarasi nedir
                    yersecenek.remove(yer)  # bu yere bir daha hamle yapilamaz.seceneklerden cikar
                    break

# 2.sutun kontrolu----------------------
        elif [tahta[0][2], tahta[1][2], tahta[2][2]].count(oyuncunun_isareti) == 2 and [tahta[0][2], tahta[1][2],
                                                                                        tahta[2][2]].count(
            bilgisayarin_isareti) == 0:

            for i in [0, 1, 2]:
                if tahta[i][2] != oyuncunun_isareti:  # 2.sutunda iki tane O vardi kalan bosu bul...
                    tahta[i][2] = bilgisayarin_isareti  # bu sutunda bos olan haneye bilgisayar isaret koysun
                    hamle_sirasi += 1  ##hamle sirasini 1 artir sira oyuncuya gecsin
                    yer = (3 * i + 2) + 1  # doldurulan yerin tabloda numarasi nedir
                    yersecenek.remove(yer)  # bu yere bir daha hamle yapilamaz.seceneklerden cikar
                    break
#capraz kontrollerini yapmadim.oyuncu ancak capraz oyun oynarsa kazanabilir.(eger kontrol yapacak olsaydim yine elle
#tektek yazardim.kisa yolunu bulamadim.ya da guzel calismadi

        else:
            import random

            yer = random.choice(yersecenek)  # hamle yapilmamis olan kisimlar listesinden bir konum sececek
            x = (yer - 1) // 3  # secilen konumun satiri
            y = (yer - 1) % 3  # secilen konumun sutunu
            tahta[x][y] = isaret  # secilen konuma X isareti yerlestirildi
            yersecenek.remove(yer)  # artik bu konum doldugu icin bos konumlar listesinden silindi
            hamle_sirasi += 1  # hamle sirasi 1 atinca cift sayili hamle oldu.sira oyuncuya gecti



