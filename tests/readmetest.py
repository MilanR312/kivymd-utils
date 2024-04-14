from kivymd_utils.router import Router, RouterWidget, Route, ShellRoute
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDTextButton
from kivymd.app import MDApp
from kivymd_utils.redrawAble import NotifyListener, RedrawAble

class Person(NotifyListener):
    def __init__(self, name:str, age: int):
        super().__init__()
        self.name = name
        self.age = age

    def age_up(self):
        self.age += 1
        self.notify_listeners()
    

class App(MDApp):
    def build(self):
        self.person = Person("Joe", 25)

        self.redraw_able= RedrawAble(
            provider=self.person,
            builder=lambda: MDBoxLayout(
                MDLabel(text= f"{self.person.name} is {self.person.age} years old"),
                MDTextButton(
                    text= "age",
                    on_release= lambda x:self.person.age_up()
                ),
                MDTextButton(
                    text="force redraw",
                    on_release= lambda x: self.redraw_able.redraw()
                )
            )
        )
        return self.redraw_able
    
if __name__=="__main__":
    App().run()