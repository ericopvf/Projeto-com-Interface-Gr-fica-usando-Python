## Interface gráfica que imprime uma mensagem e permite interagir com um botão

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class MensagemApp(App):
    def build(self):
        layout = FloatLayout()
        btn = Button(
            text='Fala galera!',
            size_hint=(0.5, 0.2),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        btn.bind(on_press=self.on_press_button)
        layout.add_widget(btn)
        return layout

    def on_press_button(self, instance):
        print('Você apertou o botão!')

if __name__ == '__main__':
    MensagemApp().run()