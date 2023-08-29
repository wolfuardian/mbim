# -*- coding: utf-8 -*-
import os
import getpass
from bim.utils.logging import installer_logger, fileio_logger
from bim.utils.registry import Registry

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


def uninstall():
    try:
        fileio_logger.info(f"Removing module file: {maya_mod_file}")
        os.remove(maya_mod_file)

    except WindowsError:
        fileio_logger.error(f"MBIM module file does not exist.")

    installer_logger.info("Removing MBIM preferences")
    Registry.delete_subkey("Software", "MBIM")


if __name__ == "__main__":
    install()
