#######################################################################
##################       Basics of PyQt5        #######################
#################                                ######################
#######################################################################


##### IMPORTED ESSENTIAL LIBRARIES ######

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLineEdit, QMessageBox
import sys


######### GENERATING A CLASS FOR RUNNING THE GUI SCRIPT FROM ANY OTHER SOURCE #########
class window1(QMainWindow):

    ####### CLASS CONSTRUCTOR ALONGWITH Main Window constructor ########

    def __init__(self):
        super(window1,self).__init__()
        self.setGeometry(500,200,500,300)        # self -> QMainWindow  ,   
        self.setWindowTitle("First Window")      # Title of the main window
        self.UI()
        

    ####### Contents to be present inside the main window #######

    ## Adding a label in the main window is done as ##

    def UI(self):
        self.label1 = QtWidgets.QLabel(self)            # set label on main screen
        self.label2 = QtWidgets.QLabel(self)
        self.label3 = QtWidgets.QLabel(self)            
        self.label4 = QtWidgets.QLabel(self)
        self.label5 = QtWidgets.QLabel(self)

        self.label1.setText("First content")            # set text of label to be printed on main e=screen
        self.label1.move(7,30)                          # set location of label to be placed on main screen as move(x_pos,y_pos)
        self.label2.setText("Second content")            
        self.label2.move(7,60)
        self.label3.setText("Third content")            
        self.label3.move(7,90)
        self.label4.setText("Fourth content")            
        self.label4.move(7,120)
       # self.label5.setText('Refresh the content')
       # self.label5.move(100,240)


    ## Adding push button in the main window is done as ##

        self.push_but1 = QtWidgets.QPushButton(self)          # set push button to be added on mian window
        self.push_but1.setText('Click Button1')               # set text to be printed on push button
        self.push_but1.move(100,30)                           # set location of the push button on main window

        self.push_but1.clicked.connect(self.event1)             # Click operation to be done on push button. It is
                                                                # just representing the operation to be done after  
                                                                # clicking the push button

        self.push_but2 = QtWidgets.QPushButton(self)
        self.push_but2.setText('Click Button2')
        self.push_but2.move(100,60)
        self.push_but2.clicked.connect(self.event2)

        self.push_but3 = QtWidgets.QPushButton(self)
        self.push_but3.setText('Click Button3')
        self.push_but3.move(100,90)
        self.push_but3.clicked.connect(self.event3)

        self.push_but4 = QtWidgets.QPushButton(self)
        self.push_but4.setText('Click Button4')
        self.push_but4.move(100,120)
        self.push_but4.clicked.connect(self.event4)

        self.push_but5 = QtWidgets.QPushButton(self)
        self.push_but5.setText('Refresh')
        self.push_but5.move(200,240)
        self.push_but5.clicked.connect(self.event5)


        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setText('Print text button')
        self.button1.move(200,200)
        self.button1.clicked.connect(self.button1_event)


        ### Added textbox ###
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(200,90)
        self.textbox1.resize(100,35)


    ### Added events for click operations ###

    def event1(self):                                 # Specific function of event to be done after 
        self.label1.setText("You clicked 1")          # clicking the push button

    def event2(self):
        self.label2.setText("You clicked 2")
    
    def event3(self):
        self.label3.setText("You clicked 3")

    def event4(self):
        self.label4.setText("You clicked 4")

    def event5(self):
        self.label1.setText("First Content")
        self.label2.setText("Second Content")
        self.label3.setText("Third Content")
        self.label4.setText("Fourth Content")

    def button1_event(self):                   ## Event associated with button1 (printing the content of textbox) 
        print('Button1 clicked!!')

    

        
        
#def display():
#    app = QApplication(sys.argv)
#    win = window1()                         
#    win.show()                                  
#    sys.exit(app.exec_())                       

#display()

if(__name__=='__main__'):
    app = QApplication(sys.argv)
    win = window1()                         
    win.show()                                  
    sys.exit(app.exec_())                       
