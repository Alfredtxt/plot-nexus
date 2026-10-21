import csv

file_path = 'data/catalogo_completo.csv'

print("--- PlotNexus: Data Extraction ---")

try:
    with open(file_path, mode='r', encoding='utf-8') as file:
        # DictReader maps the information read into a dictionary whose keys are the column headers
        reader = csv.DictReader(file)
        
        print("\n📚 FIRST 3 BOOKS EXTRACTED:")
        for i in range(3):
            try:
                book = next(reader)
                print(f"\n📖 Book {i+1}: {book['title']}")
                print(f"👤 Author: {book['author']}")
                # Printing only the first 150 characters of the description to keep the terminal clean
                print(f"📝 Plot: {book['description'][:150]}...")
            except StopIteration:
                break
                
except FileNotFoundError:
    print("Error: Could not find 'catalogo_completo.csv'.")