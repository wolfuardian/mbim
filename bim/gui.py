from maya import cmds
from bim.ui import ui_tweak
from bim.tools import packages

import bim.tools as tools

global instance


def show():
    global instance
    tools.Logging.gui_logger().info("Reloading mbim packages")
    tools.Packages.reload(packages=["bim"])

    try:
        if instance:
            tools.Logging.gui_logger().info("Cleaning existing GUI")
            instance.close()
            instance.deleteLater()
            instance = ui_tweak.Tweak()
            instance.update()
            tools.Logging.gui_logger().info("Showing GUI")
            instance.show(dockable=True, area='left')

    except NameError:
        instance = ui_tweak.Tweak()
        tools.Logging.gui_logger().warning("NameError")
        tools.Logging.gui_logger().info("Showing GUI")
        show()

    except RuntimeError:
        instance = ui_tweak.Tweak()
        tools.Logging.gui_logger().warning("RuntimeError")
        tools.Logging.gui_logger().info("Showing GUI")
        show()


def undo():
    tools.Logging.maya_logger().info("Operating undo")
    cmds.undo()


def redo():
    tools.Logging.maya_logger().info("Operating redo")
    cmds.redo()
