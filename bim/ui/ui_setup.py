from maya.app.general import mayaMixin
from bim.utils import qt

import bim.tools as tools
import bim.module as module

class Setup(mayaMixin.MayaQWidgetDockableMixin, mayaMixin.MayaQWidgetBaseMixin, qt.QtDefaultCSWidget):
    def __init__(self, parent=tools.Maya.get_main_window()):
        super(Setup, self).__init__(parent)

        self.setWindowTitle("MaBIM-v230618")
        self.setMinimumWidth(360)

        layout = qt.QtWidgets.QVBoxLayout()
        layout.setAlignment(qt.QtCore.Qt.AlignTop)
        layout.setContentsMargins(3, 3, 3, 3)
        layout.setSpacing(0)

        # <editor-fold desc="CODE_BLOCK: Create Widget">
        bar = qt.QtWidgets.QMenuBar()

        bar_main = bar.addMenu("功能選單")
        bar_undo = qt.QtWidgets.QAction("/ 復原")
        bar_redo = qt.QtWidgets.QAction("/ 重做")
        m_help = bar.addMenu("👈 懶人用")
        m_help.setEnabled(False)

        bar_main_reset = qt.QtWidgets.QAction("重新載入")

        tab = qt.QtTabCSWidget()
        tab_opt = qt.QtTabItemCSWidget()

        frm_opt_mats = qt.QtFrameLayoutCSWidget(text="材質球　⚽")

        # ui_opt_mats = module.OptimizeMaterialsCSWidget()
        # </editor-fold>

        # <editor-fold desc="CODE_BLOCK: Assembly Widget">
        tab_opt.layout.addWidget(frm_opt_mats)

        tab.addTab(tab_opt, "最佳化")

        # frm_opt_mats.frame_layout.addWidget(ui_opt_mats)

        layout.addWidget(tab)

        bar_main.addAction(bar_main_reset)
        bar.addMenu(bar_main)
        bar.addAction(bar_undo)
        bar.addAction(bar_redo)
        bar.addMenu(m_help)

        self.setLayout(layout)

        self.layout().setMenuBar(bar)
        # </editor-fold>

        # <editor-fold desc="CODE_BLOCK: Public Variable">
        self.layout = layout

        self.bar = bar
        self.bar_main = bar_main
        self.bar_undo = bar_undo
        self.bar_redo = bar_redo
        self.bar_main_reset = bar_main_reset

        self.tab = tab
        self.tab_tool = tab_opt

        self.frm_optimize = frm_opt_mats

        # self.ui_optimize = ui_opt_mats

        # </editor-fold>
