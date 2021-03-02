import os
import time
import datetime
import schedule
import threading
import pandas as pd
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from GUI.status_widget import StatusWidget
from GUI.valves_widget import ValvesWidget
from GUI.pump_widget import PumpWidget
from Variables.variables import Variables

import Functions.configuration as configuration


class MainWindow(QWidget):
    def __init__(self):
        # Inicializacion de la superclase
        super().__init__()
        # Inicializacion de la lista con los procesos
        self.processes = []
        # Inicializacion de la variable para la ruta del archivo de configuracion
        self.configfilepath = None
        # Inicializacion de los widgets de la interfaz
        self.widget_valves = ValvesWidget(p_parent=self)
        self.widget_pump = PumpWidget(p_parent=self)
        self.widget_status = StatusWidget(p_parent=self)
        # Conexion de las senales de los paneles con sus slots
        self.widget_status.check_valve_4_man_auto.stateChanged.connect(self.manual_check)
        # Inicializacion de los layout temporales y se agregan los widgets
        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()
        main_layout = QHBoxLayout()

        left_layout.addWidget(self.widget_valves)
        left_layout.addWidget(self.widget_pump)
        right_layout.addWidget(self.widget_status)

        main_layout.addLayout(left_layout, stretch=3)
        main_layout.addLayout(right_layout, stretch=3)
        self.setLayout(main_layout)
        self.showMaximized()
        self.setWindowTitle('MERCELIAN - Irrigation Control')
        self.show()

    def manual_check(self):
        variables = Variables()
        config_file_valves = pd.read_csv(variables.config_file_valves)

        status_checks = [self.widget_status.check_valve_1_man_auto,
                         self.widget_status.check_valve_2_man_auto,
                         self.widget_status.check_valve_3_man_auto,
                         self.widget_status.check_valve_4_man_auto,
                         self.widget_status.check_valve_5_man_auto,
                         self.widget_status.check_valve_6_man_auto,
                         self.widget_status.check_valve_7_man_auto,
                         self.widget_status.check_valve_7_man_auto]

        manual_buttons = [self.widget_status.button_valve_1_manual_action,
                          self.widget_status.button_valve_2_manual_action,
                          self.widget_status.button_valve_3_manual_action,
                          self.widget_status.button_valve_4_manual_action,
                          self.widget_status.button_valve_5_manual_action,
                          self.widget_status.button_valve_6_manual_action,
                          self.widget_status.button_valve_7_manual_action,
                          self.widget_status.button_valve_8_manual_action]

        for i in range(0, len(status_checks)):
            config_file_valves.values[i, 33] = status_checks[i].isChecked()
            manual_buttons[i].setEnabled(status_checks[i].isChecked())

        config_file_valves.to_csv(variables.config_file_valves, index=False)


