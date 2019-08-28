from random import random
from functools import partial
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Ellipse, Line

#Builder.load_file('paint.kv')

class PaintWidget(Widget):

    def __init__(self, **kwargs):
        self.color = (0, 0, 0, 1)
        self.color_palette_1 = [(random(),random(),random(),1) for x in range(5)]
        self.color_palette_2 = [(random(),random(),random(),1) for x in range(5)]
        super(PaintWidget, self).__init__(**kwargs)

    def on_touch_down(self, touch):
        #print('{}'.format(self.color))
        with self.canvas:
            Color(*self.color)
            d = 5
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=5)

    def on_touch_move(self,touch):
        touch.ud['line'].points += [touch.x, touch.y]

    def change_color(self, color, *args):
        self.color = color
        print('Color changed!')

    def paint_palette(self):



        palette = BoxLayout(orientation='vertical',pos=(200,0), size=(600,100))

        for i in range(2):
            row = BoxLayout(orientation='horizontal')

            if i == 0:
                for i in self.color_palette_1:
                    self.color_button = Button(background_color=i,background_normal='')
                    self.color_button.bind(on_press=partial(self.change_color,i))
                    row.add_widget(self.color_button)

            elif i == 1:
                for i in self.color_palette_2:
                    self.color_button = Button(background_color=i,background_normal='')
                    self.color_button.bind(on_press=partial(self.change_color,i))
                    row.add_widget(self.color_button)

            palette.add_widget(row)

        return palette


class PaintApp(App):

    def build(self):

        # sets the canvas color to white
        Window.clearcolor = (1, 1, 1, 1)

        parent = Widget()
        self.painter = PaintWidget()
        self.palette = self.painter.paint_palette()
        clearbtn = Button(text='Clear')
        clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        parent.add_widget(self.palette)

        return parent

    def clear_canvas(self, obj):
        self.painter.canvas.clear()


if __name__ == '__main__':
    PaintApp().run()
