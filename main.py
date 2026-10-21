from flask import Flask, render_template
import csv

# Initialize the Flask web application
app = Flask(__name__)

@app.route('/')
def home():
    """Route for the home page. Reads the catalog and sends it to the HTML template."""
    file_path = 'data/catalogo_arricchito.csv'
    books_list = []
    
    try:
        # Open our emotionally tagged database
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            # We'll extract only the first 21 books for the homepage grid
            # (to keep the page fast and beautiful)
            count = 0
            for book in reader:
                if count >= 21:
                    break
                books_list.append(book)
                count += 1
                
    except FileNotFoundError:
        print(f"Error: Could not find '{file_path}'.")
        
    # Render the index.html template, passing the books data to it
    return render_template('index.html', books=books_list)

if __name__ == '__main__':
    # Start the local web server with debug mode enabled
    print("--- PlotNexus Web Server Starting ---")
    app.run(debug=True)