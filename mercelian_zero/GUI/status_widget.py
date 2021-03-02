from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QCheckBox


class StatusWidget(QWidget):
    def __init__(self, p_parent=None):
        super().__init__(parent=p_parent)

        self.label_title = QLabel('<b>Estado del Sistema</b>')

        self.label_valve_1 = QLabel('Válvula 1:')
        self.label_valve_1_status = QLabel('Off')
        self.check_valve_1_man_auto = QCheckBox()
        self.check_valve_1_man_auto.setText('Auto')
        self.check_valve_1_man_auto.setChecked(True)
        # self.label_valve_1_next_change = QLabel('00:00')
        self.button_valve_1_manual_action = QPushButton('On')
        self.button_valve_1_manual_action.setEnabled(False)
        self.button_valve_1_manual_action.clicked.connect(self.manual_action_valve_1)

        self.label_valve_2 = QLabel('Válvula 2:')
        self.label_valve_2_status = QLabel('Off')
        self.check_valve_2_man_auto = QCheckBox()
        self.check_valve_2_man_auto.setText('Auto')
        self.check_valve_2_man_auto.setChecked(True)
        # self.label_valve_2_next_change = QLabel('00:00')
        self.button_valve_2_manual_action = QPushButton('On')
        self.button_valve_2_manual_action.setEnabled(False)
        self.button_valve_2_manual_action.clicked.connect(self.manual_action_valve_2)

        self.label_valve_3 = QLabel('Válvula 3:')
        self.label_valve_3_status = QLabel('Off')
        self.check_valve_3_man_auto = QCheckBox()
        self.check_valve_3_man_auto.setText('Auto')
        self.check_valve_3_man_auto.setChecked(True)
        # self.label_valve_3_next_change = QLabel('00:00')
        self.button_valve_3_manual_action = QPushButton('On')
        self.button_valve_3_manual_action.setEnabled(False)
        self.button_valve_3_manual_action.clicked.connect(self.manual_action_valve_3)

        self.label_valve_4 = QLabel('Válvula 4:')
        self.label_valve_4_status = QLabel('Off')
        self.check_valve_4_man_auto = QCheckBox()
        self.check_valve_4_man_auto.setText('Auto')
        self.check_valve_4_man_auto.setChecked(True)
        # self.label_valve_4_next_change = QLabel('00:00')
        self.button_valve_4_manual_action = QPushButton('On')
        self.button_valve_4_manual_action.setEnabled(False)
        self.button_valve_4_manual_action.clicked.connect(self.manual_action_valve_4)

        self.label_valve_5 = QLabel('Válvula 5:')
        self.label_valve_5_status = QLabel('Off')
        self.check_valve_5_man_auto = QCheckBox()
        self.check_valve_5_man_auto.setText('Auto')
        self.check_valve_5_man_auto.setChecked(True)
        # self.label_valve_5_next_change = QLabel('00:00')
        self.button_valve_5_manual_action = QPushButton('On')
        self.button_valve_5_manual_action.setEnabled(False)
        self.button_valve_5_manual_action.clicked.connect(self.manual_action_valve_5)

        self.label_valve_6 = QLabel('Válvula 6:')
        self.label_valve_6_status = QLabel('Off')
        self.check_valve_6_man_auto = QCheckBox()
        self.check_valve_6_man_auto.setText('Auto')
        self.check_valve_6_man_auto.setChecked(True)
        # self.label_valve_6_next_change = QLabel('00:00')
        self.button_valve_6_manual_action = QPushButton('On')
        self.button_valve_6_manual_action.setEnabled(False)
        self.button_valve_6_manual_action.clicked.connect(self.manual_action_valve_6)

        self.label_valve_7 = QLabel('Válvula 7:')
        self.label_valve_7_status = QLabel('Off')
        self.check_valve_7_man_auto = QCheckBox()
        self.check_valve_7_man_auto.setText('Auto')
        self.check_valve_7_man_auto.setChecked(True)
        # self.label_valve_7_next_change = QLabel('00:00')
        self.button_valve_7_manual_action = QPushButton('On')
        self.button_valve_7_manual_action.setEnabled(False)
        self.button_valve_7_manual_action.clicked.connect(self.manual_action_valve_7)

        self.label_valve_8 = QLabel('Válvula 8:')
        self.label_valve_8_status = QLabel('Off')
        self.check_valve_8_man_auto = QCheckBox()
        self.check_valve_8_man_auto.setText('Auto')
        self.check_valve_8_man_auto.setChecked(True)
        # self.label_valve_8_next_change = QLabel('00:00')
        self.button_valve_8_manual_action = QPushButton('On')
        self.button_valve_8_manual_action.setEnabled(False)
        self.button_valve_8_manual_action.clicked.connect(self.manual_action_valve_8)

        self.label_pump = QLabel('Bomba:')
        self.label_pump_status = QLabel('Off')
        self.check_pump_man_auto = QCheckBox()
        self.check_pump_man_auto.setText('Auto')
        self.check_pump_man_auto.setChecked(True)
        # self.label_pump_next_change = QLabel('00:00')
        self.button_pump_manual_action = QPushButton('On')
        self.button_pump_manual_action.setEnabled(False)
        self.button_pump_manual_action.clicked.connect(self.manual_action_pump)

        self.label_header = QLabel('Elemento')
        self.label_header_status = QLabel('On/Off')
        self.label_header_man_auto = QLabel('Auto/Man.')
        # self.label_header_next_change = QLabel('Próx. cambio')
        self.label_header_manual_action = QLabel('Manual')

        valve_1_layout = QHBoxLayout()
        valve_1_layout.addWidget(self.label_valve_1, stretch=4)
        valve_1_layout.addWidget(self.label_valve_1_status, stretch=3)
        valve_1_layout.addWidget(self.check_valve_1_man_auto, stretch=3)
        # valve_1_layout.addWidget(self.label_valve_1_next_change, stretch=3)
        valve_1_layout.addWidget(self.button_valve_1_manual_action, stretch=3)

        valve_2_layout = QHBoxLayout()
        valve_2_layout.addWidget(self.label_valve_2, stretch=4)
        valve_2_layout.addWidget(self.label_valve_2_status, stretch=3)
        valve_2_layout.addWidget(self.check_valve_2_man_auto, stretch=3)
        # valve_2_layout.addWidget(self.label_valve_2_next_change, stretch=3)
        valve_2_layout.addWidget(self.button_valve_2_manual_action, stretch=3)

        valve_3_layout = QHBoxLayout()
        valve_3_layout.addWidget(self.label_valve_3, stretch=4)
        valve_3_layout.addWidget(self.label_valve_3_status, stretch=3)
        valve_3_layout.addWidget(self.check_valve_3_man_auto, stretch=3)
        # valve_3_layout.addWidget(self.label_valve_3_next_change, stretch=3)
        valve_3_layout.addWidget(self.button_valve_3_manual_action, stretch=3)

        valve_4_layout = QHBoxLayout()
        valve_4_layout.addWidget(self.label_valve_4, stretch=4)
        valve_4_layout.addWidget(self.label_valve_4_status, stretch=3)
        valve_4_layout.addWidget(self.check_valve_4_man_auto, stretch=3)
        # valve_4_layout.addWidget(self.label_valve_4_next_change, stretch=3)
        valve_4_layout.addWidget(self.button_valve_4_manual_action, stretch=3)

        valve_5_layout = QHBoxLayout()
        valve_5_layout.addWidget(self.label_valve_5, stretch=4)
        valve_5_layout.addWidget(self.label_valve_5_status, stretch=3)
        valve_5_layout.addWidget(self.check_valve_5_man_auto, stretch=3)
        # valve_5_layout.addWidget(self.label_valve_5_next_change, stretch=3)
        valve_5_layout.addWidget(self.button_valve_5_manual_action, stretch=3)

        valve_6_layout = QHBoxLayout()
        valve_6_layout.addWidget(self.label_valve_6, stretch=4)
        valve_6_layout.addWidget(self.label_valve_6_status, stretch=3)
        valve_6_layout.addWidget(self.check_valve_6_man_auto, stretch=3)
        # valve_6_layout.addWidget(self.label_valve_6_next_change, stretch=3)
        valve_6_layout.addWidget(self.button_valve_6_manual_action, stretch=3)

        valve_7_layout = QHBoxLayout()
        valve_7_layout.addWidget(self.label_valve_7, stretch=4)
        valve_7_layout.addWidget(self.label_valve_7_status, stretch=3)
        valve_7_layout.addWidget(self.check_valve_7_man_auto, stretch=3)
        # valve_7_layout.addWidget(self.label_valve_7_next_change, stretch=3)
        valve_7_layout.addWidget(self.button_valve_7_manual_action, stretch=3)

        valve_8_layout = QHBoxLayout()
        valve_8_layout.addWidget(self.label_valve_8, stretch=4)
        valve_8_layout.addWidget(self.label_valve_8_status, stretch=3)
        valve_8_layout.addWidget(self.check_valve_8_man_auto, stretch=3)
        # valve_8_layout.addWidget(self.label_valve_8_next_change, stretch=3)
        valve_8_layout.addWidget(self.button_valve_8_manual_action, stretch=3)

        pump_layout = QHBoxLayout()
        pump_layout.addWidget(self.label_pump, stretch=4)
        pump_layout.addWidget(self.label_pump_status, stretch=3)
        pump_layout.addWidget(self.check_pump_man_auto, stretch=3)
        # pump_layout.addWidget(self.label_pump_next_change, stretch=3)
        pump_layout.addWidget(self.button_pump_manual_action, stretch=3)

        # header_layout = QHBoxLayout()
        # header_layout.addWidget(self.label_header, stretch=3)
        # header_layout.addWidget(self.label_header_status, stretch=3)
        # header_layout.addWidget(self.label_header_man_auto, stretch=3)
        # header_layout.addWidget(self.label_header_next_change, stretch=3)
        # header_layout.addWidget(self.label_header_manual_action, stretch=3)

        status_widget_layout = QVBoxLayout()
        status_widget_layout.addWidget(self.label_title)
        # status_widget_layout.addLayout(header_layout)
        status_widget_layout.addLayout(valve_1_layout)
        status_widget_layout.addLayout(valve_2_layout)
        status_widget_layout.addLayout(valve_3_layout)
        status_widget_layout.addLayout(valve_4_layout)
        status_widget_layout.addLayout(valve_5_layout)
        status_widget_layout.addLayout(valve_6_layout)
        status_widget_layout.addLayout(valve_7_layout)
        status_widget_layout.addLayout(valve_8_layout)
        status_widget_layout.addLayout(pump_layout)
        status_widget_layout.addWidget(QLabel('MERCELIAN - Control de Riego'))
        status_widget_layout.addWidget(QLabel('Versión 0.1'))
        status_widget_layout.addWidget(QLabel('Noviembre 2020'))
        status_widget_layout.addWidget(QLabel('Daniel Julián González Ramírez'))
        status_widget_layout.addWidget(QLabel('danielj.gonzalezr@gmail.com'))
        self.setLayout(status_widget_layout)

    def update_status(self):
        pass

    def manual_action_valve_1(self):
        print('Pump')

    def manual_action_valve_2(self):
        print('Pump')

    def manual_action_valve_3(self):
        print('Pump')

    def manual_action_valve_4(self):
        print('Pump')

    def manual_action_valve_5(self):
        print('Pump')

    def manual_action_valve_6(self):
        print('Pump')

    def manual_action_valve_7(self):
        print('Pump')

    def manual_action_valve_8(self):
        print('Pump')

    def manual_action_pump(self):
        print('Pump')


