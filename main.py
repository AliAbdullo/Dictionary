otam = {'ism':'abdumutal','t_yil':1971,'tuman':"Bo'z"}
print(F"Otamning ismi {otam['ism'].title()}, {otam['t_yil']}-yilda, {otam['tuman']}da tug'ilgan")

#Sevimli taomni aniqlash
taom = {'dadam':'palov','oyim':'mastava','Ali':'norin','Singlim':'osh','ukam':'kabop'}
print(f"Dadamning sevimli taomi {taom['dadam']}")

#Python
python = {
          'int':'butun son',
          'float':'xaqiyqiy son',
          'str':'matn',
          'append':'listga qiymat qo\'shadi',
          'title':'so\'z boshini katta xarf ',
          'upper':'ummumiy katta xarifga o\'zgartiradi',
         }
soz =input('Kalit so\'z kiriting: ').lower()
print(python.get(soz,"Bunday so'z mavjud emas!"))


