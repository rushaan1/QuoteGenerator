from kivy.app import *
from kivy.uix.gridlayout import *
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.lang import Builder
import requests
import json
from textwrap3 import wrap

class MainApp(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6,0.7)
        self.window.pos_hint ={"center_x": 0.5, "center_y":0.5}
        self.window.add_widget(Image(source="img.png",pos=(100,100)))
        self.quote = Label(text="Click To Get Quote", font_size=24, color='#C0FF02')
        self.window.add_widget(self.quote)
        self.button = Button(text="Get Quote")
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self,instance):
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        quote = json_data[0]['q']

        wquote = wrap(quote, 50)
        self.quote.text = f"\n".join(wquote)+" \n \n                                                        -"+json_data[0]['a']



if __name__ == "__main__":
    quotes = MainApp()
    quotes.run()
