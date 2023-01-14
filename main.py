import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class GridWindow(Gtk.Window):
    def __init__(self):

        super().__init__(title="Grid Example")

        button1 = Gtk.Button(label="Button 1")
        button2 = Gtk.Button(label="Button 2")
        button3 = Gtk.Button(label="Button 3")
        button4 = Gtk.Button(label="Button 4")
        button5 = Gtk.Button(label="Button 5")
        button6 = Gtk.Button(label="Button 6")
        button7 = Gtk.Button(label="Button 7")
        button8 = Gtk.Button(label="Button 8")
        button9 = Gtk.Button(label="Button 9")
        button0 = Gtk.Button(label="Button 0")

        grid = Gtk.Grid()
        grid.attach(button1, 0, 0, 1, 1)
        grid.attach(button2, 1, 0, 1, 1)
        grid.attach(button3, 2, 0, 1, 1)
        grid.attach(button4, 0, 1, 1, 1)
        grid.attach(button5, 1, 1, 1, 1)
        grid.attach(button6, 2, 1, 1, 1)
        grid.attach(button7, 0, 2, 1, 1)
        grid.attach(button8, 1, 2, 1, 1)
        grid.attach(button9, 2, 2, 1, 1)

        grid.attach(button0, 0, 3, 3, 1)

        self.add(grid)


win = GridWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
