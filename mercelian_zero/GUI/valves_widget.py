from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QComboBox, QCheckBox, QLineEdit


class ValvesWidget(QWidget):
    def __init__(self, p_parent=None):
        super().__init__(parent=p_parent)

        self.label_title = QLabel('<b>Configuración Válvulas</b>')

        self.label_valve_select = QLabel('Válvula:')
        self.combo_valve_select = QComboBox()
        for i in range(1, 9):
            self.combo_valve_select.addItem(str(i))

        self.label_valve_days = QLabel('Diás de riego:')
        self.check_valve_monday = QCheckBox()
        self.check_valve_monday.setText('L')
        self.check_valve_tuesday = QCheckBox()
        self.check_valve_tuesday.setText('M')
        self.check_valve_wednesday = QCheckBox()
        self.check_valve_wednesday.setText('X')
        self.check_valve_thursday = QCheckBox()
        self.check_valve_thursday.setText('J')
        self.check_valve_friday = QCheckBox()
        self.check_valve_friday.setText('V')
        self.check_valve_saturday = QCheckBox()
        self.check_valve_saturday.setText('S')
        self.check_valve_sunday = QCheckBox()
        self.check_valve_sunday.setText('D')

        # self.label_daily_activations = QLabel('Cant. de riegos diarios:')
        # self.line_daily_activations = QLineEdit()
        # self.line_daily_activations.setText('0')
        # self.line_daily_activations.setInputMask('0')

        self.label_activation_select = QLabel('Riego:')
        self.combo_activation_select = QComboBox()
        for i in range(1, 13):
            self.combo_activation_select.addItem(str(i))
        self.check_enable_activation = QCheckBox()
        self.check_enable_activation.setText('Habilitar')
        self.check_enable_activation.setChecked(False)

        self.label_activation_time = QLabel('Hora de inicio:')
        self.combo_activation_time_hour = QComboBox()
        for i in range(0, 25):
            self.combo_activation_time_hour.addItem(str(i))
        self.combo_activation_time_hour.setEnabled(False)
        self.combo_activation_time_minute = QComboBox()
        for i in range(0, 12):
            self.combo_activation_time_minute.addItem(str(i * 5))
        self.combo_activation_time_minute.setEnabled(False)

        self.label_deactivation_time = QLabel('Hora de fin:')
        self.combo_deactivation_time_hour = QComboBox()
        for i in range(0, 25):
            self.combo_deactivation_time_hour.addItem(str(i))
        self.combo_deactivation_time_hour.setEnabled(False)
        self.combo_deactivation_time_minute = QComboBox()
        for i in range(0, 12):
            self.combo_deactivation_time_minute.addItem(str(i * 5))
        self.combo_deactivation_time_minute.setEnabled(False)

        self.check_pump_valve_relation = QCheckBox()
        self.check_pump_valve_relation.setText('Encender bomba con válvula')
        # self.button_save_config = QPushButton('Guardar Configuración')

        valve_select_layout = QHBoxLayout()
        valve_select_layout.addWidget(self.label_valve_select)
        valve_select_layout.addWidget(self.combo_valve_select)

        valve_days_layout = QHBoxLayout()
        valve_days_layout.addWidget(self.label_valve_days)
        valve_days_layout.addWidget(self.check_valve_monday)
        valve_days_layout.addWidget(self.check_valve_tuesday)
        valve_days_layout.addWidget(self.check_valve_wednesday)
        valve_days_layout.addWidget(self.check_valve_thursday)
        valve_days_layout.addWidget(self.check_valve_friday)
        valve_days_layout.addWidget(self.check_valve_saturday)
        valve_days_layout.addWidget(self.check_valve_sunday)

        # daily_activations_layout = QHBoxLayout()
        # daily_activations_layout.addWidget(self.label_daily_activations)
        # daily_activations_layout.addWidget(self.line_daily_activations)

        activation_select_layout = QHBoxLayout()
        activation_select_layout.addWidget(self.label_activation_select)
        activation_select_layout.addWidget(self.combo_activation_select)
        activation_select_layout.addWidget(self.check_enable_activation)

        activation_time_layout = QHBoxLayout()
        activation_time_layout.addWidget(self.label_activation_time, stretch=2)
        activation_time_layout.addWidget(self.combo_activation_time_hour, stretch=2)
        activation_time_layout.addWidget(QLabel('h'))
        activation_time_layout.addWidget(self.combo_activation_time_minute, stretch=2)
        activation_time_layout.addWidget(QLabel('m'))

        deactivation_time_layout = QHBoxLayout()
        deactivation_time_layout.addWidget(self.label_deactivation_time, stretch=2)
        deactivation_time_layout.addWidget(self.combo_deactivation_time_hour, stretch=2)
        deactivation_time_layout.addWidget(QLabel('h'))
        deactivation_time_layout.addWidget(self.combo_deactivation_time_minute, stretch=2)
        deactivation_time_layout.addWidget(QLabel('m'))

        pump_valve_relation_layout = QHBoxLayout()
        pump_valve_relation_layout.addWidget(self.check_pump_valve_relation)
        # pump_valve_relation_layout.addWidget(self.button_save_config)

        valves_widget_layout = QVBoxLayout()
        valves_widget_layout.addWidget(self.label_title)
        valves_widget_layout.addLayout(valve_select_layout)
        valves_widget_layout.addLayout(valve_days_layout)
        # valves_widget_layout.addLayout(daily_activations_layout)
        valves_widget_layout.addLayout(activation_select_layout)
        valves_widget_layout.addLayout(activation_time_layout)
        valves_widget_layout.addLayout(deactivation_time_layout)
        valves_widget_layout.addLayout(pump_valve_relation_layout)
        self.setLayout(valves_widget_layout)
