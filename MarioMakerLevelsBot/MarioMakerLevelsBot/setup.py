import sys
from cx_Freeze import setup, Executable

exe = Executable(
    script="MarioMakerLevelsBot.py",
    initScript=None,
    base='Win32GUI',
    targetDir="dist",
    targetName="MarioMakerLevelsBot.exe",
    compress=True,
    copyDependentFiles=True,
    appendScriptToExe=True,
    appendScriptToLibrary=False,
    icon="ui/MarioMakerLevelsBot.ico", # TODO: add an icon?
    )

setup(
    version=1.0,
    name="MarioMakerLevelsBot",
    author="Raphaël Lejolivet",
    description="Pulls levels from Twitch chat into a pretty interface",

    options = {"build_exe": {"path": sys.path,
                             "append_script_to_exe":False,
                             "build_exe":"dist/bin",
                             "compressed":True,
                             "copy_dependent_files":True,
                             "create_shared_zip":True,
                             "include_in_shared_zip":True,
                             "optimize":2,
                             }
               },

    executables = [exe]
    )