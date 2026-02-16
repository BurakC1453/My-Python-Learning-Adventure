def main():
    text = input("What is the text you want to get rid of the vowels? \n")
    print(shorten(text))

def shorten(text):
    text = text.replace("a","").replace("e","").replace("i","").replace("o","").replace("u","").replace("A","").replace("E","").replace("I","").replace("O","").replace("U","")
    return text

if __name__ == "__main__":
    main()