import tkinter as tk


class Calculator:
    def __init__(self, window):
        self.window = window
        self.window.title("Calculator")
        self.expression = ""

        self.display = tk.Entry(window, font=("Arial", 20))
        self.display.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        button_texts = [
            '1', '2', '3', '/',
            '4', '5', '6', '*',
            '7', '8', '9', '-',
            'C', '0', '=', '+'
        ]

        row, col = 1, 0
        for text in button_texts:
            if text == '=':
                tk.Button(self.window, text=text, width=5, height=2,
                          command=self.calculate).grid(row=row, column=col)
            elif text == 'C':
                tk.Button(self.window, text=text, width=5, height=2,
                          command=self.clear).grid(row=row, column=col)
            else:
                tk.Button(self.window, text=text, width=5, height=2,
                          command=lambda t=text: self.append(t)).grid(row=row,column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def append(self, char):
        self.expression += str(char)
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)

    def calculate(self):
        try:
            result = eval(self.expression)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
            self.expression = str(result)
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            self.expression = ""


window = tk.Tk()
calculator = Calculator(window)
window.mainloop()

