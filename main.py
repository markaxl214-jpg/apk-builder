from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Calculator(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.padding = 10
        self.spacing = 10

        # Display
        self.display = TextInput(
            text='',
            font_size=40,
            size_hint=(1, .5),
            readonly=True,
            halign="right",
            multiline=False
        )
        self.add_widget(self.display)

        # Buttons Layout
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['(', ')', '=', 'DEL']
        ]

        grid = GridLayout(cols=4, spacing=10)

        for row in buttons:
            for btn in row:
                grid.add_widget(
                    Button(
                        text=btn,
                        font_size=24,
                        on_press=self.on_button_press
                    )
                )

        self.add_widget(grid)

    def on_button_press(self, instance):
        text = instance.text

        if text == 'C':
            self.display.text = ''
        elif text == 'DEL':
            self.display.text = self.display.text[:-1]
        elif text == '=':
            try:
                result = str(eval(self.display.text))
                self.display.text = result
            except:
                self.display.text = 'Error'
        else:
            self.display.text += text


class CalculatorApp(App):
    def build(self):
        return Calculator()


if __name__ == '__main__':
    CalculatorApp().run()
