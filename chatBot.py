#!/usr/bin/python

#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       The AIML files used in this program can be downloaded for free from
#                   http://aitools.org/Free_AIML_sets


from  PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import aiml

class chatBot(QDialog):
    
    def __init__(self, parent = None):
        super(chatBot, self).__init__(parent)
        self.browser = QTextBrowser()
        self.infield = QLineEdit()
        self.infield.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.infield)
        self.setLayout(layout)
        self.infield.setFocus()
        self.connect(self.infield, SIGNAL("returnPressed()"), self.updateUi)
        self.setWindowTitle("Chat Bot")
        self.resize(400, 500)
        
    def updateUi(self):
        text = unicode(self.infield.text())
        textString = QString("<b>Me</b> >> %s" %text)
        self.browser.append(textString)
        result = brain.respond("%s" %text)
        resultString = QString("<b>Bot</b> >> %s" %result)
        self.browser.append(resultString)
        self.infield.clear()
        
def main():
    app = QApplication(sys.argv)
    bot = chatBot()
    bot.show()
    app.exec_()
    
if __name__ == '__main__':
    brain = aiml.Kernel()
    brain.learn('brain/std-startup.xml')
    brain.respond("load aiml b")
    main()
