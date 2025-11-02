from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class ClickerGame(App):
    def __init__(self):
        super().__init__()
        self.score = 0
    
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50)
        
        self.score_label = Label(
            text=f'Счет: {self.score}',
            font_size='30sp'
        )
        layout.add_widget(self.score_label)
        
        click_btn = Button(
            text='КЛИКНИ!',
            size_hint=(1, 0.6),
            background_color=(1, 0, 0, 1),
            font_size='25sp'
        )
        click_btn.bind(on_press=self.add_point)
        layout.add_widget(click_btn)
        
        return layout
    
    def add_point(self, instance):
        self.score += 1
        self.score_label.text = f'Счет: {self.score}'

# Запуск игры
if __name__ == '__main__':
    ClickerGame().run()
