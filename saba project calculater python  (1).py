import tkinter as tk
import math

# 1. Main Window Setup
root = tk.Tk()
root.title("SABA's Scientific Calculator")
root.geometry("350x540")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

# 2. Variables
data_input = ""
vaani = tk.StringVar()

# 3. Smart Calculation Logic
def calculate(exp):
    try:
        exp = exp.replace(" ", "")
        
        if exp.count('(') > exp.count(')'):
            exp += ')' * (exp.count('(') - exp.count(')'))

        exp = exp.replace('π', str(math.pi))
        exp = exp.replace('^', '**')

        result = eval(exp, {"__builtins__": None}, {
            "sin": lambda x: math.sin(math.radians(x)),
            "cos": lambda x: math.cos(math.radians(x)),
            "tan": lambda x: math.tan(math.radians(x)),
            "sqrt": math.sqrt,
            "log": math.log10
        })

        if isinstance(result, float) and result.is_integer():
            return str(int(result))
        else:
            return str(round(result, 6))

    except ZeroDivisionError:
        return "Math Error"
    except:
        return "Error"

# 4. Button Click Handler
def dabaya(btn):
    global data_input

    if btn == "=":
        res = calculate(data_input)
        vaani.set(res)
        data_input = str(res)

    elif btn == "C":
        data_input = ""
        vaani.set("")

    elif btn == "⌫":
        data_input = data_input[:-1]
        vaani.set(data_input)

    else:
        data_input += str(btn)
        vaani.set(data_input)

# 5. Keyboard Support 🔥
def key_press(event):
    global data_input
    key = event.char

    if key in "0123456789+-*/.^()":
        data_input += key
        vaani.set(data_input)

    elif key == "\r":   # Enter
        res = calculate(data_input)
        vaani.set(res)
        data_input = str(res)

    elif key == "\x08":  # Backspace
        data_input = data_input[:-1]
        vaani.set(data_input)

# Bind Keyboard
root.bind("<Key>", key_press)

# 6. GUI Components
display = tk.Entry(root, font=('Arial', 22, 'bold'),
                   textvariable=vaani, bg="#222831",
                   fg="white", justify='right', bd=15, relief='flat')
display.pack(pady=25, fill="x", padx=15)

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack()

# Buttons List
buttons = [
    'sin', 'cos', 'tan', '√',
    'log', '(', ')', '^',
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', 'π', '+',
    'C', '⌫', '00', '='
]

# Format function
def format_btn(b):
    if b == '√': return 'sqrt('
    if b in ['sin', 'cos', 'tan', 'log']: return b + '('
    return b

# Create Buttons
r, c = 0, 0
for b in buttons:
    color = "#333333"

    if b in ['C', '⌫']:
        color = "#d9534f"
    elif b == '=':
        color = "#5cb85c"
    elif b in '+-*/^':
        color = "#f0ad4e"
    elif b in ['sin','cos','tan','√','log','π','(',')']:
        color = "#5bc0de"

    tk.Button(frame, text=b, width=5, height=2,
              bg=color, fg="white",
              font=('Arial', 11, 'bold'),
              command=lambda x=b: dabaya(format_btn(x))
              ).grid(row=r, column=c, padx=5, pady=5)

    c += 1
    if c > 3:
        c = 0
        r += 1

# Run App
root.mainloop()