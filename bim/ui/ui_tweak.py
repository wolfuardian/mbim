from bim.ui import ui_setup
from bim import gui


class Tweak(ui_setup.Setup):
    def __init__(self):
        super(Tweak, self).__init__()

        self.bar_main_reset.triggered.connect(gui.show)
        self.bar_main_reset.setShortcut('Alt+`')

        self.bar_undo.triggered.connect(gui.undo)
        self.bar_redo.triggered.connect(gui.redo)
