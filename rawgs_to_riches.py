from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Rawgs to Riches"

if __name__ == '__main__':
    app.run()
