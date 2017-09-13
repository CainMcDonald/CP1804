from kivy.app import App
from kivy.lang import Builder


class ConvertMilesToKilometres(App):
    def build(self):
        self.title = 'Convert Miles To Kilometres'
        self.root = Builder.load_file('convert_miles_to_kilometres.kv')
        return self.root
ConvertMilesToKilometres().run()