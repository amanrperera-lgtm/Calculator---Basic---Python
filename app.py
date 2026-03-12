from flask import Flask, render_template, request, jsonify
import numpy as np
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import re
import base64



app = Flask(__name__)
# Calculator functions
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    #In case the user divides by 0
    if y == 0: return "Error: Division by zero is undefined."
    return x / y
def root(x, n):
    #In case user tries to get the zeroth root or the root of a negative number.
    if n == 0: return "Error: Cannot take zeroth root."
    if x < 0 and n % 2 == 0: return "Error: Cannot take even root of a negative number."
    return x ** (1/n)
@app.route("/graph", methods=["POST"])
def graph():
    data = request.json
    func = data.get("func")
    func = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', func)
    try:
        xmin = float(data.get("xmin", -10))
        xmax = float(data.get("xmax", 10))
        x = np.linspace(xmin, xmax, 500)    
        y = eval(func)
        plt.figure()
        plt.plot(x, y)
        plt.title("Plot of " + func)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        img = base64.b64encode(buf.read()).decode("utf-8")
        plt.close()
        return jsonify({"image": img})
    except Exception as e:
        return jsonify({"result": f"Error: {str(e)}"})

    

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    op = data.get("operation")
    result = None
    try:
        if op == "add":
            result = add(float(data["num1"]), float(data["num2"]))
        elif op == "subtract":
            result = subtract(float(data["num1"]), float(data["num2"]))
        elif op == "multiply":
            result = multiply(float(data["num1"]), float(data["num2"]))
        elif op == "divide":
            result = divide(float(data["num1"]), float(data["num2"]))
        elif op == "root":
            result = root(float(data["num1"]), float(data["num2"]))
        elif op == "exponent":
            result = float(data["num1"]) ** float(data["num2"])
        elif op == "log":
            num = float(data["num1"])
            if num <= 0: result = "Error: Logarithm undefined for non-positive numbers."
            else: result = math.log(num)
    except Exception as e:
        result = f"Error: {str(e)}"
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)