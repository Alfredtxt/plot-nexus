import csv

input_file = 'data/catalogo_completo.csv'
output_file = 'data/catalogo_arricchito.csv'

# Dictionary for Nexus AI emotion simulation
emotion_keywords = {
    'love': 'Romance',
    'murder': 'Suspense',
    'magic': 'Wonder',
    'war': 'Anguish',
    'funny': 'Humor',
    'dark': 'Dark',
    'future': 'Awe',
    'family': 'Heartwarming',
    'mystery': 'Intrigue',
    'death': 'Melancholy'
}

def extract_emotions(description):
    """Analyzes the plot and returns emotional tags based on keywords."""
    tags = []
    if not description:
        return "Reflective"
        
    desc_lower = description.lower()
    
    for keyword, emotion in emotion_keywords.items():
        if keyword in desc_lower:
            tags.append(emotion)
    
    if not tags:
        tags.append('Reflective') 
        
    return ", ".join(tags)

print("--- PlotNexus: Starting Full Data Pipeline ---")

try:
    with open(input_file, mode='r', encoding='utf-8') as infile, \
         open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
        
        reader = csv.DictReader(infile)
        
        fieldnames = reader.fieldnames + ['emotion_tags']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        print("Analyzing books and generating emotions for the ENTIRE catalog...")
        print("This might take a few moments. Please wait...\n")
        
        count = 0
        for book in reader:
            book['emotion_tags'] = extract_emotions(book['description'])
            writer.writerow(book)
            count += 1
            
            # Print a progress update every 10,000 books
            if count % 10000 == 0:
                print(f"Processed {count} books...")
                
    print(f"\nSuccess! All {count} books have been emotionally tagged.")
    print("Your complete 'catalogo_arricchito.csv' is ready!")
    
except FileNotFoundError:
    print(f"Error: Could not find '{input_file}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")