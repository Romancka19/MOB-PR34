from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class RainbowColorApp(App):
    def build(self):
        self.color_label = Label(text='Hello!', size_hint=(1, 0.5))
        layout = BoxLayout(orientation='vertical')
        self.color_text = TextInput(hint_text='Код цвета', multiline=False)
        layout.add_widget(self.color_label)
        layout.add_widget(self.color_text)
        colors = {
            'Красный': '#ff0000',
            'Оранжевый': '#ff9900',
            'Желтый': '#ffff00',
            'Зеленый': '#00ff00',
            'Голубой': '#00ffff',
            'Синий': '#0000ff',
            'Фиолетовый': '#ff00ff'
        }
        
        for color_name, color_code in colors.items():
            btn = Button(text=color_name, background_color=self.hex_to_rgba(color_code))
            btn.bind(on_press=self.on_button_press)
            layout.add_widget(btn)
        
        
        return layout
    
    def hex_to_rgba(self, hex_code):
        hex_code = hex_code.lstrip('#')
        r = int(hex_code[0:2], 16) / 160
        g = int(hex_code[2:4], 16) / 160
        b = int(hex_code[4:6], 16) / 160
        return (r, g, b, 1)
    
    def on_button_press(self, instance):
        color_name = instance.text
        color_code = instance.background_color
        self.color_label.text = color_name
        self.color_text.text = '#{0:02x}{1:02x}{2:02x}'.format(int(color_code[0] * 160), int(color_code[1] * 160), int(color_code[2] * 160))

if __name__ == '__main__':
    RainbowColorApp().run()
