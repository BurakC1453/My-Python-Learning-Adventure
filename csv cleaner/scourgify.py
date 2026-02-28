import sys
import csv

def main():
    if len(sys.argv) != 3:
        print("Usage: scourgify.py <input_file> <output_file>")
        sys.exit(1)
    try:
        with open(sys.argv[1], 'r') as infile:
            reader = csv.DictReader(infile)
            with open(sys.argv[2], 'w', newline='') as outfile:
                sutunlar = ["first","last","house"]
                writer = csv.DictWriter(outfile, fieldnames=sutunlar)
                writer.writeheader()
                for satir in reader:
                    isim_parcalari = satir["name"].split(",")
                    writer.writerow({
                        "first": isim_parcalari[1].strip(),
                        "last": isim_parcalari[0].strip(),
                        "house": satir["house"].strip()                        
                    })
    except FileNotFoundError:
        print(f"Error: File '{sys.argv[1]}' not found.")
        sys.exit(1)
    except IOError as e:
        print(f"Error reading file '{sys.argv[1]}': {e}")
        sys.exit(1)
    
if __name__ == "__main__":
    main()