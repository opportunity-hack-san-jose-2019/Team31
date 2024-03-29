from flask import Flask

app = Flask(__name__, static_folder='static', template_folder='templates')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
