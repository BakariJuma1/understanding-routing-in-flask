from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
   
    return('<h1>Python Operations with Flask Routing and Views</h1>')

@app.route('/<string:name>')
def print_string(name):
    # prints to the console
    print(name)
    return f'print string {name}'

@app.route('/count/<int:num>')
def count(num):
    numbers=""
    for i in range(10):
        numbers += f"{1}<br>"
    return numbers    

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1,operation,num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2    
    elif operation == 'div':
        result = num1 / num2 
    elif operation == '%':
        result = num1 % num2  
    elif operation == '*':
        result = num1 * num2
    else:
        return " Invalid operation"    
    return str(result)          
    

if __name__ =='__main__':
    app.run(port=5555,debug=True)