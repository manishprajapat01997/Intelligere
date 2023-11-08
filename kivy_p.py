import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.anchorlayout import AnchorLayout
from install_service import install_new_service

 
## code ok and running github url------------
class MyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        Window.clearcolor = (1, 1, 1, 1)
        relative_layout = RelativeLayout()
        self.label = Label(
            text='Digital Documentation Systems Pvt.Ltd. ',
            font_size=24,
            color=(0, 0, 0, 1),
            pos_hint={'x': 0.0, 'top': 1.4})
            
        self.mobile_label = Label(
            text='Mob. No. : 123-456-7890',
            font_size=14,
            color=(0, 0, 0, 1),
            pos_hint={'x': -0.05, 'top': 1.3}
            )
        
        self.logo = Image(
            source='logo.png',
            size=(100, 100),
            size_hint=(None, None),
            pos_hint={'left': 1.5, 'top': 1.0}
        )

        relative_layout.add_widget(self.label)
        relative_layout.add_widget(self.mobile_label)
        relative_layout.add_widget(self.logo)

        self.layout.add_widget(relative_layout)

        # Create an AnchorLayout to center the result label vertically and horizontally
        center_layout = AnchorLayout(anchor_x='center', anchor_y='center')
        self.result_label = Label(text='', font_size=18, color=(0, 0, 0, 1)
        )
        center_layout.add_widget(self.result_label)
        self.layout.add_widget(center_layout)

        self.update_button = Button(
            text="Update Code ",
            background_color= (1.25165, 2.3232, 2.92), 
            size=(120, 40),
            size_hint=(None, None),  
            pos_hint={'center_x': 0.5, 'center_y': 0.5} 
        )
        self.update_button.bind(on_press=self.update_button_pressed) 
        self.layout.add_widget(self.update_button)

        return self.layout


    def run_my_code(self):
        print('2--------')
        result = install_new_service() 
        print('3---------',result)  

    def update_button_pressed(self,instance):
        self.run_my_code()

if __name__ == '__main__':
    MyApp().run()