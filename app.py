from flask import Flask, render_template, request, redirect
import random
import string

app = Flask(__name__)

# A dictionary to store the original and shortened URLs
url_mapping = {}

def generate_short_url():
    """Generate a random 6-character string for the short URL."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['url']
        short_url = generate_short_url()

        # Map the short URL to the original URL
        url_mapping[short_url] = original_url

        return render_template('index.html', short_url=short_url)
    
    return render_template('index.html')

@app.route('/<short_url>')
def redirect_to_url(short_url):
    """Redirect the user to the original URL if the short URL exists."""
    original_url = url_mapping.get(short_url)
    if original_url:
        return redirect(original_url)
    return "Invalid URL", 404

if __name__ == '__main__':
    app.run(debug=True)
