from flask import Flask
from numpy import corrcoef


app = Flask(__name__)


def get_lists():
    with open('list_of_numbers1.txt', 'r') as list_of_number:
        list1 = list_of_number.read()
    with open('list_of_numbers2.txt', 'r') as list_of_number:
        list2 = list_of_number.read()
    return [int(x) for x in list1.split(', ')], [int(x) for x in list2.split(', ')]


@app.route("/")
def correlation():
    list1, list2 = get_lists()
    return str(corrcoef(list1, list2)[0, 1])


if __name__ == "__main__":
    app.run()