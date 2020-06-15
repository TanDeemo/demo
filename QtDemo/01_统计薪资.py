import sys
import re
from PySide2.QtWidgets import (QApplication,
                               QMainWindow,
                               QPushButton,
                               QPlainTextEdit,
                               QMessageBox)


def handler_click():
    name_list = ''
    info = textEdit.toPlainText()
    info = info.split('\n')
    for data in info:
        wage = re.search(r"\d{4,}", data)
        if wage:
            if int(wage.group()) <= 20000:
                name_list += data[0:4] + '\n'
        else:
            print('格式有误')
    QMessageBox.about(window, '统计结果',
                      '薪资20000以下的有\n'
                      f'{name_list}')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.resize(600, 500)
    window.setWindowTitle('薪资统筹')

    # 输入面板
    textEdit = QPlainTextEdit(window)
    textEdit.setPlaceholderText('请输入薪资表')
    textEdit.move(100, 50)
    textEdit.resize(400, 300)

    # 按钮
    button = QPushButton('统计', window)
    button.move(250, 400)
    button.clicked.connect(handler_click)

    # 显示和退出
    window.show()
    sys.exit(app.exec_())