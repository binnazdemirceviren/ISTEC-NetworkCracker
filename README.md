# ISTEC-WirelessCracker
  
  Wireless Cracker ile Deauthentication saldırısı kolay ve otonom bir şekilde gerçekleştirilir. Wireless Cracker aircrack-ng ailesindeki tooların(airmon-ng, airodump-ng, aireplay-ng, aircrack-ng) otonom bir şekilde kullanılmasını sağlamaktadır. 


## Adımları
  
  Program çalıştıktan sonra otonom bir şekilde sırayla aşağıdaki işlemler gerçekleşmektedir.
  
  * Ağ kartını belirtir ve ağ kartını monitor moda alır.
  * Monitor moda alınan ağ kartının ismi tutar.
  * Etraftaki ağlar tarar.
  * Öncesinde belirlediğimiz BSSID listesindeki(input.csv) ağlardan handshake yakalar.
  * Yakalanan handshakelere, belirlediğimiz wordlistler kullanılarak brute-force saldırı gerçekleştirir
  * Parolalar txt'ye yazdırır
  * Monitor modu durdurur.


  
  
  
