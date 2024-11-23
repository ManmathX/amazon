from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
import random

app = Flask(__name__)

# Function to get a random video link
def get_random_video():
    url = "https://example.com"  # Replace with the target website
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract video links
    video_links = [tag['href'] for tag in soup.find_all("a", href=True) if tag['href'].endswith((".mp4", ".webm", ".avi"))]

    # Return a random video link
    return random.choice(video_links) if video_links else None

# Route to render the HTML page
@app.route("/")
def index():
    return render_template("index.html")  # Make sure you have an index.html file in a "templates" folder

# Route to get a random video link
@app.route("/get-video", methods=["GET"])
def get_video():
    video_link = get_random_video()
    if video_link:
        return jsonify({"video_link": video_link})
    return jsonify({"error": "No video links found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
