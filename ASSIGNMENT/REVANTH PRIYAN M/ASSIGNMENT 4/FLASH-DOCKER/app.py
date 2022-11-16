from flask import Flask
app = Flask(__name__)

@app.route('/')
def Home():
    return "Hello Docker!"

if __name__ == "__main__":
    app.run(debug=True)