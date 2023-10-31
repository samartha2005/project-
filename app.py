from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/youtube')
def scrape_youtube():
    # Scraping data from YouTube
    url = 'https://www.youtube.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract and display relevant data from YouTube (e.g., video titles)
    video_titles = [title.text for title in soup.find_all('h3', {'class': 'style-scope ytd-rich-grid-media'})]

    return render_template('youtube.html', video_titles=video_titles)

@app.route('/amazon')
def scrape_amazon():
    # Scraping data from Amazon
    search_query = request.args.get('query')
    url = f'https://www.amazon.com/s?k={search_query}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract and display relevant data from Amazon (e.g., product names)
    product_names = [name.text for name in soup.find_all('span', {'class': 'a-text-normal'})]

    return render_template('amazon.html', product_names=product_names)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
