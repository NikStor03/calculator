import tkinter as tk


class Calculator:

    def __init__(self):
        self.btn = [
            'C', 'DEL', '%', '/',
            '1', '2', '3', '*',
            '4', '5', '6', '-',
            '7', '8', '9', '+',
            '0', '^2', '=',
        ]
        self.math = ['*', '/', '%', '-', '+', '=', '^2']

        # window settings
        self.window = tk.Tk()
        self.window['bg'] = '#000'
        self.window.resizable(False, False)
        self.window.geometry('410x600')

        self.formula = '0'
        self.lbl = tk.Label()

    # create Label
    def place_label(self):
        self.lbl = tk.Label(
            text=self.formula,
            font=("Courier", 40),
            background='black',
            width=0,
            foreground="#FFF",
            height=2)
        self.lbl.place(y=1)

    # Place all buttons in window
    def place_btn(self):
        x = 10
        y = 100
        after = 0

        index_btn = 0
        for row in range(5):
            for column in range(4):
                try:
                    command = lambda x = self.btn[index_btn]: self.logic(x)
                    width = 90
                    height = 80
                    if after == 1:
                        x += 100
                        after += 1
                    elif after == 2:
                        x += 1
                    if self.btn[index_btn] == '0':
                        width = 190
                        after = 1
                    btn = tk.Button(
                        text=self.btn[index_btn],
                        font=("Times New Roman", 35),
                        foreground='grey',
                        command=command
                    )
                    btn.place(x=x, y=y, width=width, height=height)
                    index_btn += 1
                    x += 100
                except IndexError:
                    pass
            x = 10
            y += 100

    # Logic of buttons
    def logic(self, operation):
        if operation == 'C':
            self.formula = ''
        elif operation == 'DEL':
            self.formula = self.formula[0:-1]
        elif operation == '=':
            self.formula = str(eval(self.formula))
        elif operation == '^2':
            self.formula = str(eval(self.formula) ** 2)
        else:
            if len(self.formula) < 2 and self.formula[0] == '0':
                self.formula = self.formula[1:] + operation
            elif self.formula[-1] in self.math and operation in self.math:
                num = -1
                self.formula = self.formula[0:num] + operation
            else:
                self.formula += operation
        self.update()

    # Update info in Label
    def update(self):
        self.lbl.configure(text=self.formula)
        if self.formula == '':
            self.formula = '0'
        self.lbl.configure(text=self.formula)

    def start(self):
        self.place_label()
        self.place_btn()
        self.window.mainloop()


if __name__ == "__main__":
    clc = Calculator()
    clc.start()
