from PySide6 import QtCore, QtWidgets,QtGui
import random
import sys
import requests
import os

class FloatWindow(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        # 用于保存主窗口
        self.parent = parent
        # 组件创建及设置
        self.label = QtWidgets.QLabel("双击\n展开", self, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setFont(QtGui.QFont("微软雅黑",15))
        # 窗口布局
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.label)
        # 设置窗口属性
        # 窗口透明度
        self.setWindowOpacity(0.8)
        # 窗口标志(始终欸与顶层,无边框,工具层)
        self.setWindowFlags(QtCore.Qt.WindowType.WindowStaysOnTopHint | QtCore.Qt.WindowType.FramelessWindowHint | QtCore.Qt.WindowType.Tool)
    def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent):
        """覆盖默认双击行为,双击时隐藏自己,显示主窗口."""
        self.parent.setVisible(True)
        self.setVisible(False)
    def mouseMoveEvent(self, e: QtGui.QMouseEvent):
        """重写鼠标移动事件"""
        if self._tracking:
            self._endPos = e.position().toPoint() - self._startPos
            self.move(self.pos() + self._endPos)
            self.parent.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QtGui.QMouseEvent):
        """跟踪鼠标按住窗口,便于重写窗口拖动逻辑"""
        if e.button() == QtCore.Qt.MouseButton.LeftButton:
            self._startPos = QtCore.QPoint(e.position().x(), e.position().y())
            self._tracking = True

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent):
        """鼠标松开事件"""
        if e.button() == QtCore.Qt.MouseButton.LeftButton:
            self._tracking = False
            self._startPos = None
            self._endPos = None

class Window(QtWidgets.QWidget):
    start = 1
    end = 50
    def __init__(self):
        super().__init__()
        self.child = FloatWindow(self)
        self.child.setVisible(False)

        self.button = QtWidgets.QPushButton("生成", self)
        self.con_button = QtWidgets.QPushButton("设置", self)
        self.text = QtWidgets.QLabel("⬇点击按钮生成", self, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.zoom_out_button = QtWidgets.QPushButton("缩小", self)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.con_button)
        self.layout.addWidget(self.zoom_out_button)
        self.button.clicked.connect(self.gen_num)
        self.con_button.clicked.connect(self.get_scope)
        self.zoom_out_button.clicked.connect(self.zoom_out)

        self.setWindowOpacity(0.8)
        self.setWindowFlags(QtCore.Qt.WindowType.WindowStaysOnTopHint | QtCore.Qt.WindowType.FramelessWindowHint | QtCore.Qt.WindowType.Tool)

    @QtCore.Slot()
    def gen_num(self):
        self.text.setText(str(random.randint(self.start,self.end)))

    @QtCore.Slot()
    def get_scope(self):
        while True:
            start, ok = QtWidgets.QInputDialog.getInt(self, "配置", "请输入起始数字: ", self.start)
            if ok:
                self.start = start
                break
        while True:
            end,ok = QtWidgets.QInputDialog.getInt(self, "配置", "请输入结束数字: ", self.end)
            if ok:
                self.end = end
                break
    @QtCore.Slot()
    def zoom_out(self):
        self.setVisible(False)
        self.child.setVisible(True)

    def mouseMoveEvent(self, e: QtGui.QMouseEvent):
    	if self._tracking:
            self._endPos = e.position().toPoint() - self._startPos
            self.move(self.pos() + self._endPos)
            self.child.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QtGui.QMouseEvent):
    	if e.button() == QtCore.Qt.MouseButton.LeftButton:
            self._startPos = QtCore.QPoint(e.position().x(), e.position().y())
            self._tracking = True

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent):
        if e.button() == QtCore.Qt.MouseButton.LeftButton:
            self._tracking = False
            self._startPos = None
            self._endPos = None

major = 1
minor = 0
revision = 1

def check_update() -> bool:
    re_ver = requests.get("***").text
    re_major, re_minor, re_revision = re_ver.split('.')
    if int(re_revision) > revision or int(re_minor) > minor or int(re_major) > major:
        os.execl("./update.exe","update.exe","")

if __name__ == "__main__":
    check_update()

    app = QtWidgets.QApplication([])

    widget = Window()
    widget.show()
    widget.resize(90,70)

    sys.exit(app.exec())