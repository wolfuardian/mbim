# -*- coding: utf-8 -*-
import os
import getpass
import maya.cmds as cmds

import bim.tools as tools

env_dir = f"C:/Users/{getpass.getuser()}/PycharmProjects"

mod = "mbim"
mod_ver = "0.1"
mod_dir = f"{env_dir}/{mod}"

maya_ver = "2023"
maya_mod_dir = f"C:/Users/{getpass.getuser()}/Documents/maya/{maya_ver}/modules"
maya_mod_file = f"{maya_mod_dir}/{mod}.mod"


def uninstall():
    try:
        tools.Logging.fileio_logger().info(f"Removing module file: {maya_mod_file}")
        os.remove(maya_mod_file)

    except WindowsError:
        tools.Logging.fileio_logger().error(f"MBIM module file does not exist.")

    tools.Logging.installer_logger().info("Removing MBIM preferences")
    tools.Registry.delete_subkey("Software", "MBIM")

    tools.Logging.maya_logger().info("Removing MBIM shelf tab and button")
    shelf_buttons = cmds.shelfLayout("MBIM", query=True, childArray=True)
    if shelf_buttons:
        for button in shelf_buttons:
            cmds.deleteUI(button, control=True)
    if cmds.layout("MBIM", exists=True):
        cmds.deleteUI("MBIM", layout=True)


if __name__ == "__main__":
    uninstall()
