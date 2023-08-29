# -*- coding: utf-8 -*-
import os
import getpass
from bim.utils.logging import installer_logger, fileio_logger, maya_logger
from bim.utils.registry import Registry
import maya.cmds as cmds

env_dir = f"C:/Users/{getpass.getuser()}/PycharmProjects"

mod = "mbim"
mod_ver = "0.1"
mod_dir = f"{env_dir}/{mod}"

maya_ver = "2023"
maya_mod_dir = f"C:/Users/{getpass.getuser()}/Documents/maya/{maya_ver}/modules"
maya_mod_file = f"{maya_mod_dir}/{mod}.mod"


def uninstall():
    try:
        fileio_logger.info(f"Removing module file: {maya_mod_file}")
        os.remove(maya_mod_file)

    except WindowsError:
        fileio_logger.error(f"MBIM module file does not exist.")

    installer_logger.info("Removing MBIM preferences")
    Registry.delete_subkey("Software", "MBIM")

    maya_logger.info("Removing MBIM shelf tab and button")
    shelf_buttons = cmds.shelfLayout("MBIM", query=True, childArray=True)
    if shelf_buttons:
        for button in shelf_buttons:
            cmds.deleteUI(button, control=True)
    if cmds.layout("MBIM", exists=True):
        cmds.deleteUI("MBIM", layout=True)


if __name__ == "__main__":
    uninstall()
