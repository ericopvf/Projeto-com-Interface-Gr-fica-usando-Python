## Interface gráfica que imprime uma mensagem por meio da biblioteca Kivy

from kivy.app import App
from kivy.uix.label import Label

class Mensagem(App):
    def build(self):
        label = Label(text='Fala galera!',
                      size_hint = (.5, .5),
                      pos_hint = {'center_x': .5, 'center_y': .5})
        
        return label
    
if __name__ == '__main__':
    app = Mensagem()
    app.run()