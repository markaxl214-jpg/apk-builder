from kivymd.app import MDApp
from kivy.lang import Builder

KV = """
MDScreen:
    md_bg_color: 0.1, 0.1, 0.15, 1   # Dark background

    MDBoxLayout:
        orientation: "vertical"
        padding: "20dp"
        spacing: "20dp"
        padding: "29dp","90dp","40dp","0dp"

        # 🔹 Display Card
        MDCard:
            radius: [20,]
            elevation: 8
            size_hint_y: None
            height: "100dp"

            MDLabel:
                id: display
                text: "0"
                halign: "right"
                valign: "center"
                font_style: "H3"
                theme_text_color: "Primary"
                text_size: self.size
                padding: "0dp","0dp","10dp","0dp"

        # 🔹 Buttons Grid
        GridLayout:
            cols: 4
            spacing: "15dp"
            padding: "0dp","120dp","0dp","0dp"

            # Row 1
            MDRaisedButton:
                on_release: app.clear_display()
                text: "C"

            MDRaisedButton:
                on_release: app.cut_display()
                text: "Del"

            MDRaisedButton:
                on_release: app.add_value("(")
                text: "("

            MDRaisedButton:
                on_release: app.add_value(")")
                text: ")"

            MDRaisedButton:
                on_release: app.add_value("/")
                text: "/"

            # Row 2
            MDRaisedButton:
                on_release: app.add_value("7")
                text: "7"

            MDRaisedButton:
                on_release: app.add_value("8")
                text: "8"

            MDRaisedButton:
                on_release: app.add_value("9")
                text: "9"

            MDRaisedButton:
                on_release: app.add_value("*")
                text: "*"

            # Row 3
            MDRaisedButton:
                on_release: app.add_value("4")
                text: "4"

            MDRaisedButton:
                on_release: app.add_value("5")
                text: "5"

            MDRaisedButton:
                on_release: app.add_value("6")
                text: "6"

            MDRaisedButton:
                on_release: app.add_value("-")
                text: "-"

            # Row 4
            MDRaisedButton:
                on_release: app.add_value("1")
                text: "1"

            MDRaisedButton:
                on_release: app.add_value("2")
                text: "2"

            MDRaisedButton:
                on_release: app.add_value("3")
                text: "3"

            MDRaisedButton:
                on_release: app.add_value("+")
                text: "+"

            # Last Row
            MDRaisedButton:
                on_release: app.add_value("0")
                text: "0"

            MDRaisedButton:
                on_release: app.add_value(".")
                text: "."

            MDRaisedButton:
                on_release: app.calculate()
                text: "="
"""

class CalculatorApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def add_value(self, value):
        if self.root.ids.display.text == "0":
            self.root.ids.display.text = value
        else:
            self.root.ids.display.text += value

    def clear_display(self):
        self.root.ids.display.text = "0"

    def cut_display(self):
        text = self.root.ids.display.text
        if len(text) > 1:
            self.root.ids.display.text = text[:-1]
        else:
            self.root.ids.display.text = "0"

    def calculate(self):
        try:
            expression = self.root.ids.display.text
            result = str(eval(expression))
            self.root.ids.display.text = result
        except:
            self.root.ids.display.text = "Error"
CalculatorApp().run()
