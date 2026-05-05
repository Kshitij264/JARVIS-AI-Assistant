import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem
from PyQt5.QtSvg import QGraphicsSvgItem
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
        self.setWindowFlags(
            Qt.FramelessWindowHint
        )

        # Send window to bottom (wallpaper behavior)
        self.setWindowFlag(Qt.WindowStaysOnBottomHint, True)

        # Transparent background
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Load SVG
        

        self.view = QGraphicsView()
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)
        self.view.setAlignment(Qt.AlignCenter)
        self.scene.setBackgroundBrush(Qt.transparent)

        # Remove scrollbars completely
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Remove borders & background
        self.view.setStyleSheet("background: rgba(0,0,0,0); border: none;")
        self.view.setFrameShape(QGraphicsView.NoFrame)

        # Disable dragging
        self.view.setDragMode(QGraphicsView.NoDrag)

        self.svg_item = QGraphicsSvgItem("jarvis_core_master.svg")
        self.svg_item.setScale(1.0)

        self.scene.addItem(self.svg_item)

        # --- CLIPPING MASK (REMOVE RECTANGLE VISUALLY) ---
        rect = self.svg_item.boundingRect()

        mask = QGraphicsEllipseItem(rect)
        from PyQt5.QtGui import QPen
        mask.setPen(QPen(Qt.NoPen))
        mask.setBrush(Qt.transparent)

        self.svg_item.setParentItem(mask)
        mask.setTransformOriginPoint(478, 430)
        self.scene.addItem(mask)

        # Use exact SVG center (from your SVG code)
        self.svg_item.setTransformOriginPoint(478, 430)

        # Move SVG to scene center
        self.svg_item.setPos(0, 0)
        mask.setPos(-rect.width()/2, -rect.height()/2)
        # Glow disabled
        self.svg_item.setGraphicsEffect(None)

        # DO NOT override origin — keep SVG center
        pass

        # Fit SVG inside view
        rect = self.svg_item.boundingRect()

        # Make scene centered around (0,0)
        self.scene.setSceneRect(
            -rect.width()/2,
            -rect.height()/2,
            rect.width(),
            rect.height()
        )
        layout.addWidget(self.view)

        # Resize window
        screen = QApplication.primaryScreen().geometry()
        self.setGeometry(screen)

    # Center screen
        self.start_rotation()   # ALWAYS ROTATE


    def center_on_screen(self):
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)


    def update_state(self, state):

        if hasattr(self, "pulse_timer") and state != JarvisState.LISTENING:
            self.pulse_timer.stop()

        if state == JarvisState.OFF:
            self.setWindowOpacity(0.3)
            pass

        elif state == JarvisState.IDLE:
            self.setWindowOpacity(0.6)
            pass

        elif state == JarvisState.LISTENING:
            self.setWindowOpacity(0.9)
            pass
            self.start_pulse()

        elif state == JarvisState.THINKING:
            self.setWindowOpacity(1.0)
            pass

        elif state == JarvisState.SPEAKING:
            self.setWindowOpacity(1.0)
            pass

        elif state == JarvisState.EXECUTING:
            self.setWindowOpacity(1.0)
            pass


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
        self.svg_item.parentItem().setRotation(self.angle)

    # DEBUG (optional)
    # print("rotating:", self.angle)