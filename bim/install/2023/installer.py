# -*- coding: utf-8 -*-
import os
import getpass
from bim.utils.logging import installer_logger, fileio_logger, maya_logger
from bim.utils.registry import Registry
import maya.cmds as cmds
import maya.mel as mel

env_dir = f"C:/Users/{getpass.getuser()}/PycharmProjects"

mod = "mbim"
mod_ver = "0.1"
mod_dir = f"{env_dir}/{mod}"

maya_ver = "2023"
maya_mod_dir = f"C:/Users/{getpass.getuser()}/Documents/maya/{maya_ver}/modules"
maya_mod_file = f"{maya_mod_dir}/{mod}.mod"


def install():
    if not os.path.exists(maya_mod_dir):
        fileio_logger.info(f"Creating module folder: {maya_mod_dir}")
        os.makedirs(maya_mod_dir)

    command = f"""+ {mod} {mod_ver} {mod_dir}
scripts: {mod_dir}"""

    fileio_logger.info(f"Creating module file: {maya_mod_file}")
    fp = open(maya_mod_file, "w")
    fp.write(command)
    fp.close()

    installer_logger.info("Saving MBIM preferences")
    Registry.set_value("Software", "MBIM", "Pref_ModuleName", mod)
    Registry.set_value("Software", "MBIM", "Pref_ModuleEnvDirectory", env_dir)
    Registry.set_value("Software", "MBIM", "Pref_ModuleProjectDirectory", mod_dir)
    Registry.set_value("Software", "MBIM", "Pref_MayaVersion", maya_ver)
    Registry.set_value("Software", "MBIM", "Pref_MayaModuleFolder", maya_mod_dir)
    Registry.set_value("Software", "MBIM", "Pref_MayaModuleFile", maya_mod_file)

    if not cmds.layout("MBIM", exists=True):
        maya_logger.info("Creating MBIM shelf tab")
        mel.eval('addNewShelfTab("MBIM");')

    command = """from bim import gui
gui.show()"""

    icon_path = "/execute.png"

    shelf_mbim = cmds.shelfLayout("MBIM", query=True, childArray=True)
    if shelf_mbim:
        maya_logger.info("Clearing MBIM shelf buttons")
        for button in shelf_mbim:
            cmds.deleteUI(button, control=True)

    maya_logger.info("Creating MBIM shelf button")
    cmds.shelfButton(
        annotation="Run",
        image1=icon_path,
        command=command,
        parent="MBIM",
        label="run",
    )


if __name__ == "__main__":
    install()
