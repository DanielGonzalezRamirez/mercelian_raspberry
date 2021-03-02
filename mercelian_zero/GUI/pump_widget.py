from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QComboBox, QCheckBox, QLineEdit


class PumpWidget(QWidget):
    def __init__(self, p_parent=None):
        super().__init__(parent=p_parent)

        self.label_title = QLabel('<b>Configuración Bomba</b>')
        self.label_subtitle = QLabel('A continuación se programa un comportamiento de la bomba '
                                     'independiente de las válvulas')
        self.label_subtitle.setWordWrap(True)

        self.label_pump_days = QLabel('Diás de riego:')
        self.check_pump_monday = QCheckBox()
        self.check_pump_monday.setText('L')
        self.check_pump_tuesday = QCheckBox()
        self.check_pump_tuesday.setText('M')
        self.check_pump_wednesday = QCheckBox()
        self.check_pump_wednesday.setText('X')
        self.check_pump_thursday = QCheckBox()
        self.check_pump_thursday.setText('J')
        self.check_pump_friday = QCheckBox()
        self.check_pump_friday.setText('V')
        self.check_pump_saturday = QCheckBox()
        self.check_pump_saturday.setText('S')
        self.check_pump_sunday = QCheckBox()
        self.check_pump_sunday.setText('D')

        # self.label_daily_activations = QLabel('Cant. de riegos diarios:')
        # self.line_daily_activations = QLineEdit()
        # self.line_daily_activations.setText('1')
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
        self.combo_deactivation_time_minute.setEnabled(True)

        # self.button_save_config = QPushButton('Guardar Configuración')

        pump_days_layout = QHBoxLayout()
        pump_days_layout.addWidget(self.label_pump_days)
        pump_days_layout.addWidget(self.check_pump_monday)
        pump_days_layout.addWidget(self.check_pump_tuesday)
        pump_days_layout.addWidget(self.check_pump_wednesday)
        pump_days_layout.addWidget(self.check_pump_thursday)
        pump_days_layout.addWidget(self.check_pump_friday)
        pump_days_layout.addWidget(self.check_pump_saturday)
        pump_days_layout.addWidget(self.check_pump_sunday)

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

        # save_config_layout = QHBoxLayout()
        # save_config_layout.addWidget(self.button_save_config)

        pump_widget_layout = QVBoxLayout()
        pump_widget_layout.addWidget(self.label_title)
        pump_widget_layout.addWidget(self.label_subtitle)
        pump_widget_layout.addLayout(pump_days_layout)
        # pump_widget_layout.addLayout(daily_activations_layout)
        pump_widget_layout.addLayout(activation_select_layout)
        pump_widget_layout.addLayout(activation_time_layout)
        pump_widget_layout.addLayout(deactivation_time_layout)
        # pump_widget_layout.addLayout(save_config_layout)
        self.setLayout(pump_widget_layout)
