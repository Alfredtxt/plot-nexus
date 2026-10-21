import csv

# Update the path to the new complete catalog
file_path = 'data/catalogo_completo.csv'

print("--- PlotNexus: Dataset Explorer ---")

try:
    # Most Kaggle CSVs use a comma (,) as a delimiter instead of a semicolon (;)
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        
        # Read and print the headers (column names)
        headers = next(reader)
        print("\n📊 COLUMN HEADERS FOUND IN THE DATASET:")
        print(headers)
        print("-" * 50)
        
        # Read and print just the first 3 rows to see the data structure
        print("\n📚 FIRST 3 BOOKS:")
        for i in range(3):
            row = next(reader)
            # Printing only the first few elements to avoid massive text blocks
            print(f"Book {i+1}: {row[:4]}...") 
            
except FileNotFoundError:
    print("Error: Could not find 'catalogo_completo.csv' in the 'data' folder.")
except UnicodeDecodeError:
    print("Error: Encoding issue. The file might not be in standard UTF-8 format.")