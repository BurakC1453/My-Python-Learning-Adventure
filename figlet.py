import sys
import random
from pyfiglet import Figlet # type: ignore 

def main():
    figlet = Figlet()
    available_fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        # Senaryo 1: Kullanıcı sadece dosya adını yazdıysa rastgele font seç
        selected_font = random.choice(available_fonts)
    
    elif len(sys.argv) == 3:
        # Senaryo 2: Kullanıcı -f veya --font ile font adı girdiyse
        is_flag_correct = sys.argv[1] == "-f" or sys.argv[1] == "--font"
        is_font_valid = sys.argv[2] in available_fonts
        
        if is_flag_correct and is_font_valid:
            selected_font = sys.argv[2]
        else:
            # Bayrak yanlışsa veya font listede yoksa programı kapat
            sys.exit("Invalid usage")
            
    else:
        # Senaryo 3: Argüman sayısı 1 veya 3 değilse (2 veya 4+ ise) hata ver
        sys.exit("Invalid usage")

    # Kullanıcıdan mesajı alıyoruz
    text = input("Input: ")

    # Seçtiğimiz fontu sisteme tanımlıyoruz
    figlet.setFont(font=selected_font)
    
    # Metni ASCII sanatına dönüştürüp ekrana basıyoruz
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()