from kivymd.app import MDApp

from kivymd_utils.router import Router, RouterWidget
from kivymd_utils.router import Route, ShellRoute
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDTextButton
from kivymd.uix.boxlayout import MDBoxLayout

from testscreen import TestScreen

class MainScreen(MDBoxLayout):
    def __init__(self, *args, **kwargs):
        router = kwargs["router"]
        super().__init__(
            MDBoxLayout(
                MDLabel(
                    text= "home"
                ),
                MDTextButton(
                    text = "go to test",
                    on_release = lambda x: router.go("/echo/hello")
                )

            )
        )


#ROUTES = 

class TestRoutesBase(MDApp):
    def build(self):
        return RouterWidget(
            router=Router(
    initial_route="/",
    routes= [
        Route(
            path="/",
            builder=lambda state, *args, **kwargs: TestScreen(
                "home", 
                ["/", "/redirect", "/item_test", "/a", "/sa"],
                *args, 
                **kwargs)
        ),
        Route(
            path="/echo/:name",
            name="test",
            builder=lambda state, *args, **kwargs: TestScreen(
                f"filled in {state.parameters['name']}",
                ["/", "/test/a"],
                *args,
                **kwargs)
        ),
        Route(
            path="/redirect",
            name="redirecter",
            redirect="/test"
        ),
        Route(
            path="/item_test",
            name="item_test",
            builder=lambda state, *args, **kwargs: MDBoxLayout(
                MDLabel(text="hey"),
                MDTextButton(
                    text="push_item",
                    on_release= lambda x: kwargs["router"].goData("/echo/_", {"name": "Test"})
                )
            )
        ),
        Route(
            path="/test",
            name="test2",
            builder=lambda state, *args, **kwargs: TestScreen(
                "testpage", 
                ["/", "/test/a"], 
                *args, 
                **kwargs
            ),
            routes=[
                Route(
                    path="/a",
                    name="subtest",
                    builder=lambda state, *args, **kwargs: TestScreen(
                        "subpagetest",
                        ["/"],
                        *args,
                        **kwargs
                    )
                ),
            ]
        ),
        ShellRoute(
            builder= lambda state, child, *args, **kwargs: MDBoxLayout(
                MDLabel(text= "hello from the shell"),
                child,
                orientation="vertical",
            ),
            routes=[
                Route(
                    path="/sa",
                    name="sa",
                    widget= MDBoxLayout(
                        MDLabel(text="hello")
                    )
                )
            ]
        )
    ]
)

        )

if __name__ == "__main__":
    TestRoutesBase().run()