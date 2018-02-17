# scrapy
scrapy ile İHA ekonomi haberlerini çekme
scrapy aracı ile İHA haber sitesindeki ekonomi haberlerine ait başlıkları bir csv dosyasına kaydedilmiştir. 
Web üzerinden bilgiye erişim dersi için örnek uygulamadır.
çalıştırmak için 
#scrapy crawl iha -o data.csv

iha: spider adı
-o data.csv : çıktı datasının nasıl kaydedileceği. istenirse json olarak da alınabilir.

spider dizininde bulunan ekonomi.py dosyasını kendinize göre düzenleyebilir farklı sitelerden css kurallarına dikkat ederek veri çekebilirsiniz.
