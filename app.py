'''
Here's some comments that I'm going to try to commit to both the local repo
and the GitHub master branch.
'''
from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/hello")
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    app.run()
