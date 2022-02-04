import flask
import os

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    html = """
    <h2>ENGINE Media Exchange (EMX)</h2>
    <p>If you have any questions please contact with us through web page</p>
    <p><a href="https://enginemediaexchange.com/contact/">Contact</a></p>
    """
    return html

if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 4004)))

