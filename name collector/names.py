name_list = []
name = ""

def quit_detector():
    controller = input("Are we done? \n").lower()
    if controller == "1" or controller.startswith("yes") or controller == "quit" or controller.startswith("end") :
        return True
    else : 
        return False

def name_writer_to_screen():
    with open("names.txt", "r") as file :
        for line in file :
            clean_line = line.strip("\n") 
            if clean_line  not in name_list :
                name_list.append(clean_line)   

def name_writer_to_file(name):
    with open("names.txt", "a") as file :
            file.write(f"{name}\n")
while True:
    try :
        name = input("What's your name? \n")
        if quit_detector() == True :
            break
        name_writer_to_file(name)
    except EOFError :
        break

name_writer_to_screen()
print(sorted(name_list))

