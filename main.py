import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class GridWindow(Gtk.Window):
    def __init__(self):

        super().__init__(title="Grid Example")

        index = 0
        grid = Gtk.Grid()

        entry = Gtk.Entry()
        grid.attach(entry, 0, 0, 3, 1)

        while index < 10:
            button = Gtk.Button(label=f"{index}")
            if index < 3:
                grid.attach(button, index, 1, 1, 1)
            elif 2 < index < 6:
                grid.attach(button, index-3, 2, 1, 1)
            elif 5 < index < 9:
                grid.attach(button, index-6, 3, 1, 1)
            index += 1

        button_dot = Gtk.Button(label=".")
        button0 = Gtk.Button(label="0")
        button_eq = Gtk.Button(label="=")
        grid.attach(button_dot, 0, 4, 1, 1)
        grid.attach(button0, 1, 4, 1, 1)
        grid.attach(button_eq, 2, 4, 1, 1)

        button_c = Gtk.Button(label="C")
        button_plus = Gtk.Button(label="+")
        button_minus = Gtk.Button(label="-")
        button_mult = Gtk.Button(label="*")
        button_div = Gtk.Button(label="/")
        grid.attach(button_c, 4, 0, 1, 1)
        grid.attach(button_plus, 4, 1, 1, 1)
        grid.attach(button_minus, 4, 2, 1, 1)
        grid.attach(button_mult, 4, 3, 1, 1)
        grid.attach(button_div, 4, 4, 1, 1)

        self.add(grid)


win = GridWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
