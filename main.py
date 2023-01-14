import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class GridWindow(Gtk.Window):
    def __init__(self):

        super().__init__(title="Grid Example")

        index = 0
        grid = Gtk.Grid()

        while index < 9:
            button = Gtk.Button(label=f"Button {index}")
            if index < 3:
                grid.attach(button, index, 0, 1, 1)
            elif 2 < index < 6:
                grid.attach(button, index-3, 1, 1, 1)
            elif 5 < index < 9:
                grid.attach(button, index-6, 2, 1, 1)
            index += 1

        button0 = Gtk.Button(label="Button 0")
        grid.attach(button0, 0, 3, 3, 1)

        self.add(grid)


win = GridWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
