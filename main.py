from kivy.app import App
from kivy.lang import Builder
from datetime import datetime

reservations = {}


def make_reservation(instance):
    date_str = instance.parent.ids.date_input.text
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        if date in reservations:
            instance.parent.ids.message.text = "Date already in use."
        else:
            reservations[date] = True
            instance.parent.ids.message.text = "Reservation successful."
    except ValueError:
        instance.parent.ids.message.text = "Invalid format. use YYYY-MM-DD."


kv = """
BoxLayout:
    orientation: 'vertical'
    Label:
        id: label
        text: "Enter a date (YYYY-MM-DD):"
    TextInput:
        id: date_input
        multiline: False
    Button:
        text: "Make Reservation"
        on_press: app.make_reservation(self)
    Label:
        id: message
        text: ""
"""


class ReservationApp(App):
    def build(self):
        return Builder.load_string(kv)

    def make_reservation(self, instance):
        make_reservation(instance)


if __name__ == "__main__":
    ReservationApp().run()
