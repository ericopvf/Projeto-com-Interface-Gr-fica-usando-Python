## Interface gráfica que imprime uma imagem por meio da biblioteca Kivy e por meio de uma URL

from kivy.app import App
from kivy.uix.image import AsyncImage

class Imagem(App):
    def build(self):
        img = AsyncImage(
            source='https://supermariorun.com/assets/img/stage/mario03.png',
            size_hint=(1, 0.5),
            pos_hint={'center_x': .5, 'center_y': .5}
        )
        return img  

if __name__ == '__main__':
    Imagem().run()