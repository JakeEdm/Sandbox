"""Module docstring"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from operator import itemgetter


class AnimalDemoApp(App):
    default = StringProperty()
    animals = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.animals = [['Leo', 'Dog'], ['Pickles', 'Cat'], ['Andre', 'Bird'], ['Felix', 'Cat']]

    def build(self):
        self.title = "Animals & Breeds"
        Window.size = (400, 400)
        self.root = Builder.load_file('AnimalsDemo.kv')
        self.generate_labels()
        return self.root

    def generate_labels(self):
        for animal in self.animals:
            temp_label = Label(text=f'{animal[0]} - {animal[-1]}')
            self.root.ids.entries_box.add_widget(temp_label)

    def sort_animals(self, choice):
        if choice == 'Sort by Name':
            self.animals.sort(key=itemgetter(0))
        elif choice == "Sort by Breed":
            self.animals.sort(key=itemgetter(1))
        self.root.ids.entries_box.clear_widgets()
        self.generate_labels()

    def on_save(self, name, breed):
        if name and breed != '':
            self.animals.append([name, breed])
            temp_animal = Label(text=f'{name} - {breed}')
            self.root.ids.entries_box.add_widget(temp_animal)
            self.root.ids.name.text = ''
            self.root.ids.breed.text = ''
            self.root.ids.popup.dismiss()


AnimalDemoApp().run()
