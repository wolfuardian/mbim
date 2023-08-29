# -*- coding: utf-8 -*-
import os
import getpass
import maya.mel as mel
import maya.cmds as cmds

import bim.tools as tools


env_dir = f"C:/Users/{getpass.getuser()}/PycharmProjects"

mod = "mbim"
mod_ver = "0.1"
mod_dir = f"{env_dir}/{mod}"

maya_ver = "2023"
maya_mod_dir = f"C:/Users/{getpass.getuser()}/Documents/maya/{maya_ver}/modules"
maya_mod_file = f"{maya_mod_dir}/{mod}.mod"


def install():
    if not os.path.exists(maya_mod_dir):
        tools.Logging.fileio_logger().info(f"Creating module folder: {maya_mod_dir}")
        os.makedirs(maya_mod_dir)

    command = f"""+ {mod} {mod_ver} {mod_dir}
scripts: {mod_dir}"""

    tools.Logging.fileio_logger().info(f"Creating module file: {maya_mod_file}")
    fp = open(maya_mod_file, "w")
    fp.write(command)
    fp.close()

    tools.Logging.installer_logger().info("Saving MBIM preferences")
    tools.Registry.set_value("Software", "MBIM", "Pref_ModuleName", mod)
    tools.Registry.set_value("Software", "MBIM", "Pref_ModuleEnvDirectory", env_dir)
    tools.Registry.set_value("Software", "MBIM", "Pref_ModuleProjectDirectory", mod_dir)
    tools.Registry.set_value("Software", "MBIM", "Pref_MayaVersion", maya_ver)
    tools.Registry.set_value("Software", "MBIM", "Pref_MayaModuleFolder", maya_mod_dir)
    tools.Registry.set_value("Software", "MBIM", "Pref_MayaModuleFile", maya_mod_file)

    if not cmds.layout("MBIM", exists=True):
        tools.Logging.maya_logger().info("Creating MBIM shelf tab")
        mel.eval('addNewShelfTab("MBIM");')

    command = """from bim import gui
gui.show()"""

    icon_path = "/execute.png"

    shelf_mbim = cmds.shelfLayout("MBIM", query=True, childArray=True)
    if shelf_mbim:
        tools.Logging.maya_logger().info("Clearing MBIM shelf buttons")
        for button in shelf_mbim:
            cmds.deleteUI(button, control=True)

    tools.Logging.maya_logger().info("Creating MBIM shelf button")
    cmds.shelfButton(
        annotation="Run",
        image1=icon_path,
        command=command,
        parent="MBIM",
        label="run",
    )


if __name__ == "__main__":
    install()
