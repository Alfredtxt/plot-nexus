from flask import Flask, render_template
import csv

# Initialize the Flask web application
app = Flask(__name__)

@app.route('/')
def home():
    """Route for the cozy, magical Home Page (Entrance Hall)."""
    return render_template('index.html')

@app.route('/biblioteca')
def biblioteca():
    """Route for the Catalog Page, displaying the 10 emotional sections."""
    # We define the 10 main emotional sections
    emotions = [
        {'name': 'Romance', 'desc': 'Stories of love, passion, and deep connections'},
        {'name': 'Suspense', 'desc': 'Thrilling tales that keep you on the edge of your seat'},
        {'name': 'Wonder', 'desc': 'Magic, fantasy, and impossible worlds'},
        {'name': 'Humor', 'desc': 'Lighthearted, witty, and funny adventures'},
        {'name': 'Dark', 'desc': 'Explore the shadows, the macabre, and the unknown'},
        {'name': 'Awe', 'desc': 'Mind-bending sci-fi and visions of the future'},
        {'name': 'Heartwarming', 'desc': 'Feel-good stories of family, hope, and friendship'},
        {'name': 'Intrigue', 'desc': 'Mysteries, hidden secrets, and complex puzzles'},
        {'name': 'Melancholy', 'desc': 'Reflective, tear-jerking, and poetic journeys'},
        {'name': 'Reflective', 'desc': 'Deep thoughts, philosophy, and inner growth'}
    ]
    return render_template('biblioteca.html', emotions=emotions)

@app.route('/biblioteca/<emotion_name>')
def emotion_section(emotion_name):
    """Dynamic route that loads hundreds of books for a specific emotion."""
    file_path = 'data/catalogo_arricchito.csv'
    books_in_emotion = []
    
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            # We load up to 300 books for this specific emotion
            count = 0
            for book in reader:
                # Extract the tags string
                tags_string = book.get('emotion_tags', 'Reflective')
                
                # Clean and split the tags into a list
                tags = [tag.strip() for tag in tags_string.split(',') if tag.strip()]
                
                # If the requested emotion is in the book's tags, add it to our list
                if emotion_name in tags:
                    books_in_emotion.append(book)
                    count += 1
                    if count >= 300: # Safety limit for the browser
                        break
                        
    except FileNotFoundError:
        print(f"Error: Could not find '{file_path}'.")
        
    return render_template('emotion_books.html', books=books_in_emotion, emotion=emotion_name)

@app.route('/nexus')
def nexus():
    """Route for the Nexus AI chat interface."""
    return render_template('nexus.html')

if __name__ == '__main__':
    # Start the local web server with debug mode enabled
    print("--- PlotNexus Magical Server Starting ---")
    app.run(debug=True)