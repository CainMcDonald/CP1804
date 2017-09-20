from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button


class SeperateNames(App):
    def build(self):
        self.title = 'Names List'
        self.root = Builder.load_file('separate_names.kv')
        self.create_widget()
        return self.root

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = {'Dylan smith', 'Ted ryan', 'Jenny jones', 'Billy D', 'Kevin'}

    def create_widget(self):
        for name in self.names:
            temp_button = Button(text=name)
            self.root.ids.entriesBox.add_widget(temp_button)


SeperateNames().run()
