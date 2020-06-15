"""数据
薛蟠     4560 25
薛蝌     4460 25
薛宝钗   35776 23
薛宝琴   14346 18
王夫人   43360 45
王熙凤   24460 25
王子腾   55660 45
王仁     15034 65
尤二姐   5324 24
贾芹     5663 25
贾兰     13443 35
贾芸     4522 25
尤三姐   5905 22
贾珍     54603 35
"""
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox
import re


class WageStat(object):
    def __init__(self):
        self.window = QMainWindow()
        self.window.resize(600, 500)
        self.window.setWindowTitle('薪酬统筹')
        self.textEdit = QPlainTextEdit(self.window)
        self.textEdit.setPlaceholderText('请输入薪资表')
        self.textEdit.resize(400, 400)
        self.textEdit.move(100, 25)
        self.button = QPushButton('统计', self.window)
        self.button.move(250, 450)
        self.button.clicked.connect(self.__handler_click)

    def __handler_click(self):
        info = self.textEdit.toPlainText()
        info = info.split('\n')
        name = ''
        for data in info:
            num = re.search(r'\d{4,}', data)
            if num:
                if int(num.group()) <= 20000:
                    name += data[0:4] + '\n'
            else:
                print('匹配失败')
        QMessageBox.about(self.window, '统计结果', f'薪资低于2万人员名单\n{name}')


if __name__ == '__main__':
    wage = QApplication()
    stat = WageStat()
    stat.window.show()
    wage.exec_()
