import logging

import bim.core.tools as core
import bim.tools as tools

class Logging(core.Logging):
    @classmethod
    def installer_logger(cls):
        return logging.getLogger("Installer")

    @classmethod
    def registry_logger(cls):
        return logging.getLogger("Registry")

    @classmethod
    def fileio_logger(cls):
        return logging.getLogger("FileIO")

    @classmethod
    def maya_logger(cls):
        return logging.getLogger("Maya")

    @classmethod
    def gui_logger(cls):
        return logging.getLogger("GUI")

    @classmethod
    def packages_logger(cls):
        return logging.getLogger("Packages")

