from kivy.app import App
from kivy.lang import Builder


class ConvertMilesToKilometres(App):
    def build(self):
        self.title = 'Convert Miles To Kilometres'
        self.root = Builder.load_file('convert_miles_to_kilometres.kv')
        return self.root

    def handle_convert(self):
        value = self.validate_distance()
        result = value * 1.60934
        self.root.ids.output_label.text = str(result)

    def validate_distance(self):
        try:
            value = float(self.root.ids.input_distance.text)
            return value
        except ValueError:
            return 0

    def handle_increment(self, change):
        value = self.validate_distance() + change
        self.root.ids.input_distance.text = str(value)
        self.handle_convert()


ConvertMilesToKilometres().run()
