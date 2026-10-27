
from flask import Flask, request
from html import escape
from pathlib import Path
import os

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        file = request.files.get("document")

        if file and file.filename:
            filename = escape(Path(file.filename).name)
            message = f"<p>Selected file: {filename}</p>"
        else:
            message = "<p>Please select a document.</p>"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Python Application</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f0f4f8;
                padding: 40px 15px;
            }}
            main {{
                max-width: 500px;
                margin: auto;
                background: white;
                padding: 30px;
                border-radius: 12px;
            }}
            button {{
                background: #0080ff;
                color: white;
                padding: 10px 18px;
                border: 0;
                border-radius: 6px;
                cursor: pointer;
            }}
        </style>
    </head>
    <body>
        <main>
            <h1>My Python Application</h1>
            <h2>Full Name: Aynur Hüseynova</h2>
            <h3>Group: CE-204</h3>
            <hr>
            <h3>Upload a Document</h3>
            <form method="POST" enctype="multipart/form-data">
                <input type="file" name="document" required>
                <br><br>
                <button type="submit">Submit</button>
            </form>
            {message}
        </main>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080))
    )
