from kivymd.app import MDApp
from kivymd_utils.coroutine.coroutineBuilder import CoroutineBuilder, CoroutineSnapshot
from kivymd.uix.label import MDLabel

import asyncio

class TestApp(MDApp):
    async def generate_number(self):
        await asyncio.sleep(2)
        return "5"
    def build(self):
        self.coroutine = self.generate_number()
        return CoroutineBuilder(
            builder=self.generate_text,
            coroutine=self.coroutine
        )
    
    def generate_text(self, snapshot: CoroutineSnapshot):
        if snapshot.has_data:
            return MDLabel(text = snapshot.data)
        else:
            return MDLabel(text = "calculating")
        

if __name__ == "__main__":
    asyncio.run(TestApp().async_run())