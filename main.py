import os
from kivy.lang import Builder
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.list import TwoLineListItem

KV = '''
MDBoxLayout:
    orientation: 'vertical'
    md_bg_color: 0.05, 0.05, 0.05, 1

    MDTopAppBar:
        title: "Mister-Flasheur IA Player"
        md_bg_color: 0.1, 0.1, 0.1, 1
        elevation: 4

    MDBoxLayout:
        adaptive_height: True
        padding: "10dp"
        spacing: "8dp"
        MDTextField:
            id: search_field
            hint_text: "Demandez à l'IA..."
            mode: "round"
            fill_color_normal: 0.15, 0.15, 0.15, 1
        MDIconButton:
            icon: "microphone"
            md_bg_color: 0.2, 0.4, 0.9, 1
            on_release: app.commande_vocale()
        MDIconButton:
            icon: "music-note-search"
            md_bg_color: 0.8, 0.2, 0.2, 1
            on_release: app.recherche_fredonnement()

    MDTabs:
        id: tabs
        on_tab_switch: app.on_tab_switch(*args)
        background_color: 0.1, 0.1, 0.1, 1

    ScrollView:
        MDList:
            id: song_list

    MDCard:
        orientation: 'vertical'
        size_hint_y: None
        height: "180dp"
        md_bg_color: 0.1, 0.1, 0.1, 1
        radius: [25, 25, 0, 0]
        padding: "15dp"

        MDSlider:
            id: progress_bar
            min: 0
            max: 100
            value: 0
            color: 0.2, 0.6, 1, 1
            on_touch_up: if self.collide_point(*args[1].pos): app.seek_music(self.value)

        MDBoxLayout:
            orientation: 'horizontal'
            MDLabel:
                id: current_song_label
                text: "Sélectionnez un titre"
                theme_text_color: "Primary"
                bold: True
            MDLabel:
                text: "Mister-Flasheur dj Émmato on the beat"
                theme_text_color: "Secondary"
                font_style: "Caption"
                halign: "right"

        MDBoxLayout:
            orientation: 'horizontal'
            adaptive_height: True
            spacing: "20dp"
            pos_hint: {"center_x": .5}
            MDIconButton:
                icon: "skip-previous"
                icon_size: "40dp"
            MDIconButton:
                id: play_btn
                icon: "play-circle"
                icon_size: "60dp"
                on_release: app.toggle_play()
            MDIconButton:
                icon: "skip-next"
                icon_size: "40dp"

<Tab>:
'''

class Tab(FloatLayout, MDTabsBase):
    pass

class MusicApp(MDApp):
    sound = None
    music_files = []

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.ui = Builder.load_string(KV)
        for name in ["ARTISTES", "ALBUMS", "PLAYLISTS"]:
            self.ui.ids.tabs.add_widget(Tab(title=name))
        return self.ui

    def on_start(self):
        self.scan_music()

    def scan_music(self):
        path = "/storage/emulated/0/Music"
        if os.path.exists(path):
            for file in os.listdir(path):
                if file.endswith(".mp3"):
                    self.music_files.append(os.path.join(path, file))
                    item = TwoLineListItem(
                        text=file.replace(".mp3", ""),
                        secondary_text="Musique Locale",
                        on_release=lambda x, p=os.path.join(path, file), t=file: self.play_music(p, t)
                    )
                    self.ui.ids.song_list.add_widget(item)

    def play_music(self, path, title):
        if self.sound:
            self.sound.stop()
        self.sound = SoundLoader.load(path)
        if self.sound:
            self.ui.ids.current_song_label.text = title
            self.ui.ids.play_btn.icon = "pause-circle"
            self.sound.play()
            self.ui.ids.progress_bar.max = self.sound.length
            Clock.schedule_interval(self.update_progress, 1)

    def toggle_play(self):
        if self.sound:
            if self.sound.state == 'play':
                self.sound.stop()
                self.ui.ids.play_btn.icon = "play-circle"
            else:
                self.sound.play()
                self.ui.ids.play_btn.icon = "pause-circle"

    def update_progress(self, dt):
        if self.sound and self.sound.state == 'play':
            self.ui.ids.progress_bar.value = self.sound.get_pos()

    def seek_music(self, value):
        if self.sound:
            self.sound.seek(value)

    def on_tab_switch(self, *args):
        pass

    def commande_vocale(self):
        print("L'IA écoute pour lancer une musique...")

    def recherche_fredonnement(self):
        print("L'IA écoute votre fredonnement...")

if __name__ == "__main__":
    MusicApp().run()
