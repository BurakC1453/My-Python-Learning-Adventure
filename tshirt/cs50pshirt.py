import sys
import os
from PIL import Image, ImageOps

def main():
    # 1. ARGÜMAN SAYISI KONTROLÜ
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # 2. UZANTI AYIKLAMA VE KONTROLÜ
    _, uzanti1 = os.path.splitext(sys.argv[1].lower())
    _, uzanti2 = os.path.splitext(sys.argv[2].lower())
    
    gecerli_uzantilar = [".jpg", ".jpeg", ".png"]

    # Uzantı geçerli mi?
    if uzanti1 not in gecerli_uzantilar or uzanti2 not in gecerli_uzantilar:
        sys.exit("Invalid output")

    # İki dosyanın uzantısı birbiriyle eşleşiyor mu?
    if uzanti1 != uzanti2:
        sys.exit("Input and output have different extensions")

    # 3. ASIL ŞOV: GÖRÜNTÜ İŞLEME VE GİYDİRME
    try:
        # Şeffaf tişörtümüzü açıyoruz ve boyutunu alıyoruz
        shirt = Image.open("shirt.png")
        boyut = shirt.size

        # Kullanıcının verdiği fotoğrafı açıyoruz
        with Image.open(sys.argv[1]) as photo:
            
            # Fotoğrafı tam olarak tişörtün boyutuna göre ortalayarak kırpıyoruz
            photo = ImageOps.fit(photo, boyut)
            
            # Tişörtü fotoğrafın üzerine yapıştırıyoruz (İkinci 'shirt' arka planı şeffaf yapar)
            photo.paste(shirt, shirt)
            
            # Yeni oluşan şaheseri kaydediyoruz
            photo.save(sys.argv[2])
            
    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()