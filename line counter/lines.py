import sys
def main():
    if len(sys.argv) > 2:
        print("Too many files to chech")
        return 1
    elif len(sys.argv) < 2:
        print("Too few files to check")
        return 1
    if sys.argv[1].endswith(".py") != 1:
        print("Not a Python file")
        return 1
    line_counter = 0
    name_of_file = sys.argv[1]
    try:
        with open(name_of_file) as file:
            for line in file:
                clean_line = line.strip()
                if clean_line.startswith("#") or clean_line == "":
                    continue
                else:
                    line_counter += 1
        print(f"{line_counter} lines")
    except FileNotFoundError:
        print("File not found")
        return 1
    

main()