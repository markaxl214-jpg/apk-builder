from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Calculator(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 4

        self.display = TextInput(
            text='0',
            font_size=32,
            readonly=True,
            halign="right",
            size_hint=(1, 0.2)
        )
        self.add_widget(self.display)

        buttons = [
            '7','8','9','/',
            '4','5','6','*',
            '1','2','3','-',
            '0','.','=','+'
        ]

        for btn in buttons:
            self.add_widget(Button(text=btn, on_press=self.on_button_click))

    def on_button_click(self, instance):
        text = instance.text

        if text == "=":
            try:
                self.display.text = str(eval(self.display.text))
            except:
                self.display.text = "Error"

        else:
            if self.display.text == "0":
                self.display.text = text
            else:
                self.display.text += text


class CalculatorApp(App):
    def build(self):
        return Calculator()


CalculatorApp().run()
