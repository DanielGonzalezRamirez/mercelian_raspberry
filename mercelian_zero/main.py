import sys

from threading import Thread
from PyQt5.QtWidgets import QApplication
from GUI.main_window import MainWindow
from Variables.variables import Variables

import Functions.configuration as configuration
import Functions.timers as timers

if __name__ == '__main__':
    valve_config_file = '/home/daniel/Projects/mercelian_zero/ConfigurationFiles/config_valves.csv'
    pump_config_file = '/home/daniel/Projects/mercelian_zero/ConfigurationFiles/config_pump.csv'

    app = QApplication(sys.argv)
    Variables.window = MainWindow()
    configuration.load_config()
    t = Thread(target=timers.check_timer)
    t.start()
    sys.exit(app.exec_())