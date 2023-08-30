from bim.utils import qt

from bim.ui import ui_setup
from bim import gui


class Tweak(ui_setup.Setup):
    def __init__(self):
        super(Tweak, self).__init__()

        self.frame_widget_toggle = False

        self.act_reset.triggered.connect(gui.show)
        self.act_reset.setShortcut("Shift+`")

        self.act_expand_all.triggered.connect(self.toggle_frame_widgets)


    def toggle_frame_widgets(self):
        for frame_btn in self.frame_widgets:
            frame_btn.set_toggle(self.frame_widget_toggle)
        self.frame_widget_toggle = not self.frame_widget_toggle
        self.act_expand_all.setText("🙂" if self.frame_widget_toggle else "😮")