from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>DevOps Lab Assignment 1</h1>
    <h2>Docker Container Running Successfully!</h2>
    <p>Registration Number: 055</p>
    <p>Semester: BSE-7</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)