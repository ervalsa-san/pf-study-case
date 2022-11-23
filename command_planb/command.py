from abc import ABCMeta, abstractstaticmethod

class DarkMode:

    def Turn_On(self):
        print("Dark Mode ON")

    def Turn_Off(self):
        print("Dark Mode OFF")

class Command(metaclass=ABCMeta):

    @abstractstaticmethod
    def execute():
        """Static Methode"""

class SwitchOnCommand(Command):

    def __init__(self, darkmode):
        self._darkmode = darkmode

    def execute(self):
        self._darkmode.Turn_On()

class SwitchOffCommand(Command):
    def __init__(self, darkmode):
        self._darkmode = darkmode

    def execute(self):
        self._darkmode.Turn_Off()

class Switch:

    def __init__(self):
        self._commands = {}

    def register(self, command_name, command):
        self._commands[command_name] = command

    def execute(self, command_name):
        if command_name in self._commands:
            self._commands[command_name].execute()
        else:
            print("Command Not Found")

if __name__ == "__main__":
    DARKMODE = DarkMode()

    TURN_ON = SwitchOnCommand(DARKMODE)
    TURN_OFF = SwitchOffCommand(DARKMODE)

    SWITCH = Switch()
    SWITCH.register("ON", TURN_ON)
    SWITCH.register("OFF", TURN_OFF)

    SWITCH.execute("ON")
    SWITCH.execute("OFF")