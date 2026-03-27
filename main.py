from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.metrics import dp
import math

KV = '''
MDScreen:
    md_bg_color: 0.05, 0.15, 0.25, 1

    MDBoxLayout:
        orientation: "vertical"

        MDBoxLayout:
            orientation: "vertical"
            size_hint_y: 10
            height: dp(120)
            padding: dp(12)
            spacing: dp(4)

            MDLabel:
                id: small_display
                text: ""
                halign: "right"
                theme_text_color: "Custom"
                text_color: 0.7,0.7,0.7,1
                font_size: "14sp"
                size_hint_y: None
                height: self.texture_size[1]

            MDLabel:
                id: display
                text: "0"
                halign: "right"
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "34sp"
                size_hint_y: None
                height: self.texture_size[1] * 1.4

        Widget:
            size_hint_y: 1

        ScrollView:
            size_hint_y: None
            height: self.parent.height - dp(320)

            MDGridLayout:
                cols: 5
                adaptive_height: True
                spacing: dp(6)
                padding: dp(10)

                CalcButton:
                    text: "C"
                    md_bg_color: 1, 0.3, 0.3, 1
                    on_press: app.clear()

                CalcButton:
                    text: "DEL"
                    md_bg_color: 0.8, 0.4, 0.2, 1
                    on_press: app.delete()

                CalcButton:
                    text: "()"
                    on_press: app.bracket()

                CalcButton:
                    text: "%"
                    on_press: app.add("%")

                CalcButton:
                    text: "÷"
                    on_press: app.add("/")

                CalcButton:
                    text: "sin"
                    on_press: app.func("sin")

                CalcButton:
                    text: "cos"
                    on_press: app.func("cos")

                CalcButton:
                    text: "tan"
                    on_press: app.func("tan")

                CalcButton:
                    text: "log"
                    on_press: app.func("log")

                CalcButton:
                    text: "√"
                    on_press: app.func("sqrt")

                CalcButton:
                    text: "7"
                    on_press: app.add("7")

                CalcButton:
                    text: "8"
                    on_press: app.add("8")

                CalcButton:
                    text: "9"
                    on_press: app.add("9")

                CalcButton:
                    text: "×"
                    on_press: app.add("*")

                CalcButton:
                    text: "x²"
                    on_press: app.add("**2")

                CalcButton:
                    text: "4"
                    on_press: app.add("4")

                CalcButton:
                    text: "5"
                    on_press: app.add("5")

                CalcButton:
                    text: "6"
                    on_press: app.add("6")

                CalcButton:
                    text: "+"
                    on_press: app.add("+")

                CalcButton:
                    text: "^"
                    on_press: app.add("**")

                CalcButton:
                    text: "1"
                    on_press: app.add("1")

                CalcButton:
                    text: "2"
                    on_press: app.add("2")

                CalcButton:
                    text: "3"
                    on_press: app.add("3")

                CalcButton:
                    text: "-"
                    on_press: app.add("-")

                CalcButton:
                    text: "1/x"
                    on_press: app.inverse()

                CalcButton:
                    text: "π"
                    on_press: app.add("3.1416")

                CalcButton:
                    text: "0"
                    on_press: app.add("0")

                CalcButton:
                    text: "."
                    on_press: app.add(".")

                CalcButton:
                    text: "e"
                    on_press: app.add("2.718")

                CalcButton:
                    text: "="
                    md_bg_color: 0.2, 0.6, 1, 1
                    on_press: app.calculate()

<CalcButton@MDRaisedButton>:
    font_size: "15sp"
    size_hint: 1, None
    height: dp(55)
    md_bg_color: 0.15, 0.25, 0.35, 1
    text_color: 1,1,1,1
    elevation: 5
    radius: [15, 15, 15, 15]
    ripple_alpha: 0.2
'''

class CalculatorApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.bracket_open = True
        return Builder.load_string(KV)

    def add(self, value):
        d = self.root.ids.display
        if d.text == "0":
            d.text = value
        else:
            d.text += value

    def clear(self):
        self.root.ids.display.text = "0"
        self.root.ids.small_display.text = ""

    def delete(self):
        d = self.root.ids.display
        d.text = d.text[:-1] if len(d.text) > 1 else "0"

    def bracket(self):
        if self.bracket_open:
            self.add("(")
            self.bracket_open = False
        else:
            self.add(")")
            self.bracket_open = True

    def func(self, name):
        if name == "sin":
            self.add("math.sin(math.radians(")
        elif name == "cos":
            self.add("math.cos(math.radians(")
        elif name == "tan":
            self.add("math.tan(math.radians(")
        elif name == "log":
            self.add("math.log10(")
        elif name == "sqrt":
            self.add("math.sqrt(")

    def inverse(self):
        try:
            val = eval(self.root.ids.display.text, {"__builtins__": None, "math": math})
            self.root.ids.display.text = str(1 / val)
        except:
            self.root.ids.display.text = "Error"

    def calculate(self):
        try:
            exp = self.root.ids.display.text

            if exp.count("(") != exp.count(")"):
                self.root.ids.display.text = "Error"
                return

            exp = exp.replace("%", "/100")

            result = str(eval(exp, {"__builtins__": None, "math": math}))

            self.root.ids.small_display.text = exp
            self.root.ids.display.text = result
        except Exception as e:
            self.root.ids.display.text = "Error"

CalculatorApp().run()
