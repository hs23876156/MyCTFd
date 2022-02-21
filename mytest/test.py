from flask import Flask


if __name__ == '__main__':

    app = Flask(__name__)
    @app.route("/")
    def hello():
        return "Hello, World!"
    
    app.run(host="0.0.0.0", port=7000)

    print("GG inin der!!!")

