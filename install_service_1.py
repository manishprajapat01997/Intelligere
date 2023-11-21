# import gdown
# import os
# import ctypes
# import sys
# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.label import Label
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.relativelayout import RelativeLayout
# from kivy.uix.anchorlayout import AnchorLayout
# from kivy.uix.image import Image
# from kivy.uix.progressbar import ProgressBar
# from kivy.core.window import Window
# from kivy.config import Config
# from kivy.clock import Clock
# import shutil 

# class IntelligereApp(App):
#     def build(self):  
#         self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
#         self.icon="logo.png"
#         self.title = "Intelligere"
#         Window.clearcolor = (1, 1, 1, 1)
#         relative_layout = RelativeLayout()
#         Window.icon = 'logo.ico'

#         self.label = Label(
#             text='Digital Documentation Systems Pvt.Ltd. ',
#             font_size=24,
#             color=(0, 0, 0, 1),
#             pos_hint={'x': 0.0, 'top': 1.4}
#         )

#         self.mobile_label = Label(
#             text='Mob. No. : 123-456-7890',
#             font_size=14,
#             color=(0, 0, 0, 1),
#             pos_hint={'x': -0.05, 'top': 1.3}
#         )

#         self.logo = Image(
#             source='logo.png',
#             size=(100, 100),
#             size_hint=(None, None),
#             pos_hint={'left': 1.5, 'top': 1.0}
#         )

#         relative_layout.add_widget(self.label)
#         relative_layout.add_widget(self.mobile_label)
#         relative_layout.add_widget(self.logo)

#         self.layout.add_widget(relative_layout)

#         center_layout = AnchorLayout(anchor_x='center', anchor_y='center')
#         self.result_label = Label(text='', font_size=18, color=(0, 0, 0, 1))
#         center_layout.add_widget(self.result_label)
#         self.layout.add_widget(center_layout)

#         self.update_button = Button(
#             text="Update Code",
#             background_color=(1.25165, 2.3232, 2.92),
#             size=(120, 40),
#             size_hint=(None, None),
#             pos_hint={'center_x': 0.5, 'center_y': 0.5}
#         )
#         self.update_button.bind(on_press=self.update_button_pressed)
#         self.layout.add_widget(self.update_button)

#         remove_old_folders_button = Button(
#                             text='Remove Old Folders',
#                             on_release=self.remove_old_folders,  
#                             background_color=(1.25165, 2.3232, 2.92),
#                             size=(150, 40),
#                             size_hint=(None, None),
#                             pos_hint={'center_x': 0.5, 'center_y': 0.5}
#                         )
#         self.layout.add_widget(remove_old_folders_button)

#         return self.layout


#     def download_file_from_google_drive(self, gdrive_file_id, destination):
#         progress_bar = ProgressBar(max=100)
#         self.layout.add_widget(progress_bar)
#         self.layout.remove_widget(self.result_label)

#         def update_progress(dt):
#             percent_complete = (progress_bar.value / progress_bar.max) * 100
#             self.result_label.text = f'Downloading: {percent_complete:.2f}%'

#         Clock.schedule_interval(update_progress, 0.1)

#         try:
#             gdown.download(f'https://drive.google.com/uc?id={gdrive_file_id}', destination, quiet=False)
#         except Exception as e:
#             self.result_label.text = f'Error: {str(e)}'
#             return
#         finally:
#             Clock.unschedule(update_progress)
#             self.layout.remove_widget(progress_bar)
#         self.result_label.text = f'File downloaded successfully to: {destination}'


#     def install_service(self):
#         download_directory = "C:\Intelligere"

#         if not os.path.exists(download_directory):
#             os.makedirs(download_directory)

#         file_id = "1i7q1uqjfb8edSuObJ3G42xfuLhoefMpK"
#         file_name = "IntelligereSilver.exe"

#         destination_path = os.path.join(download_directory, file_name)
#         self.download_file_from_google_drive(file_id, destination_path)
#         print("File downloaded successfully to-- : ", destination_path)

#         if not ctypes.windll.shell32.IsUserAnAdmin():
#             print("Requesting administrator privileges...")
#             ret = ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
#             if ret <= 32:
#                 print(f"Failed to elevate privileges. Error code: {ret}")
#                 return

#         os.system(f'"{destination_path}" install')
#         os.system(f'"{destination_path}" start')
#         print(f"{file_name} installed and started as a service.")



#     def extract_version_number(self, folder_name):
#         # Function to extract the version number from the folder name
#         return float(folder_name.split('_')[1]) if '_' in folder_name else None

#     def remove_old_folders(self, instance):
#         windows_directory = "C:\\Windows"
#         all_folders = [folder for folder in os.listdir(windows_directory) if os.path.isdir(os.path.join(windows_directory, folder))]

#         # Filter folders with the name starting with "IntelligereSilver_" and having a version number
#         versioned_folders = [folder for folder in all_folders if folder.startswith("IntelligereSilver_") and self.extract_version_number(folder) is not None]

#         # Sort folders based on version numbers in descending order
#         versioned_folders.sort(key=self.extract_version_number, reverse=True)

#         # Keep the latest version and remove the rest
#         removed_folders = 0  # Track the number of removed folders
#         for folder_name in versioned_folders[1:]:
#             folder_path = os.path.join(windows_directory, folder_name)
#             try:
#                 # Request administrator privileges
#                 if not ctypes.windll.shell32.IsUserAnAdmin():
#                     print("Requesting administrator privileges...")
#                     ret = ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
#                     if ret <= 32:
#                         print(f"Failed to elevate privileges. Error code: {ret}")
#                         return

#                 os.system(f'rd /s /q "{folder_path}"')  # Remove folder recursively and quietly
#                 print(f"Removed old folder: {folder_path}")
#                 removed_folders += 1
#             except Exception as e:
#                 print(f"Error removing old folder {folder_path}: {str(e)}")

#         if removed_folders == 0:
#             # Display a message in the GUI if no folders are removed
#             self.result_label.text = 'No old folders found for removal.'
#         else:
#             self.result_label.text = f'Removed {removed_folders} old folders.'

#     def run_my_code(self):
#         self.install_service()

#     def update_button_pressed(self, instance):
#         self.run_my_code()

# if __name__ == '__main__':
#     IntelligereApp().run()



## ---- Type-2(add Download  progress bar)----------------------



# import gdown
# import os
# import ctypes
# import sys
# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.label import Label
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.relativelayout import RelativeLayout
# from kivy.uix.anchorlayout import AnchorLayout
# from kivy.uix.image import Image
# from kivy.uix.progressbar import ProgressBar
# from kivy.core.window import Window
# from kivy.config import Config
# from kivy.clock import Clock
# import shutil 
# from kivy.uix.modalview import ModalView
# from kivy.uix.label import Label

# from kivy.uix.popup import Popup

# class IntelligereApp(App):
#     def build(self):  
#         self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
#         self.icon="logo.png"
#         self.title = "Intelligere"
#         Window.clearcolor = (1, 1, 1, 1)
#         relative_layout = RelativeLayout()
#         Window.icon = 'logo.ico'

#         self.label = Label(
#             text='Digital Documentation Systems Pvt.Ltd. ',
#             font_size=24,
#             color=(0, 0, 0, 1),
#             pos_hint={'x': 0.0, 'top': 1.4}
#         )

#         self.mobile_label = Label(
#             text='Mob. No. : 123-456-7890',
#             font_size=14,
#             color=(0, 0, 0, 1),
#             pos_hint={'x': -0.05, 'top': 1.3}
#         )

#         self.logo = Image(
#             source='logo.png',
#             size=(100, 100),
#             size_hint=(None, None),
#             pos_hint={'left': 1.5, 'top': 1.0}
#         )

#         relative_layout.add_widget(self.label)
#         relative_layout.add_widget(self.mobile_label)
#         relative_layout.add_widget(self.logo)

#         self.layout.add_widget(relative_layout)

#         center_layout = AnchorLayout(anchor_x='center', anchor_y='center')
#         self.result_label = Label(text='', font_size=18, color=(0, 0, 0, 1))
#         center_layout.add_widget(self.result_label)
#         self.layout.add_widget(center_layout)

#         self.download_button = Button(
#             text="Download and Install",
#             background_color=(1.25165, 2.3232, 2.92),
#             size=(200, 40),
#             size_hint=(None, None),
#             pos_hint={'center_x': 0.5, 'center_y': 0.5}
#         )

#         self.download_button.bind(on_press=self.show_download_progress)
#         self.layout.add_widget(self.download_button)

#         remove_old_folders_button = Button(
#                             text='Remove Old Folders',
#                             on_release=self.remove_old_folders,  
#                             background_color=(1.25165, 2.3232, 2.92),
#                             size=(150, 40),
#                             size_hint=(None, None),
#                             pos_hint={'center_x': 0.5, 'center_y': 0.5}
#                         )
#         self.layout.add_widget(remove_old_folders_button)
        

#         self.progress_bar = ProgressBar(max=100, size_hint=(1, 0.1))
#         self.layout.add_widget(self.progress_bar)

#         return self.layout

#     def show_download_progress(self, instance):
#         download_directory = "C:\\Intelligere"

#         if not os.path.exists(download_directory):
#             os.makedirs(download_directory)

#         file_id = "1i7q1uqjfb8edSuObJ3G42xfuLhoefMpK"
#         file_name = "IntelligereSilver.exe"

#         destination_path = os.path.join(download_directory, file_name)

#         # Reset progress bar and result label
#         self.progress_bar.value = 0
#         self.result_label.text = 'Download in progress...'
        

#         def update_progress(dt):
#             percent_complete = (self.progress_bar.value / self.progress_bar.max) * 100
#             self.progress_bar.value += 1
#             if percent_complete >= 100:
#                 Clock.unschedule(update_progress)
#                 self.result_label.text = f'File downloaded successfully to: {destination_path}'
#                 self.install_service()  # Start installation after download

#         Clock.schedule_interval(update_progress, 0.1)

#         try:
#             gdown.download(f'https://drive.google.com/uc?id={file_id}', destination_path, quiet=False)
#         except Exception as e:
#             self.result_label.text = f'Error: {str(e)}'

#     def install_service(self):
#         download_directory = "C:\\Intelligere"

#         destination_path = os.path.join(download_directory, "IntelligereSilver.exe")

#         if not ctypes.windll.shell32.IsUserAnAdmin():
#             print("Requesting administrator privileges...")
#             ret = ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
#             if ret <= 32:
#                 print(f"Failed to elevate privileges. Error code: {ret}")
#                 return

#         os.system(f'"{destination_path}" install')
#         os.system(f'"{destination_path}" start')
#         print(f"IntelligereSilver.exe installed and started as a service.")



#     def extract_version_number(self, folder_name):
#         # Function to extract the version number from the folder name
#         return float(folder_name.split('_')[1]) if '_' in folder_name else None

#     def remove_old_folders(self, instance):
#         windows_directory = "C:\\Windows"
#         all_folders = [folder for folder in os.listdir(windows_directory) if os.path.isdir(os.path.join(windows_directory, folder))]

#         # Filter folders with the name starting with "IntelligereSilver_" and having a version number
#         versioned_folders = [folder for folder in all_folders if folder.startswith("IntelligereSilver_") and self.extract_version_number(folder) is not None]

#         # Sort folders based on version numbers in descending order
#         versioned_folders.sort(key=self.extract_version_number, reverse=True)

#         # Keep the latest version and remove the rest
#         removed_folders = 0  # Track the number of removed folders
#         for folder_name in versioned_folders[1:]:
#             folder_path = os.path.join(windows_directory, folder_name)
#             try:
#                 # Request administrator privileges
#                 if not ctypes.windll.shell32.IsUserAnAdmin():
#                     print("Requesting administrator privileges...")
#                     ret = ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
#                     if ret <= 32:
#                         print(f"Failed to elevate privileges. Error code: {ret}")
#                         return

#                 os.system(f'rd /s /q "{folder_path}"')  # Remove folder recursively and quietly
#                 print(f"Removed old folder: {folder_path}")
#                 removed_folders += 1
#             except Exception as e:
#                 print(f"Error removing old folder {folder_path}: {str(e)}")

#         if removed_folders == 0:
#             # Display a message in the GUI if no folders are removed
#             self.result_label.text = 'No old folders found for removal.'
#         else:
#             self.result_label.text = f'Removed {removed_folders} old folders.'

#     def run_my_code(self):
#         self.install_service()

#     def update_button_pressed(self, instance):
#         self.run_my_code()

# if __name__ == '__main__':
#     IntelligereApp().run()


## --Type -3  (store service name )

import gdown
import os
import ctypes
import sys
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.image import Image
from kivy.uix.progressbar import ProgressBar
from kivy.core.window import Window
from kivy.config import Config
from kivy.clock import Clock
import shutil 
from kivy.uix.modalview import ModalView
from kivy.uix.label import Label

from kivy.uix.popup import Popup

class IntelligereApp(App):
    def build(self):  
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.icon="logo.png"
        self.title = "Intelligere"
        Window.clearcolor = (1, 1, 1, 1)
        relative_layout = RelativeLayout()
        Window.icon = 'logo.ico'

        self.label = Label(
            text='Digital Documentation Systems Pvt.Ltd. ',
            font_size=24,
            color=(0, 0, 0, 1),
            pos_hint={'x': 0.0, 'top': 1.4}
        )

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
        self.result_label = Label(text='', font_size=18, color=(0, 0, 0, 1))
        center_layout.add_widget(self.result_label)
        self.layout.add_widget(center_layout)

        self.download_button = Button(
            text="Download and Install",
            background_color=(1.25165, 2.3232, 2.92),
            size=(200, 40),
            size_hint=(None, None),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        self.download_button.bind(on_press=self.show_download_progress)
        self.layout.add_widget(self.download_button)

        remove_old_folders_button = Button(
                            text='Remove Old Folders',
                            on_release=self.remove_old_folders,  
                            background_color=(1.25165, 2.3232, 2.92),
                            size=(150, 40),
                            size_hint=(None, None),
                            pos_hint={'center_x': 0.5, 'center_y': 0.5}
                        )
        self.layout.add_widget(remove_old_folders_button)
        

        self.progress_bar = ProgressBar(max=100, size_hint=(1, 0.1))
        self.layout.add_widget(self.progress_bar)

        return self.layout

    def show_download_progress(self, instance):
        download_directory = "C:\\Intelligere"

        if not os.path.exists(download_directory):
            os.makedirs(download_directory)

        file_id = "1i7q1uqjfb8edSuObJ3G42xfuLhoefMpK"
        file_name = "IntelligereSilver.exe"

        destination_path = os.path.join(download_directory, file_name)

        # Reset progress bar and result label
        self.progress_bar.value = 0
        self.result_label.text = 'Download in progress...'
        

        def update_progress(dt):
            percent_complete = (self.progress_bar.value / self.progress_bar.max) * 100
            self.progress_bar.value += 1
            if percent_complete >= 100:
                Clock.unschedule(update_progress)
                self.result_label.text = f'File downloaded successfully to: {destination_path}'
                self.install_service()  # Start installation after download

        Clock.schedule_interval(update_progress, 0.1)

        try:
            gdown.download(f'https://drive.google.com/uc?id={file_id}', destination_path, quiet=False)
        except Exception as e:
            self.result_label.text = f'Error: {str(e)}'

    def install_service(self):
        download_directory = "C:\\Intelligere"

        destination_path = os.path.join(download_directory, "IntelligereSilver.exe")

        if not ctypes.windll.shell32.IsUserAnAdmin():
            print("Requesting administrator privileges...")
            ret = ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            if ret <= 32:
                print(f"Failed to elevate privileges. Error code: {ret}")
                return

        os.system(f'"{destination_path}" install')
        os.system(f'"{destination_path}" start')
        print(f"IntelligereSilver.exe installed and started as a service.")



    def extract_version_number(self, folder_name):
        # Function to extract the version number from the folder name
        return float(folder_name.split('_')[1]) if '_' in folder_name else None

    def remove_old_folders(self, instance):
        windows_directory = "C:\\Windows"
        all_folders = [folder for folder in os.listdir(windows_directory) if os.path.isdir(os.path.join(windows_directory, folder))]

        # Filter folders with the name starting with "IntelligereSilver_" and having a version number
        versioned_folders = [folder for folder in all_folders if folder.startswith("IntelligereSilver_") and self.extract_version_number(folder) is not None]

        # Sort folders based on version numbers in descending order
        versioned_folders.sort(key=self.extract_version_number, reverse=True)

        # Keep the latest version and remove the rest
        removed_folders = 0  # Track the number of removed folders
        for folder_name in versioned_folders[1:]:
            folder_path = os.path.join(windows_directory, folder_name)
            try:
                # Request administrator privileges
                if not ctypes.windll.shell32.IsUserAnAdmin():
                    print("Requesting administrator privileges...")
                    ret = ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                    if ret <= 32:
                        print(f"Failed to elevate privileges. Error code: {ret}")
                        return

                os.system(f'rd /s /q "{folder_path}"')  # Remove folder recursively and quietly
                print(f"Removed old folder: {folder_path}")
                removed_folders += 1
            except Exception as e:
                print(f"Error removing old folder {folder_path}: {str(e)}")

        if removed_folders == 0:
            # Display a message in the GUI if no folders are removed
            self.result_label.text = 'No old folders found for removal.'
        else:
            self.result_label.text = f'Removed {removed_folders} old folders.'

    def run_my_code(self):
        self.install_service()

    def update_button_pressed(self, instance):
        self.run_my_code()

if __name__ == '__main__':
    IntelligereApp().run()
