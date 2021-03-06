#openweathermap.org sitesinden şehir sıcaklık verisi çekilecek.


#Api Call: http://api.openweathermap.org/data/2.5/weather?q=ankara&appid=24bb5a00705b2420901490c95519ab0b

import requests
import json
import cevir

sehir=input("Şehri Giriniz:")
sehirD=sehir.replace("i","İ").capitalize()
api_request=requests.get("http://api.openweathermap.org/data/"
                         "2.5/weather?q="+sehir+"&appid=24bb5a00705b2420901490c95519ab0b")

result= json.loads(api_request.content)

#print(result)

hava_sozluk={

    "Clouds":"Bulutlu",
    "Clear":"Açık",
    "Rain":"Yağmurlu"


}

print(sehirD+" sıcaklığı {} C".format(round(cevir.kelvin_to_celcius(result["main"]["temp"]),2)))
print(sehirD+"  sıcaklığı {} F".format(round(cevir.kelvin_to_fahrenheit(result["main"]["temp"]),2)))

print(sehirD+" Durumu: ", hava_sozluk[result["weather"][0]["main"]])