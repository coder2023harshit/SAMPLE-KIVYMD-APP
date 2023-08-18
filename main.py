from kivy.config import Config
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class ColorfulCalculatorApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Display
        self.display = Label(font_size=32, markup=True)
        self.display.bind(texture_size=self._update_display_height)
        layout.add_widget(self.display)

        # Button grid layout
        button_layout = GridLayout(cols=4, spacing=10, padding=10)

        buttons = [
             ('7', (0.2, 0.6, 0.2, 1)),
            ('8', (0.2, 0.6, 0.2, 1)),
            ('9', (0.2, 0.6, 0.2, 1)),
            ('/', (0.6, 0.6, 0.2, 1)),
            ('4', (0.2, 0.6, 0.2, 1)),
            ('5', (0.2, 0.6, 0.2, 1)),
            ('6', (0.2, 0.6, 0.2, 1)),
            ('*', (0.6, 0.6, 0.2, 1)),
            ('1', (0.2, 0.6, 0.2, 1)),
            ('2', (0.2, 0.6, 0.2, 1)),
            ('3', (0.2, 0.6, 0.2, 1)),
            ('-', (0.6, 0.6, 0.2, 1)),
            ('.', (0.2, 0.2, 0.6, 1)),
            ('0', (0.2, 0.2, 0.6, 1)),
            ('=', (0.6, 0.2, 0.2, 1)),
            ('+', (0.6, 0.6, 0.2, 1))
        ]

        for label, color in buttons:
            button = Button(text=label, background_color=color, color=(1, 1, 1, 1))
            button.bind(on_press=self.on_button_press)
            button_layout.add_widget(button)

        clear_button = Button(text='C', background_color=(0.6, 0.2, 0.2, 1), color=(1, 1, 1, 1))
        clear_button.bind(on_press=self.clear_display)
        button_layout.add_widget(clear_button)

        layout.add_widget(button_layout)

        return layout

    def _update_display_height(self, instance, value):
        self.display.text_size = (self.display.width, None)

    def on_button_press(self, instance):
        current = self.display.text
        button_text = instance.text

        if button_text == '=':
            try:
                solution = str(eval(current))
                self.display.text = '[color=00FF00]' + solution + '[/color]'
            except:
                self.display.text = '[color=FF0000]Error[/color]'
        else:
            self.display.text += button_text

    def clear_display(self, instance):
        self.display.text = ''

if __name__ == '__main__':
    Config.set('graphics', 'resizable', '0')  # Disable window resizing
    Config.set('graphics', 'width', '350')
    Config.set('graphics', 'height', '450')
    app = ColorfulCalculatorApp()
    app.run()
