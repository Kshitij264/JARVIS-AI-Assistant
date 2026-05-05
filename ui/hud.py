import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGraphicsView, QGraphicsScene
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtCore import Qt
from states.jarvis_states import JarvisState
from PyQt5.QtCore import QPropertyAnimation, QRect, QEasingCurve, QTimer
from PyQt5.QtCore import pyqtSignal

class JarvisHUD(QWidget):

    state_signal = pyqtSignal(object)
    def __init__(self):
        super().__init__()
        self.state_signal.connect(self.update_state)
        self.setWindowTitle("JARVIS HUD")
        self.pulse_anim = None
        self.rotation_anim = None
        # Remove window frame
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )

        # Transparent background
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Load SVG
        from PyQt5.QtSvg import QGraphicsSvgItem

        self.view = QGraphicsView()
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

        # Remove scrollbars completely
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Remove borders & background
        self.view.setStyleSheet("background: transparent; border: none;")

        # Disable dragging
        self.view.setDragMode(QGraphicsView.NoDrag)

        self.svg_item = QGraphicsSvgItem("jarvis_core_master.svg")
        self.svg_item.setScale(0.5)

        self.scene.addItem(self.svg_item)

        # Set transform origin to center (VERY IMPORTANT)
        rect = self.svg_item.boundingRect()
        self.svg_item.setTransformOriginPoint(rect.center())

        # Fit SVG inside view
        self.view.fitInView(self.svg_item, Qt.KeepAspectRatio)
        self.scene.setSceneRect(self.svg_item.boundingRect())
        layout.addWidget(self.view)

        # Resize window
        self.resize(400, 400)

    # Center screen
        self.center_on_screen()
        self.start_rotation()   # ALWAYS ROTATE


    def center_on_screen(self):
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)


    def update_state(self, state):
        # Stop previous animations
        if hasattr(self, "pulse_timer") and state != JarvisState.LISTENING:
            self.pulse_timer.stop()


        if state == JarvisState.OFF:
            self.setWindowOpacity(0.3)

        elif state == JarvisState.IDLE:
            self.setWindowOpacity(0.6)

        elif state == JarvisState.LISTENING:
            self.setWindowOpacity(0.9)
            self.start_pulse()

        elif state == JarvisState.THINKING:
            self.setWindowOpacity(1.0)
            self.start_rotation()

        elif state == JarvisState.SPEAKING:
            self.setWindowOpacity(1.0)

        elif state == JarvisState.EXECUTING:
            self.setWindowOpacity(1.0)


    def start_pulse(self):
        self.scale_value = 0.5
        self.growing = True

        self.pulse_timer = QTimer()
        self.pulse_timer.timeout.connect(self.pulse_step)
        self.pulse_timer.start(30)


    def pulse_step(self):
        if self.growing:
            self.scale_value += 0.005
            if self.scale_value >= 0.6:
                self.growing = False
        else:
            self.scale_value -= 0.005
            if self.scale_value <= 0.5:
                self.growing = True

        self.svg_item.setScale(self.scale_value)


    def start_rotation(self):
        if hasattr(self, "rotation_timer") and self.rotation_timer.isActive():
            return

        print("ROTATION STARTED")

        self.angle = 0
        self.rotation_timer = QTimer()
        self.rotation_timer.timeout.connect(self.rotate_step)
        self.rotation_timer.start(16)


    def rotate_step(self):
        self.angle += 2
        self.svg_item.setRotation(self.angle)

    # DEBUG (optional)
    # print("rotating:", self.angle)