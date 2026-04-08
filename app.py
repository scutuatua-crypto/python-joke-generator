import os
import random

import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOKEAPI_URL = "https://v2.jokeapi.dev/joke/Any"
JOKEAPI_PARAMS = {
    "blacklistFlags": "nsfw,racist,sexist,explicit",
    "type": "single,twopart",
}

FALLBACK_JOKES = [
    {
        "type": "single",
        "joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
    },
    {
        "type": "twopart",
        "setup": "Why don't scientists trust atoms?",
        "delivery": "Because they make up everything!",
    },
    {
        "type": "single",
        "joke": "I told my computer I needed a break. Now it won't stop sending me Kit Kat ads.",
    },
    {
        "type": "twopart",
        "setup": "Why did the scarecrow win an award?",
        "delivery": "Because he was outstanding in his field!",
    },
    {
        "type": "single",
        "joke": "A SQL query walks into a bar, walks up to two tables and asks... 'Can I join you?'",
    },
    {
        "type": "twopart",
        "setup": "How many programmers does it take to change a light bulb?",
        "delivery": "None, that's a hardware problem.",
    },
    {
        "type": "single",
        "joke": "I asked my dog what two minus two is. He said nothing.",
    },
    {
        "type": "twopart",
        "setup": "Why do cows wear bells?",
        "delivery": "Because their horns don't work!",
    },
]


def get_fallback_joke():
    """Return a random fallback joke."""
    joke = dict(random.choice(FALLBACK_JOKES))
    joke["source"] = "fallback"
    return {"joke": joke}


@app.route("/")
def index():
    """Serve the main web interface."""
    return render_template("index.html")


@app.route("/api/joke")
def get_joke():
    """Fetch a random joke from JokeAPI, falling back to local jokes on error."""
    try:
        response = requests.get(JOKEAPI_URL, params=JOKEAPI_PARAMS, timeout=5)
        response.raise_for_status()
        data = response.json()

        if data.get("error"):
            return jsonify(get_fallback_joke())

        joke_data = {
            "type": data.get("type"),
            "category": data.get("category", ""),
            "source": "api",
        }

        if data["type"] == "single":
            joke_data["joke"] = data.get("joke", "")
        else:
            joke_data["setup"] = data.get("setup", "")
            joke_data["delivery"] = data.get("delivery", "")

        return jsonify({"joke": joke_data})

    except requests.exceptions.Timeout:
        return jsonify(get_fallback_joke())
    except requests.exceptions.ConnectionError:
        return jsonify(get_fallback_joke())
    except requests.exceptions.RequestException:
        return jsonify(get_fallback_joke())
    except Exception:
        return jsonify(get_fallback_joke())


@app.route("/health")
def health():
    """Simple health check endpoint."""
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    debug = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=debug, host="0.0.0.0", port=port)
