from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def Hello_world():
    return 'Hello world'

@app.route('/add/<int:n>')
def armstrong(n):
    sum = 0
    order = len(str(n))
    copy_n = n
    while(n>0):
        digit = n%10
        sum += digit **order
        n = n//10
    if (sum== copy_n):
        result = {
            'number': copy_n,
            'Armstrong': True,
            "Server IP" : "122.22.150.66"
        }
    else:
        result = {
            'number': copy_n,
            'Armstrong': False,
            "Server IP": "122.22.150.53"
        }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)