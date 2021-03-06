from flask import Flask, render_template
from db_utils import get_session
from variables import DEBUG, PORT
from model import People

app = Flask(__name__)


@app.route("/unique_name")
def get_unique_name():
    s = get_session()
    uniq_names = set([x.FirstName for x in s.query(People).all()])

    return render_template('std/list.html', uniq_names=uniq_names)


if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)
