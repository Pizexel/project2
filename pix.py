from flask import Flask, render_template, request

app = Flask(__name__)

# Set language for Wikipedia
wikipedia.set_lang("en")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query').lower()

    try:
        page = wikipedia.page(query)
        summary = page.summary
    except wikipedia.exceptions.DisambiguationError as e:
        summary = "Can you please be more specific?"
    except wikipedia.exceptions.PageError as e:
        summary = "Sorry, I could not find any information on that topic."

    return render_template('search.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)