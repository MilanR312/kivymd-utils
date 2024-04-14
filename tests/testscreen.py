from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDTextButton
from kivymd.uix.boxlayout import MDBoxLayout

class TestScreen(MDBoxLayout):
    def __init__(self, name:str, paths: list[str], *args, **kwargs):
        router = kwargs["router"]
        buttons = [
            MDTextButton(
                text = f"go to '{e}'",
                on_release = lambda x, f=e: router.go(f)
            ) for e in paths
        ]
        super().__init__(
                MDLabel(
                    text= f"{name}"
                ),
                *buttons,
                *args,
                orientation="vertical",
                spacing=20
        )