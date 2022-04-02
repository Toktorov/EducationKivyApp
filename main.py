from logging import PlaceHolder
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class Education(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        #возвращает объект окна со всеми его виджетами
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

        # виджет изображения
        self.window.add_widget(Image(source="logo.png"))

        # виджет текста
        self.error = Label(
                        text= "Введите свой логин и пароль",
                        font_size= 18,
                        color= 'black'
                        )
        self.window.add_widget(self.error)

        # виджет ввода текста для логина
        self.login = TextInput(
                    multiline= False,
                    padding_y= (20,20),
                    size_hint= (1, 0.5),
                    text = "Логин",
                    )

        self.window.add_widget(self.login)

        # виджет ввода текста для пароля

        self.password = TextInput(
                    multiline= False,
                    padding_y= (20,20),
                    size_hint= (1, 0.5),
                    text = "Пароль"
                    )

        self.window.add_widget(self.password)

        # виджет кнопки для входа
        self.button = Button(
                      text= "Войти",
                      size_hint= (1,0.5),
                      bold= True,
                      )
        self.button.bind(on_press=self.check)
        self.window.add_widget(self.button)

        return self.window

    def check(self, instance):
        #Проверка логина и пароля
        self.error.text = "Неправильный пароль или пароль"

if __name__ == "__main__":
    Education().run()
