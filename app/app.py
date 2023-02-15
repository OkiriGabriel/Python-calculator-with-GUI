mport tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.expression = ""
        self.input_var = tk.StringVar()
        self.input_var.set("0")

        input_frame = tk.Frame(self.master, height=50)
        input_frame.pack(side=tk.TOP, fill=tk.X)

        self.input_label = tk.Label(input_frame, textvariable=self.input_var, font=('Arial', 20), anchor='e')
        self.input_label.pack(side=tk.RIGHT, padx=10)

        button_frame = tk.Frame(self.master)
        button_frame.pack(side=tk.TOP)

        buttons = [
            ['1', '2', '3', '+'],
            ['4', '5', '6', '-'],
            ['7', '8', '9', '*'],
            ['0', '.', 'C', '/'],
            ['(', ')', '^', '=']
        ]

        for row in buttons:
            row_frame = tk.Frame(button_frame)
            row_frame.pack(side=tk.TOP)

            for label in row:
                button = tk.Button(row_frame, text=label, width=5, height=2, font=('Arial', 16), command=lambda label=label: self.button_click(label))
                button.pack(side=tk.LEFT, padx=5, pady=5)

    def button_click(self, label):
        if label == 'C':
            self.expression = ""
            self.input_var.set("0")
        elif label == '=':
            try:
                result = str(eval(self.expression))
                self.expression = result
                self.input_var.set(result)
            except:
                self.expression = ""
                self.input_var.set("Error")
        else:
            self.expression += label
            self.input_var.set(self.expression)

root = tk.Tk()
app = Calculator(root)
root.mainloop()
