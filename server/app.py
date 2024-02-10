from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string>')
def print_string(string):
    print(f'{string}')
    return f'{string}'

@app.route('/count/<int:integer>')
def count(integer):
    numbers = '\n'.join(str(num) for num in range(integer + 1))
    return numbers[:-2]

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        if num2 != 0:
            return str(num1 / num2)
        else:
            return 'Error: Division by zero'
    elif operation == '%':
        return str(num1 % num2)

if __name__ == '__main__':
    app.run(port=5555, debug=True)