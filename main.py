#!/usr/bin/env python3

## Password Generator Android App
## Developer: https://github.com/Izolabela

# Imports
import random
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.actionbar import ActionBar, ActionButton
from kivy.uix.popup import Popup

# App class
class UmApp(App):

    # Build Method
    def build(self):

        # Main Layout
        layout = FloatLayout(
        )

        # Action bar
        self.ActionBar = ActionBar(
            background_color = "00FF00",
            size_hint = (1, 1),
            pos_hint = {"top": 1},
        )


        # Logo widget
        self.Logo = Image(
            source = "logo.png",
            size_hint = (1, 1),
            pos_hint = {"center_x": 0.5, "center_y":0.7},

        )

        # Text widget
        self.Text = Label(
            text = "[b]Let's Make a [color=00FF00]Password[/color] For You[/b]",
            font_size = 18,
            color = '#FFFFFF',
            halign = "center",
            size_hint = (0.5, 0.5),
            markup = True,
            pos_hint = {"center_x": 0.5, "center_y":0.5}
        )
        
        # Input widget
        self.Output = TextInput(
            multiline = False,
            halign = "center",
            background_color = "#111111",
            foreground_color = "FFFFFF",
            cursor_color = "00FF00",
            size_hint = (0.4, None),
            height = "30dp",
            pos_hint = {"center_x": 0.5, "center_y":0.3}
        )

        # Generate Button widget
        self.GButton = Button(
            text = "Make",
            size_hint = (0.2, None),
            height = "40dp",
            pos_hint = {"center_x": 0.4, "center_y":0.2},
            bold = True,
            background_color ='#00FF00',
            on_press = self.make
        )

        # Clear Button widget
        self.CButton = Button(
            text = "Clear",
            size_hint = (0.2, None),
            height = "40dp",
            pos_hint = {"center_x": 0.6, "center_y":0.2},
            bold = True,
            background_color ='#00FF00',
            on_press = self.clear
        )

        # Add widgets
        layout.add_widget(self.ActionBar)
        layout.add_widget(self.Logo)
        layout.add_widget(self.Text)
        layout.add_widget(self.Output)
        layout.add_widget(self.GButton)
        layout.add_widget(self.CButton)

        # Return home Layout
        return layout

    # Make password method
    def make(self, *args):
        words = "0qaDzSw2FsxGe3AHdcZrJ4XfvCtg5KbyV6LW$MBNh7QnuEY#8TRjmik9olpPOI@U!"
        self.Output.text = "".join(random.choices(words, k=8))

    # Clear Output
    def clear(self, *args):
        self.Output.text = ""

# Run
UmApp().run()
