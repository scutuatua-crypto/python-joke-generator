# 😂 Python Joke Generator

A fun Flask web application that fetches random jokes from [JokeAPI](https://jokeapi.dev/) and displays them in a beautiful, responsive UI.

## Features

- 🎲 Fetches random jokes from JokeAPI (safe, family-friendly categories)
- 😂 Displays both single-liner jokes and setup/delivery (two-part) jokes
- 🔄 "Get New Joke" button with smooth animations
- 📦 Offline fallback jokes if the API is unavailable
- 📱 Fully mobile-responsive design
- ⚡ Built with Python 3.8+, Flask, and Vanilla JavaScript

## Project Structure

```
python-joke-generator/
├── app.py               # Flask application (routes + API integration)
├── requirements.txt     # Python dependencies
├── templates/
│   └── index.html       # Main web interface
├── static/
│   ├── style.css        # Styling & animations
│   └── script.js        # Frontend JavaScript
├── .gitignore
└── README.md
```

## Setup & Running Locally

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/scutuatua-crypto/python-joke-generator.git
cd python-joke-generator

# 2. (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Flask development server
python app.py
```

Open your browser at **http://localhost:5000** and enjoy the jokes! 🎉

## Environment Variables

| Variable       | Default  | Description                              |
|----------------|----------|------------------------------------------|
| `PORT`         | `5000`   | Port the Flask server listens on         |
| `FLASK_DEBUG`  | `false`  | Set to `true` to enable debug/reload mode |

## Production Deployment

Use **Gunicorn** (included in `requirements.txt`) for production:

```bash
gunicorn app:app --bind 0.0.0.0:$PORT
```

## API Endpoint

| Endpoint     | Method | Description                        |
|--------------|--------|------------------------------------|
| `/`          | GET    | Serves the web interface           |
| `/api/joke`  | GET    | Returns a JSON joke object         |
| `/health`    | GET    | Health check (`{"status": "ok"}`)  |

### Example `/api/joke` Response

```json
{
  "joke": {
    "type": "twopart",
    "setup": "Why don't scientists trust atoms?",
    "delivery": "Because they make up everything!",
    "category": "Science",
    "source": "api"
  }
}
```

## Tech Stack

- **Backend:** Python 3.8+, Flask, Requests
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Joke Source:** [JokeAPI v2](https://jokeapi.dev/)

## License

MIT
