import random
import sys

def main():
    # 1. Seviyeyi al
    level = get_level()
    
    score = 0
    # 2. 10 Soru sor
    for _ in range(10):
        # Sayıları üret
        x = generate_integer(level)
        y = generate_integer(level)
        
        answer = x + y
        attempts = 0
        
        # 3. Her soru için 3 hak
        while attempts < 3:
            try:
                user_answer = input(f"{x} + {y} = ")
                if int(user_answer) == answer:
                    if attempts == 0 :
                        score += 1
                    else:
                        break # Doğru bildi, döngüyü kır
                else:
                    print("EEE")
                    attempts += 1
            except ValueError:
                print("EEE")
                attempts += 1
        
        # 3 hakkı da bittiyse doğrusunu göster
        if attempts == 3:
            print(f"{x} + {y} = {answer}")
            
    # 4. Final skoru
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]: # Liste içinde var mı kontrolü (Pythonic)
                return n
        except ValueError:
            continue # Hata verirse sessizce tekrar sor


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else: # Level 3
        return random.randint(100, 999)


if __name__ == "__main__":
    main()