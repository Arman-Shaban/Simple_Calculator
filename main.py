
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QFrame
from PyQt6.QtCore import Qt


from operators import (
    subtraction, aggregate, multiply, division, square_root,
    log, power, sin, cos, arccos, arcsin
)

# state

current_operator = {"name": None, "func": None, "unary": True}
history = []

def set_operator(name, func, unary=True):
    current_operator["name"] = name
    current_operator["func"] = func
    current_operator["unary"] = unary

    if unary:
        second_input.setDisabled(True)
        second_input.setPlaceholderText("This operator is Unary")
        second_input.clear()
    else:
        second_input.setDisabled(False)
        second_input.setPlaceholderText("Enter second number")

    result_label.setText(f'Selected operator: {name}')


def calculate():
    text1 = display.text().strip()
    if not text1:
        result_label.setText("Please enter first number")
        return
    try:
        a = float(text1)
    except ValueError:
        result_label.setText("First number is not valid")
        return

    if current_operator["func"] is None:
        result_label.setText("Please choose a operator")
        return

    try:
        if current_operator["unary"]:
            result = current_operator["func"](a)
            expression = f'{current_operator["name"]}({a})'
        else:
            text2 = second_input.text().strip()
            if not text2:
                result_label.setText("Please enter second number")
                return
            b = float(text2)
            result = current_operator["func"](a, b)
            expression = f"{a}{current_operator['name']}({b})"

        if isinstance(result, float) and result.is_integer():
            res_str = str(int(result))
        else:
            res_str = f"{result:.10g}"

        result_label.setText(f'Result: {res_str}')

        history.append(f"{expression} = {res_str}")
        history_label.setText("History: \n" + "\n".join(history[-3:]))

    except ValueError as e:
        result_label.setText(f'Error: {e}')
    except Exception as e:
        result_label.setText(f'Unexpected Error: {e}')


def clear_all():
    display.clear()
    second_input.clear()
    result_label.setText("Result:")
    current_operator["func"] = None
    current_operator["unary"] = True
    current_operator["name"] = None
    second_input.setDisabled(True)


app = QApplication([])
app.setStyle("Fusion")
window = QMainWindow()
window.setWindowTitle("Calculator")
window.resize(800, 700)
# sidebar
sidebar = QFrame(window)
sidebar.setGeometry(0, 0, 240, 700)

sidebar.setStyleSheet("""
    QFrame {
        background-color: black;
    }
""")


# Buttons

subtraction_button = QPushButton("Subtraction", window)
subtraction_button.move(30, 100)
subtraction_button.clicked.connect(lambda: set_operator("Subtraction", subtraction, unary=False))

aggregate_button = QPushButton("Aggregate", window)
aggregate_button.move(30, 140)
aggregate_button.clicked.connect(lambda: set_operator("Aggregate", aggregate, unary=False))

multiply_button = QPushButton("Multiply", window)
multiply_button.move(30, 180)
multiply_button.clicked.connect(lambda: set_operator("Multiply", multiply, unary=False))

division_button = QPushButton("Devide", window)
division_button.move(30, 220)
division_button.clicked.connect(lambda: set_operator("Division", division, unary=False))

square_root_button = QPushButton("Square Root", window)
square_root_button.move(30, 260)
square_root_button.clicked.connect(lambda: set_operator("SquareRoot", square_root, unary=True))

log_button = QPushButton("Log", window)
log_button.move(30, 300)
log_button.clicked.connect(lambda: set_operator("Log", log, unary=True))


power_button = QPushButton("Power", window)
power_button.move(30, 340)
power_button.clicked.connect(lambda: set_operator("Power", power, unary=False))

sin_button = QPushButton("Sin", window)
sin_button.move(30, 380)
sin_button.clicked.connect(lambda: set_operator("Sin", sin, unary=True))

cos_button = QPushButton("Cos", window)
cos_button.move(30, 420)
cos_button.clicked.connect(lambda: set_operator("Cos", cos, unary=True))

arcsin_button = QPushButton("ArcSin", window)
arcsin_button.move(30, 460)
arcsin_button.clicked.connect(lambda: set_operator("ArcSin", arcsin, unary=True))

arccos_button = QPushButton("ArcCos", window)
arccos_button.move(30, 500)
arccos_button.clicked.connect(lambda: set_operator("ArcCos", arccos, unary=True))

buttons = [
    subtraction_button,
    aggregate_button,
    multiply_button,
    division_button,
    square_root_button,
    log_button,
    power_button,
    sin_button,
    cos_button,
    arcsin_button,
    arccos_button
]

for button in buttons:
    button.setStyleSheet("""
        QPushButton {
            padding: 8px;
            font-size: 14px;
            min-width: 180px;
            min-height: 38px;
            border: none;
            border-radius: 8px;
            color: #00FFFF;
        }
        QPushButton:hover {
            background-color: #008080;
        }
        QPushButton:pressed {
        background-color: #D4E0EE;
        }
    """)
# Display
display = QLineEdit(window)
display.setGeometry(280, 40, 480, 60)
display.setPlaceholderText("0")
display.setAlignment(Qt.AlignmentFlag.AlignRight)
display.setStyleSheet("""
    QLineEdit {
        background-color: #2b2b2b;
        color: #00FFFF;
        font-size: 26px;
        padding: 10px;
        border: 2px solid #008080;
        border-radius: 10px;
    }

""")

# Result Label
result_label = QLabel("Result", window)
result_label.setGeometry(270, 120, 480, 40)
result_label.setStyleSheet("""
    QLabel {
        color: #00FFFF;
        font-size: 18px;
        padding: 5px;
    }
""")
# History Log

history_label = QLabel("History", window)
history_label.setGeometry(280, 180, 480, 40)
history_label.setStyleSheet("""
    QLabel {
        color: #FFA500
        font-size: 16px;
        padding: 5px;
    }
""")
# Second Input
second_input = QLineEdit(window)
second_input.setPlaceholderText("Enter second number(For binary operations)")
second_input.setGeometry(280, 240, 480, 50)
second_input.setAlignment(Qt.AlignmentFlag.AlignRight)
second_input.setStyleSheet("""
    QLineEdit {
        background-color: #2b2b2b;
        color: #00FFFF;
        font-size: 18px;
        padding: 8px;
        border: 2px solid #444;
        border-radius: 8px;
    }
""")
# Calc / Clear Button
calc_button = QPushButton("Calculate", window)
calc_button.setGeometry(280, 320, 220, 60)
calc_button.setStyleSheet("""
    QPushButton {
        background-color: #008080;
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
    }
    QPushButton:hover { background-color: #00b3b3; }
    QPushButton:pressed { background-color: #005959; }
""")
clear_button = QPushButton("Clear", window)
clear_button.setGeometry(540, 320, 220, 60)
clear_button.setStyleSheet("""
    QPushButton {
        background-color: #b33a3a;
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
    }
    QPushButton:hover { background-color: #d94c4c; }
    QPushButton:pressed { background-color: #7a2626; }
""")


calc_button.clicked.connect(calculate)
clear_button.clicked.connect(clear_all)

# Enter
display.returnPressed.connect(calculate)
second_input.returnPressed.connect(calculate)

second_input.setDisabled(True)


window.show()
app.exec()
