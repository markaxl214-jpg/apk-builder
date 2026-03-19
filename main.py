from kivymd.app import MDApp
from kivy.lang import Builder

KV = """
MDScreen:
    md_bg_color: 0.1, 0.1, 0.15, 1

    MDBoxLayout:
        orientation: "vertical"
        padding: "15dp"
        spacing: "15dp"

        MDCard:
            radius: [20]
            elevation: 8
            size_hint_y: None
            height: "100dp"

            MDLabel:
                id: display
                text: "0"
                halign: "right"
                font_style: "H4"
                padding: "10dp"

        GridLayout:
            cols: 4
            spacing: "10dp"

            MDFlatButton:
                text: "7"
                on_release: app.add("7")

            MDFlatButton:
                text: "8"
                on_release: app.add("8")

            MDFlatButton:
                text: "9"
                on_release: app.add("9")

            MDFlatButton:
                text: "/"
                on_release: app.add("/")

            MDFlatButton:
                text: "4"
                on_release: app.add("4")

            MDFlatButton:
                text: "5"
                on_release: app.add("5")

            MDFlatButton:
                text: "6"
                on_release: app.add("6")

            MDFlatButton:
                text: "*"
                on_release: app.add("*")

            MDFlatButton:
                text: "1"
                on_release: app.add("1")

            MDFlatButton:
                text: "2"
                on_release: app.add("2")

            MDFlatButton:
                text: "3"
                on_release: app.add("3")

            MDFlatButton:
                text: "-"
                on_release: app.add("-")

            MDFlatButton:
                text: "0"
                on_release: app.add("0")

            MDFlatButton:
                text: "."
                on_release: app.add(".")

            MDFlatButton:
                text: "="
                on_release: app.calculate()

            MDFlatButton:
                text: "+"
                on_release: app.add("+")
"""

class CalculatorApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def add(self, value):
        if self.root.ids.display.text == "0":
            self.root.ids.display.text = value
        else:
            self.root.ids.display.text += value

    def calculate(self):
        try:
            result = str(eval(self.root.ids.display.text))
            self.root.ids.display.text = result
        except:
            self.root.ids.display.text = "Error"

CalculatorApp().run()
