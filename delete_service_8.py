
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.popup import Popup
import os
import psutil
import shutil
import sys
import shell
import win32com.shell.shell as shell


ASADMIN = 'asadmin'
if sys.argv[(-1)] != ASADMIN:
    print("Script is not running with administrative privileges. Trying to elevate...")
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + [ASADMIN])

    retval = shell.ShellExecuteEx(lpVerb='runas', lpFile=(sys.executable), lpParameters=params)
    if retval['hInstApp'] <= 32:
        print(f"Failed to elevate privileges. Error code: {retval['hInstApp']}")
        sys.exit(1)

    print("Elevated successfully. Continuing...")

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

        center_layout = AnchorLayout(anchor_x='center', anchor_y='center')
        self.result_label = Label(text='', font_size=18, color=(0, 0, 0, 1)
        )
        center_layout.add_widget(self.result_label)
        self.layout.add_widget(center_layout)

        self.update_button = Button(
            text="Update Code ",
            background_color=(1.25165, 2.3232, 2.92),
            size=(120, 40),
            size_hint=(None, None),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.update_button.bind(on_press=self.update_button_pressed)
        self.layout.add_widget(self.update_button)

        self.restart_button = Button(
            text="Restart PC",
            background_color=(2.25165, 1.3232, 2.92),
            size=(120, 40),
            size_hint=(None, None),
            pos_hint={'center_x': 0.5, 'center_y': 0.4}
        )
        self.restart_button.bind(on_press=self.restart_button_pressed)
        self.layout.add_widget(self.restart_button)

        # Create a popup to display messages
        self.popup = None

        return self.layout

    def show_message(self, message):
        if self.popup is not None:
            self.popup.dismiss()

        self.popup = Popup(title='Message', content=Label(text=message),
                           size_hint=(None, None), size=(400, 200))
        self.popup.open()

    def run_my_code(self):
        service_prefix = 'Intelligere'
        service = self.getService(service_prefix)
        print('a-----', service)
        if service:
            status = service.status()
            print(f'Service Status: {status}')

            # Stop and delete the service, and remove the executable
            result = self.stopAndDeleteService(service)
            if result:
                print('Service stopped and deleted.')
                self.show_message("Please restart your PC.")
            else:
                print('Error stopping and deleting service.')
        else:
            print('Service not found.')
            self.show_message("Service not found.")

    def update_button_pressed(self, instance):
        self.run_my_code()

    def getService(self, service_prefix):
        all_services = list(psutil.win_service_iter())
        target_service = None

        for service in all_services:
            if service.name() and service.name().lower().startswith(service_prefix.lower()):
                target_service = service
                print('target_service-----', target_service)
                break

        return target_service

    def stopAndDeleteService(self, service):
        try:
            service_name = service.name()
            print(f'service_name---- {service_name}')
            service_status = service.status()
            print(f'service_status---- {service_status}')
            if service_status == 'running':
                try:
                    os.system(f'sc stop {service_name}')
                    print(f"Service '{service_name}' stopped.---!!!")
                except Exception as e:
                    print(f"Error stopping service: {e}")
            try:
                os.system(f'sc delete {service_name}')
                print(f"Service '{service_name}' deleted.---!!!")
            except Exception as e:
                print(f"Error deleting service: {e}")


            folder_path = os.path.join('C:\\Windows', service_name)
            print(f'folder_path---- {folder_path}')
            if os.path.exists(folder_path):
                try:
                    shutil.rmtree(folder_path)
                    print(f"Folder '{service_name}' and its contents removed.")
                except Exception as e:
                    print(f"Error deleting folder: {e}")
            else:
                print(f"Folder '{service_name}' not found.")
            return True
        
        except Exception as e:
            print(f"Error stopping/deleting service: {e}")
            return False
        
    def restart_button_pressed(self, instance):
        os.system('shutdown /r /t 0')

if __name__ == '__main__':
    MyApp().run()






