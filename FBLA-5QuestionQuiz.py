import sys                          #Here I am importing all of the files from the computer and the modules that I need.
from PyQt5.QtWidgets import *       #This part of PyQt5 allows me to use widgets for the GUI
from PyQt5.QtGui import *           #This part of PyQt5 allows me to set up the GUI
from PyQt5.QtCore import *          #This part of PyQt5 allows me to use other miscellaneous functions in PyQt5
from fpdf import FPDF               #The FPDF module allows me to easily generate PDFs to print
import random                       #This enables me to use the random.randint() function for randomizing questions
import time                         #This enables me to set the random seed to the time to generate different random numbers

class App(QMainWindow):             #This class encompasses the majority of the program and involves all of the GUI and backend functions

    def __init__(self):             #This function initializes the window with the set size, name and initUI parameters
        super().__init__()
        self.title = 'FBLA QUIZ!'
        self.left = 500
        self.top = 100
        self.width = 600
        self.height = 480
        self.initUI()
        
    def initUI(self):               #This function initializes all of the widgets and most variables that are used in the program, and displays the Main Screen.
        self.setWindowTitle(self.title)               #Sets the window's title to self.title
        self.setFixedSize(self.width, self.height)    #Makes sure the user cannot change the size of the window; there would be white space, and it would look ugly
        self.move(self.left, self.top)                #Moves the Window to an appropriate spot on the screen
        
        self.setAutoFillBackground(True)              #These functions set the palette and the background color of the window to white
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)
        
        
        self.initMainScreen()       #This function initializes all of the widgets and variables of the Main Screen
        
        self.show()                 #This function shows all of the widgets on only the main screen
        
        self.initQuestion()         #This function initializes all of the widgets and variables of the Question Screen
        
        self.initGradeScreen()      #This function initializes all of the widgets and variables of the Grading Screen
        
    
    
    def initMainScreen(self):       #Main Screen initialization
    
        
        self.screen = 0             #This variable represents which screen the window is on. 
                                    #0 represents the Main Screen, 1 is Question #1, 2 is Question #2 . . . 6 is the Grade Screen
        
        #Borders                    #These are the different rectangles that are the borders on all the screens
        
        self.topBarRed = QLabel(" ", self)                           #The QLabel type is used without text to make a colored box
        self.topBarRed.setGeometry(30, 30, 540, 80)                  #The Dimensions are 540x80, and it is 30x30 away from the top left corner
        self.topBarRed.setStyleSheet("background-color: #be2f37")    #Sets the color to red - the same shade as on the FBLA logo
        
        self.bottomBarRed = QLabel(" ", self)                        #Red Box on the botton of the screen
        self.bottomBarRed.setGeometry(30, 430, 540, 20)
        self.bottomBarRed.setStyleSheet("background-color: #be2f37")
        
        self.leftBarRed = QLabel(" ", self)                          #Red Box on the left of the screen
        self.leftBarRed.setGeometry(30, 30, 20, 420)
        self.leftBarRed.setStyleSheet("background-color: #be2f37")
        
        self.rightBarRed = QLabel(" ", self)                         #Red Box on the right of the screen
        self.rightBarRed.setGeometry(550, 30, 20, 420)
        self.rightBarRed.setStyleSheet("background-color: #be2f37")
        
        
        self.topBarBlue = QLabel(" ", self)                          #Blue Box on the top of the screen
        self.topBarBlue.setGeometry(0, 0, 600, 20)
        self.topBarBlue.setStyleSheet("background-color: #00529b")   #Sets the color to blue - the same shade as on the FBLA logo 
        
        self.bottomBarBlue = QLabel(" ", self)                       #Blue Box on the bottom of the screen
        self.bottomBarBlue.setGeometry(0, 460, 600, 20)
        self.bottomBarBlue.setStyleSheet("background-color: #00529b")
        
        self.leftBarBlue = QLabel(" ", self)                         #Blue Box on the left of the screen
        self.leftBarBlue.setGeometry(0, 0, 20, 480)
        self.leftBarBlue.setStyleSheet("background-color: #00529b")
        
        self.rightBarBlue = QLabel(" ", self)                        #Blue Box on the right of the screen
        self.rightBarBlue.setGeometry(580, 0, 20, 480)
        self.rightBarBlue.setStyleSheet("background-color: #00529b")
        
        #Create Image
        self.img = QLabel(self)                                      #The QLabel type is used to create the box that the image will be in
        pixmap = QPixmap("FBLA1.jpg")                                #pixmap is set to the QPixmap type to use the image
        self.img.setPixmap(pixmap)                                   #Here, the image on the pixmap is set to the label
        self.img.move(120,115)                                       #The image is moved to the correct spot
        self.img.resize(pixmap.width(),pixmap.height())              #The label is resized to match the correct size of the image
        
        #Button
        self.button = QPushButton("Start Quiz!", self)                                          #This function creates the first button widget that says "Start Quiz!" in it
        self.button.setGeometry(60, 260, 480, 75)                                               #Sets the size of the button as 480x75 and the coordinates from the top left corner as 60x260
        self.button.setFont(QFont("Impact", 30))                                                #Sets the font to Impace at size 30
        self.button.setStyleSheet('QPushButton {background-color: #be2f37; color: white;}')     #Sets the background color as red (in the FBLA logo) and the text color as white
        self.button.clicked.connect(lambda: self.startQuiz())                                   #This connects the button to the startQuiz() function that will execute when it is clicked
    
        #Quit Button
        self.quitButton = QPushButton("Quit Application", self)                                 #Sets name to "Quit Application"
        self.quitButton.setGeometry(60, 345, 480, 75)                                           #Sets size and position
        self.quitButton.setFont(QFont("Impact", 30))                                            #Sets font and font size
        self.quitButton.setStyleSheet('QPushButton {background-color: #00529b; color: white;}') #Sets text color and background color
        self.quitButton.clicked.connect(lambda: self.quitQuiz())                                #Links button to quitQuiz() function
    
        #Labels
        self.label = QLabel("FBLA 5-Question Quiz", self)         #Creates title "FBLA 5-Question Quiz"
        self.label.setGeometry(30, 30, 540, 80)                   #Sets size and position
        self.label.setFont(QFont("Impact", 40))                   #Sets font and font size
        self.label.setStyleSheet("color: white")                  #Sets text color to white
        self.label.setAlignment(Qt.AlignCenter)                   #Alligns the Text in the center of the label
        
        self.label2 = QLabel("Created By Simon Hjatason", self)   #Creates footnote "FBLA 5-Question Quiz"
        self.label2.setGeometry(10, 460, 200, 20)                 #Sets size and position
        self.label2.setStyleSheet("color: white")                 #Sets text color to white
        
    
    
        
        
    def mainScreen(self):              #This Function is called whenever the program needs to direct itself to the Main Screen
    
        self.hideAnswerWidgets()       #This calls the hideAnswerWidgets() function, which hides the functions on the question pages
        
        self.greenSmiley.hide()        #These functions all hide the widgets on the answer page
        self.redSmiley.hide()
        self.compliment.hide()
        self.gradeTitle.hide()
        self.q1Grade.hide()
        self.q2Grade.hide()
        self.q3Grade.hide()
        self.q4Grade.hide()
        self.q5Grade.hide()
        self.printButton.hide()
        
        self.img.show()             #These functions show the correct widgets for the Main Screen
        self.button.show()
        self.quitButton.show()
        self.label.show()
        self.label2.show()
        
    def initGradeScreen(self):                                       #This function initializes all of the functions and variables on the grade screen
    
        #Create Score Variable
        self.score = 0                                               #The score variable is how many questions are correct once they have been graded
        self.correct = [" ", " ", " ", " ", " "]                     #The correct array shows if each question is correct or incorrect
        
        #Create Green Smiley Face
        self.greenSmiley = QLabel(self)                              #initializes the image of the green smiley face for getting 3 or more questions correct
        pixmap1 = QPixmap("smileygreen.png")                         #Sets the pixmap
        pixmap1 = pixmap1.scaled(100,100)                            #Scales the pixmap
        self.greenSmiley.setPixmap(pixmap1)                          #Sets the pixmap on the label
        self.greenSmiley.move(450,30)                                #Moves it to the right coordinates
        self.greenSmiley.resize(pixmap1.width(),pixmap1.height())    #Sets the size to the correct width and height
        
        #Create Red Smiley Face
        self.redSmiley = QLabel(self)                                #initializes the image of the red smiley face for getting 2 or less questions correct
        pixmap2 = QPixmap("smileyred.png")                           #Sets the pixmap
        pixmap2 = pixmap2.scaled(100,100)                            #Scales the pixmap
        self.redSmiley.setPixmap(pixmap2)                            #Sets the pixmap on the label
        self.redSmiley.move(450,30)                                  #Moves it to the right coordinates
        self.redSmiley.resize(pixmap2.width(),pixmap2.height())      #Sets the size to the correct width and height
        
        #Labels
        self.gradeTitle = QLabel("Score", self)                      #Creates the QLabel for the score
        self.gradeTitle.setGeometry(30, 30, 540, 80)                 #Sets all of the corret parameters for the title
        self.gradeTitle.setFont(QFont("Impact", 40))
        self.gradeTitle.setStyleSheet("color: white")
        self.gradeTitle.setAlignment(Qt.AlignCenter)
        
        self.compliment = QLabel("Great Job!", self)                 #Creates the QLabel for the compliment that changes depending on how many the user gets right
        self.compliment.setGeometry(60, 120, 480, 40)                #Sets all of the correct parameters for the compliment
        self.compliment.setFont(QFont("Impact", 15))
        self.compliment.setStyleSheet("color: #00529b")
        self.compliment.setAlignment(Qt.AlignCenter)
        
        self.q1Grade = QLabel(" ", self)                             #Each Question Grade QLabel displays if the question is correct/incorrect, as well as the correct answer
        self.q1Grade.setGeometry(60, 170, 540, 35)                   #Sets all of the corret parameters for the label
        self.q1Grade.setFont(QFont("Impact", 10))
        self.q1Grade.setAlignment(Qt.AlignLeft)
        
        self.q2Grade = QLabel(" ", self)                             #Question #2 Grade Label
        self.q2Grade.setGeometry(60, 208, 540, 35)
        self.q2Grade.setFont(QFont("Impact", 10))
        self.q2Grade.setAlignment(Qt.AlignLeft)
        
        self.q3Grade = QLabel(" ", self)                             #Question #3 Grade Label
        self.q3Grade.setGeometry(60, 246, 540, 35)
        self.q3Grade.setFont(QFont("Impact", 10))
        self.q3Grade.setAlignment(Qt.AlignLeft)
        
        self.q4Grade = QLabel(" ", self)                             #Question #4 Grade Label
        self.q4Grade.setGeometry(60, 284, 540, 35)
        self.q4Grade.setFont(QFont("Impact", 10))
        self.q4Grade.setAlignment(Qt.AlignLeft)
        
        self.q5Grade = QLabel(" ", self)                             #Question #5 Grade Label
        self.q5Grade.setGeometry(60, 322, 540, 35)
        self.q5Grade.setFont(QFont("Impact", 10))
        self.q5Grade.setAlignment(Qt.AlignLeft)
        
        self.printButton = QPushButton("Save PDF", self)                                           #The Print Button allows the user to create a printable PDF of the score, the question, and the correct answers
        self.printButton.setGeometry(305, 345, 235, 75)                                            #Sets the correct parameters for the Print Button
        self.printButton.setFont(QFont("Impact", 30))
        self.printButton.setStyleSheet('QPushButton {background-color: #be2f37; color: white;}')
        self.printButton.clicked.connect(lambda: self.printResults())                              #Connects the button to the printResults() function
        
    def gradeScreen(self):                                           #This function is called when the quiz is finished and the screen changes to the grade screen
    
        self.hideAnswerWidgets()                                     #Hides all of the widgets on the question screens
        
        #Grade All Possible Multiple Choice Questions
        
        if(self.line1[0] == "1"):                                    #This only runs if the first question is a Multiple-Choice Question
            if(self.q1Answer[int(self.line1[6])-1] == 1):            #Only runs if the bubble for the correct label (indicated by self.line1[6]) is toggled
                self.correct[0] = "Correct!   "                      #Sets the question to correct
                self.score += 1                                      #Increases the round's score
                self.q1Grade.setStyleSheet("color: #00ff00")         #Sets the grade message to green because it is correct
            else:                                                    #This only runs if the anwer to question 1 is wrong
                self.correct[0] = "Incorrect. "                      #Sets the question to incorrect
                self.q1Grade.setStyleSheet("color: #ff0000")         #Sets the grade message to red because it is incorrect
            self.q1Grade.setText("Question #1: " + self.correct[0] + "\tAnswer: " + self.line1[int(self.line1[6])+1])         #This sets the grade message as correct/incorrect and displays the correct answer
            
        if(self.line2[0] == "1"):                                    #Same as first function but only for question 2 multiple-choice questions
            if(self.q2Answer[int(self.line2[6])-1] == 1):
                self.correct[1] = "Correct!   "
                self.score += 1
                self.q2Grade.setStyleSheet("color: #00ff00")
            else:
                self.correct[1] = "Incorrect. "
                self.q2Grade.setStyleSheet("color: #ff0000")
            self.q2Grade.setText("Question #2: " + self.correct[1] + "\tAnswer: " + self.line2[int(self.line2[6])+1])
        
        if(self.line3[0] == "1"):                                    #Same as first function but only for question 3 multiple-choice questions
            if(self.q3Answer[int(self.line3[6])-1] == 1):
                self.correct[2] = "Correct!   "
                self.score += 1
                self.q3Grade.setStyleSheet("color: #00ff00")
            else:
                self.correct[2] = "Incorrect. "
                self.q3Grade.setStyleSheet("color: #ff0000")
            self.q3Grade.setText("Question #3: " + self.correct[2] + "\tAnswer: " + self.line3[int(self.line3[6])+1])
        
        if(self.line4[0] == "1"):                                    #Same as first function but only for question 4 multiple-choice questions
            if(self.q4Answer[int(self.line4[6])-1] == 1):
                self.correct[3] = "Correct!   "
                self.score += 1
                self.q4Grade.setStyleSheet("color: #00ff00")
            else:
                self.correct[3] = "Incorrect. "
                self.q4Grade.setStyleSheet("color: #ff0000")
            self.q4Grade.setText("Question #4: " + self.correct[3] + "\tAnswer: " + self.line4[int(self.line4[6])+1])
        
        if(self.line5[0] == "1"):                                    #Same as first function but only for question 5 multiple-choice questions
            if(self.q5Answer[int(self.line5[6])-1] == 1):
                self.correct[4] = "Correct!   "
                self.score += 1
                self.q5Grade.setStyleSheet("color: #00ff00")
            else:
                self.correct[4] = "Incorrect. "
                self.q5Grade.setStyleSheet("color: #ff0000")
            self.q5Grade.setText("Question #5: " + self.correct[4] + "\tAnswer: " + self.line5[int(self.line5[6])+1])
        
        #Grade All Possible Multi-Select Questions
        
        if(self.line1[0] == "2"):                                    #This only runs if the first question is a Multi-Select Question
            if(self.q1Answer[0] == int(self.line1[6]) and self.q1Answer[1] == int(self.line1[7]) and self.q1Answer[2] == int(self.line1[8]) and self.q1Answer[3] == int(self.line1[9])):        #Only runs if the checkboxes for the correct labels (indicated by self.line1[6] to line1[9]) are toggled
                self.correct[0] = "Correct!   "                      #Sets the question to correct
                self.score += 1                                      #Increases the round's score
                self.q1Grade.setStyleSheet("color: #00ff00")         #Sets the grade message to green because it is correct
            else:                                                    #This only runs if the anwer to question 1 is wrong
                self.correct[0] = "Incorrect. "                      #Sets the question to incorrect
                self.q1Grade.setStyleSheet("color: #ff0000")         #Sets the grade message to red because it is incorrect
            self.q1Grade.setText("Question #1: " + self.correct[0] + "\tAnswers: " + self.line1[2] * int(self.line1[6]) + " - " + self.line1[3] * int(self.line1[7]) + " - " + self.line1[4] * int(self.line1[8]) + " - " + self.line1[5] * int(self.line1[9]) )           #This sets the grade message as correct/incorrect and displays the correct answers to the right options
        
        if(self.line2[0] == "2"):                                    #Same as first function but only for question 2 multi-select questions
            if(self.q2Answer[0] == int(self.line2[6]) and self.q2Answer[1] == int(self.line2[7]) and self.q2Answer[2] == int(self.line2[8]) and self.q2Answer[3] == int(self.line2[9])):
                self.correct[1] = "Correct!   "
                self.score += 1
                self.q2Grade.setStyleSheet("color: #00ff00")
            else:
                self.correct[1] = "Incorrect. "
                self.q2Grade.setStyleSheet("color: #ff0000")
            self.q2Grade.setText("Question #2: " + self.correct[1] + "\tAnswers: " + self.line2[2] * int(self.line2[6]) + " - " + self.line2[3] * int(self.line2[7]) + " - " + self.line2[4] * int(self.line2[8]) + " - " + self.line2[5] * int(self.line2[9]) )
        
        if(self.line3[0] == "2"):                                    #Same as first function but only for question 3 multi-select questions
            if(self.q3Answer[0] == int(self.line3[6]) and self.q3Answer[1] == int(self.line3[7]) and self.q3Answer[2] == int(self.line3[8]) and self.q3Answer[3] == int(self.line3[9])):
                self.correct[2] = "Correct!   "
                self.score += 1
                self.q3Grade.setStyleSheet("color: #00ff00")
            else:
                self.correct[2] = "Incorrect. "
                self.q3Grade.setStyleSheet("color: #ff0000")
            self.q3Grade.setText("Question #3: " + self.correct[2] + "\tAnswers: " + self.line3[2] * int(self.line3[6]) + " - " + self.line3[3] * int(self.line3[7]) + " - " + self.line3[4] * int(self.line3[8]) + " - " + self.line3[5] * int(self.line3[9]) )
        
        if(self.line4[0] == "2"):                                    #Same as first function but only for question 4 multi-select questions
            if(self.q4Answer[0] == int(self.line4[6]) and self.q4Answer[1] == int(self.line4[7]) and self.q4Answer[2] == int(self.line4[8]) and self.q4Answer[3] == int(self.line4[9])):
                self.correct[3] = "Correct!   "
                self.score += 1
                self.q4Grade.setStyleSheet("color: #00ff00")
            else:
                self.correct[3] = "Incorrect. "
                self.q4Grade.setStyleSheet("color: #ff0000")
            self.q4Grade.setText("Question #4: " + self.correct[3] + "\tAnswers: " + self.line4[2] * int(self.line4[6]) + " - " + self.line4[3] * int(self.line4[7]) + " - " + self.line4[4] * int(self.line4[8]) + " - " + self.line4[5] * int(self.line4[9]) )
        
        if(self.line5[0] == "2"):                                    #Same as first function but only for question 5 multi-select questions
            if(self.q5Answer[0] == int(self.line5[6]) and self.q5Answer[1] == int(self.line5[7]) and self.q5Answer[2] == int(self.line5[8]) and self.q5Answer[3] == int(self.line5[9])):
                self.correct[4] = "Correct!   "
                self.score += 1
                self.q5Grade.setStyleSheet("color: #00ff00")
            else:
                self.correct[4] = "Incorrect. "
                self.q5Grade.setStyleSheet("color: #ff0000")
            self.q5Grade.setText("Question #5: " + self.correct[4] + "\tAnswers: " + self.line5[2] * int(self.line5[6]) + " - " + self.line5[3] * int(self.line5[7]) + " - " + self.line5[4] * int(self.line5[8]) + " - " + self.line5[5] * int(self.line5[9]) )
        
        
        #Grade All Possible True/False Questions
        
        if(self.line1[0] == "3"):                                    #Same as Multiple-Choice functions but only for question 1 true/false questions
            if(self.q1Answer[int(self.line1[4])-1] == 1):
                self.correct[0] = "Correct!   "
                self.score += 1
                self.q1Grade.setStyleSheet("color: #00ff00")
            else:
                self.correct[0] = "Incorrect. "
                self.q1Grade.setStyleSheet("color: #ff0000")
            self.q1Grade.setText("Question #1: " + self.correct[0] + "\tAnswer: " + self.line1[int(self.line1[4])+1])
        
        if(self.line2[0] == "3"):                                    #Same as Multiple-Choice functions but only for question 2 true/false questions
            if(self.q2Answer[int(self.line2[4])-1] == 1):
                self.correct[1] = "Correct!   "
                self.score += 1
                self.q2Grade.setStyleSheet("color: #00ff00")
            else:
                self.correct[1] = "Incorrect. "
                self.q2Grade.setStyleSheet("color: #ff0000")
            self.q2Grade.setText("Question #2: " + self.correct[1] + "\tAnswer: " + self.line2[int(self.line2[4])+1])
        
        if(self.line3[0] == "3"):                                    #Same as Multiple-Choice functions but only for question 3 true/false questions
            if(self.q3Answer[int(self.line3[4])-1] == 1):
                self.correct[2] = "Correct!   "
                self.score += 1
                self.q3Grade.setStyleSheet("color: #00ff00")
            else:
                self.correct[2] = "Incorrect. "
                self.q3Grade.setStyleSheet("color: #ff0000")
            self.q3Grade.setText("Question #3: " + self.correct[2] + "\tAnswer: " + self.line3[int(self.line3[4])+1])
        
        if(self.line4[0] == "3"):                                    #Same as Multiple-Choice functions but only for question 4 true/false questions
            if(self.q4Answer[int(self.line4[4])-1] == 1):
                self.correct[3] = "Correct!   "
                self.score += 1
                self.q4Grade.setStyleSheet("color: #00ff00")
            else:
                self.correct[3] = "Incorrect. "
                self.q4Grade.setStyleSheet("color: #ff0000")
            self.q4Grade.setText("Question #4: " + self.correct[3] + "\tAnswer: " + self.line4[int(self.line4[4])+1])
        
        if(self.line5[0] == "3"):                                    #Same as Multiple-Choice functions but only for question 5 true/false questions
            if(self.q5Answer[int(self.line5[4])-1] == 1):
                self.correct[4] = "Correct!   "
                self.score += 1
                self.q5Grade.setStyleSheet("color: #00ff00")
            else:
                self.correct[4] = "Incorrect. "
                self.q5Grade.setStyleSheet("color: #ff0000")
            self.q5Grade.setText("Question #5: " + self.correct[4] + "\tAnswer: " + self.line5[int(self.line5[4])+1])
        
        
        #Grade All Possible Matching Questions
        
        if(self.line1[0] == "4"):                                    #Same as other question functions but only for question 1 matching questions
            if(self.q1Answer[0] == int(self.line1[10]) and self.q1Answer[1] == int(self.line1[11]) and self.q1Answer[2] == int(self.line1[12]) and self.q1Answer[3] == int(self.line1[13])):                #This only runs if the answers for the dropdown boxes match what is on the database
                self.correct[0] = "Correct!   "
                self.score += 1
                self.q1Grade.setStyleSheet("color: #00ff00")
            else:
                self.correct[0] = "Incorrect. "
                self.q1Grade.setStyleSheet("color: #ff0000")
            self.q1Grade.setText("Question #1: " + self.correct[0] + "\tAnswers (In Order): " + chr(64 + int(self.line1[10])) + ", " + chr(64 + int(self.line1[11])) + ", " + chr(64 + int(self.line1[12])) + ", " + chr(64 + int(self.line1[13])) )     #States the order of the letters by using the chr() function and translating the answer key to letters
        
        if(self.line2[0] == "4"):                                    #Same as first function but only for question 2 matching questions
            if(self.q2Answer[0] == int(self.line2[10]) and self.q2Answer[1] == int(self.line2[11]) and self.q2Answer[2] == int(self.line2[12]) and self.q2Answer[3] == int(self.line2[13])):
                self.correct[1] = "Correct!   "
                self.score += 1
                self.q2Grade.setStyleSheet("color: #00ff00")
            else:
                self.correct[1] = "Incorrect. "
                self.q2Grade.setStyleSheet("color: #ff0000")
            self.q2Grade.setText("Question #2: " + self.correct[1] + "\tAnswers (In Order): " + chr(64 + int(self.line2[10])) + ", " + chr(64 + int(self.line2[11])) + ", " + chr(64 + int(self.line2[12])) + ", " + chr(64 + int(self.line2[13])) )
        
        if(self.line3[0] == "4"):                                    #Same as first function but only for question 3 matching questions
            if(self.q3Answer[0] == int(self.line3[10]) and self.q3Answer[1] == int(self.line3[11]) and self.q3Answer[2] == int(self.line3[12]) and self.q3Answer[3] == int(self.line3[13])):
                self.correct[2] = "Correct!   "
                self.score += 1
                self.q3Grade.setStyleSheet("color: #00ff00")
            else:
                self.correct[2] = "Incorrect. "
                self.q3Grade.setStyleSheet("color: #ff0000")
            self.q3Grade.setText("Question #3: " + self.correct[2] + "\tAnswers (In Order): " + chr(64 + int(self.line3[10])) + ", " + chr(64 + int(self.line3[11])) + ", " + chr(64 + int(self.line3[12])) + ", " + chr(64 + int(self.line3[13])) )
        
        if(self.line4[0] == "4"):                                    #Same as first function but only for question 4 matching questions
            if(self.q4Answer[0] == int(self.line4[10]) and self.q4Answer[1] == int(self.line4[11]) and self.q4Answer[2] == int(self.line4[12]) and self.q4Answer[3] == int(self.line4[13])):
                self.correct[3] = "Correct!   "
                self.score += 1
                self.q4Grade.setStyleSheet("color: #00ff00")
            else:
                self.correct[3] = "Incorrect. "
                self.q4Grade.setStyleSheet("color: #ff0000")
            self.q4Grade.setText("Question #4: " + self.correct[3] + "\tAnswers (In Order): " + chr(64 + int(self.line4[10])) + ", " + chr(64 + int(self.line4[11])) + ", " + chr(64 + int(self.line4[12])) + ", " + chr(64 + int(self.line4[13])) )
        
        if(self.line5[0] == "4"):                                    #Same as first function but only for question 5 matching questions
            if(self.q5Answer[0] == int(self.line5[10]) and self.q5Answer[1] == int(self.line5[11]) and self.q5Answer[2] == int(self.line5[12]) and self.q5Answer[3] == int(self.line5[13])):
                self.correct[4] = "Correct!   "
                self.score += 1
                self.q5Grade.setStyleSheet("color: #00ff00")
            else:
                self.correct[4] = "Incorrect. "
                self.q5Grade.setStyleSheet("color: #ff0000")
            self.q5Grade.setText("Question #5: " + self.correct[4] + "\tAnswers (In Order): " + chr(64 + int(self.line5[10])) + ", " + chr(64 + int(self.line5[11])) + ", " + chr(64 + int(self.line5[12])) + ", " + chr(64 + int(self.line5[13])) )
        
        
        
        if(self.score >= 3):                          #If the score is 3 or more, the text turns green and the green smiley face appears
            self.greenSmiley.show()
            self.compliment.setStyleSheet("color: #00ff00")
            if(self.score == 4 or self.score == 3):
                self.compliment.setText("Great Work! Keep it up and you can get a PERFECT score!")    #The message changes depending on if the score was PERFECT
            elif(self.score == 5):
                self.compliment.setText("You earned a PERFECT score and know a lot about FBLA!")
                
        else:                                         #If the score is 2 or less, the text turns red, the red smiley face appears, and the specfic text changes
            self.redSmiley.show()
            self.compliment.setStyleSheet("color: #ff0000")
            self.compliment.setText("Nice try! Keep practicing to increase your score!")
        
        self.gradeTitle.setText("Score: " + str(self.score) + "/5")        #The title of the grade screen includes the score that the user recieves
        
        
        
        self.q1Grade.show()            #Shows all of the grade messages for questions 1-5
        self.q2Grade.show()
        self.q3Grade.show()
        self.q4Grade.show()
        self.q5Grade.show()
        
        self.compliment.show()         #Shows the compliment
        self.gradeTitle.show()         #Shows the title for the grade screen
        self.exitButton.show()         #Shows the exit button
        self.printButton.show()        #Shows the print button
        
    def question(self):                #This is definitely the biggest function. It changes to a question and shows the correct widgets
    
        self.img.hide()                #Hides all of the widgets on the Main Screen
        self.button.hide()
        self.quitButton.hide()
        self.label.hide()
        self.label2.hide()
    
        self.question_header.setText("Question #" + str(self.screen))         #Sets and shows the question header that displays the question number
        self.question_header.show()
        
        if(self.screen == 1):                            #Each of these sets the prompt for each question as what is in the database depending on what screen it is on
            self.questionName.setText(self.line1[1])
        if(self.screen == 2):
            self.questionName.setText(self.line2[1])
        if(self.screen == 3):
            self.questionName.setText(self.line3[1])
        if(self.screen == 4):
            self.questionName.setText(self.line4[1])
        if(self.screen == 5):
            self.questionName.setText(self.line5[1])
        
        self.questionName.show()                         #Shows the question prompt
                
        if(self.screen < 5):                             #These here show the exit button on the first question and the finish button on the last question, and the previous and next buttons on all others
            self.nextButton.show()
        else:
            self.finishButton.show()
        
        if(self.screen > 1):
            self.previousButton.show()
        else:
            self.exitButton.show()
            
                                                         #The next 600 lines (about) here set the question up depending on self.screen (which question) and self.line#[0] (what type of question)
        
        ####START OF SCREEN 1 IN QUESTION FUNCTION---------------------------------------------------------------------------------

        
        if(self.screen == 1):                                              #This whole part is only for screen 1 and question 1
            if(self.line1[0] == "1"):                                      #This is for Multiple-Choice questions
                self.questionType.setText("Type: " + "Multiple Choice")    #This displays the type of question
                
                if(self.q1Answer[0] == 1):                                 #This toggles or untoggles the first radio button if the user has already answered the question
                    self.radioButton1.setChecked(True)
                else:
                    self.radioButton1.setAutoExclusive(False)              #This method had to be used or else it would not uncheck itself
                    self.radioButton1.setChecked(False)
                    self.radioButton1.setAutoExclusive(True)
                
                if(self.q1Answer[1] == 1):
                    self.radioButton2.setChecked(True)
                else:
                    self.radioButton2.setAutoExclusive(False)
                    self.radioButton2.setChecked(False)
                    self.radioButton2.setAutoExclusive(True)
                
                if(self.q1Answer[2] == 1):
                    self.radioButton3.setChecked(True)
                else:
                    self.radioButton3.setAutoExclusive(False)
                    self.radioButton3.setChecked(False)
                    self.radioButton3.setAutoExclusive(True)
                
                if(self.q1Answer[3] == 1):
                    self.radioButton4.setChecked(True)
                else:
                    self.radioButton4.setAutoExclusive(False)
                    self.radioButton4.setChecked(False)
                    self.radioButton4.setAutoExclusive(True)
                
                
                self.radioButton1.setText(self.line1[2])                   #These here set the text next to the radio buttons to the answer options in the database
                self.radioButton2.setText(self.line1[3])
                self.radioButton3.setText(self.line1[4])
                self.radioButton4.setText(self.line1[5])
                self.radioButton1.show()                                   #These show all 4 radio buttons
                self.radioButton2.show()
                self.radioButton3.show()
                self.radioButton4.show()
                
            if(self.line1[0] == "2"):                                      #This section is similar to the Multiple-Choice questions, but it instead uses the Multi-Select questions and the checkboxes
                self.questionType.setText("Type: " + "Multi-Select")
                
                if(self.q1Answer[0] == 1):
                    self.checkBox1.setCheckState(Qt.Checked)
                else:
                    self.checkBox1.setCheckState(Qt.Unchecked)
                
                if(self.q1Answer[1] == 1):
                    self.checkBox2.setCheckState(Qt.Checked)
                else:
                    self.checkBox2.setCheckState(Qt.Unchecked)
                
                if(self.q1Answer[2] == 1):
                    self.checkBox3.setCheckState(Qt.Checked)
                else:
                    self.checkBox3.setCheckState(Qt.Unchecked)
                
                if(self.q1Answer[3] == 1):
                    self.checkBox4.setCheckState(Qt.Checked)
                else:
                    self.checkBox4.setCheckState(Qt.Unchecked)
                
                
                self.checkBox1.setText(self.line1[2])
                self.checkBox2.setText(self.line1[3])
                self.checkBox3.setText(self.line1[4])
                self.checkBox4.setText(self.line1[5])
                self.checkBox1.show()
                self.checkBox2.show()
                self.checkBox3.show()
                self.checkBox4.show()
                
            if(self.line1[0] == "3"):                                      #This section is similar to the Multiple-Choice questions, but it instead uses the True/False questions and only 2 radio buttons
                self.questionType.setText("Type: " + "True/False")
                
                if(self.q1Answer[0] == 1):
                    self.trueButton.setChecked(True)
                else:
                    self.trueButton.setAutoExclusive(False)
                    self.trueButton.setChecked(False)
                    self.trueButton.setAutoExclusive(True)
                
                if(self.q1Answer[1] == 1):
                    self.falseButton.setChecked(True)
                else:
                    self.falseButton.setAutoExclusive(False)
                    self.falseButton.setChecked(False)
                    self.falseButton.setAutoExclusive(True)

                
                self.trueButton.show()
                self.falseButton.show()
        
            if(self.line1[0] == "4"):                                   #This section is similar to the Multiple-Choice questions, but it instead uses the Matching questions and the combo-boxes
                self.questionType.setText("Type: " + "Matching")
                
                self.comboBox1.setCurrentIndex(self.q1Answer[0])        #These set the selected choice for each combo box to what the user has already selected
                self.comboBox2.setCurrentIndex(self.q1Answer[1])
                self.comboBox3.setCurrentIndex(self.q1Answer[2])
                self.comboBox4.setCurrentIndex(self.q1Answer[3])
                
                self.match1.setText(self.line1[6])                      #These set the choice to match and the letter of each
                self.description1.setText("(A) " + self.line1[2])
                self.match2.setText(self.line1[7])
                self.description2.setText("(B) " + self.line1[3])
                self.match3.setText(self.line1[8])
                self.description3.setText("(C) " + self.line1[4])
                self.match4.setText(self.line1[9])
                self.description4.setText("(D) " + self.line1[5])
                
                self.comboBox1.show()
                self.match1.show()
                self.description1.show()
                self.comboBox2.show()
                self.match2.show()
                self.description2.show()
                self.comboBox3.show()
                self.match3.show()
                self.description3.show()
                self.comboBox4.show()
                self.match4.show()
                self.description4.show()
        
        ####START OF SCREEN 2 IN QUESTION FUNCTION---------------------------------------------------------------------------------

        
        if(self.screen == 2):                                           #This section is exactly the same as the prevous one, but it relates to question #2 (self.screen == 2, self.line2, self.q2Answer)
            if(self.line2[0] == "1"):
                self.questionType.setText("Type: " + "Multiple Choice")
                
                if(self.q2Answer[0] == 1):
                    self.radioButton1.setChecked(True)
                else:
                    self.radioButton1.setAutoExclusive(False)
                    self.radioButton1.setChecked(False)
                    self.radioButton1.setAutoExclusive(True)
                
                if(self.q2Answer[1] == 1):
                    self.radioButton2.setChecked(True)
                else:
                    self.radioButton2.setAutoExclusive(False)
                    self.radioButton2.setChecked(False)
                    self.radioButton2.setAutoExclusive(True)
                
                if(self.q2Answer[2] == 1):
                    self.radioButton3.setChecked(True)
                else:
                    self.radioButton3.setAutoExclusive(False)
                    self.radioButton3.setChecked(False)
                    self.radioButton3.setAutoExclusive(True)
                
                if(self.q2Answer[3] == 1):
                    self.radioButton4.setChecked(True)
                else:
                    self.radioButton4.setAutoExclusive(False)
                    self.radioButton4.setChecked(False)
                    self.radioButton4.setAutoExclusive(True)
                
                
                self.radioButton1.setText(self.line2[2])
                self.radioButton2.setText(self.line2[3])
                self.radioButton3.setText(self.line2[4])
                self.radioButton4.setText(self.line2[5])
                self.radioButton1.show()
                self.radioButton2.show()
                self.radioButton3.show()
                self.radioButton4.show()
                
            if(self.line2[0] == "2"):
                self.questionType.setText("Type: " + "Multi-Select")
                
                if(self.q2Answer[0] == 1):
                    self.checkBox1.setCheckState(Qt.Checked)
                else:
                    self.checkBox1.setCheckState(Qt.Unchecked)
                
                if(self.q2Answer[1] == 1):
                    self.checkBox2.setCheckState(Qt.Checked)
                else:
                    self.checkBox2.setCheckState(Qt.Unchecked)
                
                if(self.q2Answer[2] == 1):
                    self.checkBox3.setCheckState(Qt.Checked)
                else:
                    self.checkBox3.setCheckState(Qt.Unchecked)
                
                if(self.q2Answer[3] == 1):
                    self.checkBox4.setCheckState(Qt.Checked)
                else:
                    self.checkBox4.setCheckState(Qt.Unchecked)
                
                
                self.checkBox1.setText(self.line2[2])
                self.checkBox2.setText(self.line2[3])
                self.checkBox3.setText(self.line2[4])
                self.checkBox4.setText(self.line2[5])
                self.checkBox1.show()
                self.checkBox2.show()
                self.checkBox3.show()
                self.checkBox4.show()
                
            if(self.line2[0] == "3"):
                self.questionType.setText("Type: " + "True/False")
                
                if(self.q2Answer[0] == 1):
                    self.trueButton.setChecked(True)
                else:
                    self.trueButton.setAutoExclusive(False)
                    self.trueButton.setChecked(False)
                    self.trueButton.setAutoExclusive(True)
                
                if(self.q2Answer[1] == 1):
                    self.falseButton.setChecked(True)
                else:
                    self.falseButton.setAutoExclusive(False)
                    self.falseButton.setChecked(False)
                    self.falseButton.setAutoExclusive(True)

                
                self.trueButton.show()
                self.falseButton.show()
        
            if(self.line2[0] == "4"):
                self.questionType.setText("Type: " + "Matching")
                
                self.comboBox1.setCurrentIndex(self.q2Answer[0])
                self.comboBox2.setCurrentIndex(self.q2Answer[1])
                self.comboBox3.setCurrentIndex(self.q2Answer[2])
                self.comboBox4.setCurrentIndex(self.q2Answer[3])
                
                self.match1.setText(self.line2[6])
                self.description1.setText("(A) " + self.line2[2])
                self.match2.setText(self.line2[7])
                self.description2.setText("(B) " + self.line2[3])
                self.match3.setText(self.line2[8])
                self.description3.setText("(C) " + self.line2[4])
                self.match4.setText(self.line2[9])
                self.description4.setText("(D) " + self.line2[5])
                
                self.comboBox1.show()
                self.match1.show()
                self.description1.show()
                self.comboBox2.show()
                self.match2.show()
                self.description2.show()
                self.comboBox3.show()
                self.match3.show()
                self.description3.show()
                self.comboBox4.show()
                self.match4.show()
                self.description4.show()

        
        ####START OF SCREEN 3 IN QUESTION FUNCTION---------------------------------------------------------------------------------

        
        if(self.screen == 3):                                           #This section is exactly the same as the prevous one, but it relates to question #3 (self.screen == 3, self.line3, self.q3Answer)
            if(self.line3[0] == "1"):
                self.questionType.setText("Type: " + "Multiple Choice")
                
                if(self.q3Answer[0] == 1):
                    self.radioButton1.setChecked(True)
                else:
                    self.radioButton1.setAutoExclusive(False)
                    self.radioButton1.setChecked(False)
                    self.radioButton1.setAutoExclusive(True)
                
                if(self.q3Answer[1] == 1):
                    self.radioButton2.setChecked(True)
                else:
                    self.radioButton2.setAutoExclusive(False)
                    self.radioButton2.setChecked(False)
                    self.radioButton2.setAutoExclusive(True)
                
                if(self.q3Answer[2] == 1):
                    self.radioButton3.setChecked(True)
                else:
                    self.radioButton3.setAutoExclusive(False)
                    self.radioButton3.setChecked(False)
                    self.radioButton3.setAutoExclusive(True)
                
                if(self.q3Answer[3] == 1):
                    self.radioButton4.setChecked(True)
                else:
                    self.radioButton4.setAutoExclusive(False)
                    self.radioButton4.setChecked(False)
                    self.radioButton4.setAutoExclusive(True)
                
                
                self.radioButton1.setText(self.line3[2])
                self.radioButton2.setText(self.line3[3])
                self.radioButton3.setText(self.line3[4])
                self.radioButton4.setText(self.line3[5])
                self.radioButton1.show()
                self.radioButton2.show()
                self.radioButton3.show()
                self.radioButton4.show()
                
            if(self.line3[0] == "2"):
                self.questionType.setText("Type: " + "Multi-Select")
                
                if(self.q3Answer[0] == 1):
                    self.checkBox1.setCheckState(Qt.Checked)
                else:
                    self.checkBox1.setCheckState(Qt.Unchecked)
                
                if(self.q3Answer[1] == 1):
                    self.checkBox2.setCheckState(Qt.Checked)
                else:
                    self.checkBox2.setCheckState(Qt.Unchecked)
                
                if(self.q3Answer[2] == 1):
                    self.checkBox3.setCheckState(Qt.Checked)
                else:
                    self.checkBox3.setCheckState(Qt.Unchecked)
                
                if(self.q3Answer[3] == 1):
                    self.checkBox4.setCheckState(Qt.Checked)
                else:
                    self.checkBox4.setCheckState(Qt.Unchecked)
                
                
                self.checkBox1.setText(self.line3[2])
                self.checkBox2.setText(self.line3[3])
                self.checkBox3.setText(self.line3[4])
                self.checkBox4.setText(self.line3[5])
                self.checkBox1.show()
                self.checkBox2.show()
                self.checkBox3.show()
                self.checkBox4.show()
                
            if(self.line3[0] == "3"):
                self.questionType.setText("Type: " + "True/False")
                
                if(self.q3Answer[0] == 1):
                    self.trueButton.setChecked(True)
                else:
                    self.trueButton.setAutoExclusive(False)
                    self.trueButton.setChecked(False)
                    self.trueButton.setAutoExclusive(True)
                
                if(self.q3Answer[1] == 1):
                    self.falseButton.setChecked(True)
                else:
                    self.falseButton.setAutoExclusive(False)
                    self.falseButton.setChecked(False)
                    self.falseButton.setAutoExclusive(True)

                
                self.trueButton.show()
                self.falseButton.show()
        
            if(self.line3[0] == "4"):
                self.questionType.setText("Type: " + "Matching")
                
                self.comboBox1.setCurrentIndex(self.q3Answer[0])
                self.comboBox2.setCurrentIndex(self.q3Answer[1])
                self.comboBox3.setCurrentIndex(self.q3Answer[2])
                self.comboBox4.setCurrentIndex(self.q3Answer[3])
                
                self.match1.setText(self.line3[6])
                self.description1.setText("(A) " + self.line3[2])
                self.match2.setText(self.line3[7])
                self.description2.setText("(B) " + self.line3[3])
                self.match3.setText(self.line3[8])
                self.description3.setText("(C) " + self.line3[4])
                self.match4.setText(self.line3[9])
                self.description4.setText("(D) " + self.line3[5])
                
                self.comboBox1.show()
                self.match1.show()
                self.description1.show()
                self.comboBox2.show()
                self.match2.show()
                self.description2.show()
                self.comboBox3.show()
                self.match3.show()
                self.description3.show()
                self.comboBox4.show()
                self.match4.show()
                self.description4.show()

        ####START OF SCREEN 4 IN QUESTION FUNCTION---------------------------------------------------------------------------------
        
        
        if(self.screen == 4):                                           #This section is exactly the same as the prevous one, but it relates to question #4 (self.screen == 4, self.line4, self.q4Answer)
            if(self.line4[0] == "1"):
                self.questionType.setText("Type: " + "Multiple Choice")
                
                if(self.q4Answer[0] == 1):
                    self.radioButton1.setChecked(True)
                else:
                    self.radioButton1.setAutoExclusive(False)
                    self.radioButton1.setChecked(False)
                    self.radioButton1.setAutoExclusive(True)
                
                if(self.q4Answer[1] == 1):
                    self.radioButton2.setChecked(True)
                else:
                    self.radioButton2.setAutoExclusive(False)
                    self.radioButton2.setChecked(False)
                    self.radioButton2.setAutoExclusive(True)
                
                if(self.q4Answer[2] == 1):
                    self.radioButton3.setChecked(True)
                else:
                    self.radioButton3.setAutoExclusive(False)
                    self.radioButton3.setChecked(False)
                    self.radioButton3.setAutoExclusive(True)
                
                if(self.q4Answer[3] == 1):
                    self.radioButton4.setChecked(True)
                else:
                    self.radioButton4.setAutoExclusive(False)
                    self.radioButton4.setChecked(False)
                    self.radioButton4.setAutoExclusive(True)
                
                
                self.radioButton1.setText(self.line4[2])
                self.radioButton2.setText(self.line4[3])
                self.radioButton3.setText(self.line4[4])
                self.radioButton4.setText(self.line4[5])
                self.radioButton1.show()
                self.radioButton2.show()
                self.radioButton3.show()
                self.radioButton4.show()
                
            if(self.line4[0] == "2"):
                self.questionType.setText("Type: " + "Multi-Select")
                
                if(self.q4Answer[0] == 1):
                    self.checkBox1.setCheckState(Qt.Checked)
                else:
                    self.checkBox1.setCheckState(Qt.Unchecked)
                
                if(self.q4Answer[1] == 1):
                    self.checkBox2.setCheckState(Qt.Checked)
                else:
                    self.checkBox2.setCheckState(Qt.Unchecked)
                
                if(self.q4Answer[2] == 1):
                    self.checkBox3.setCheckState(Qt.Checked)
                else:
                    self.checkBox3.setCheckState(Qt.Unchecked)
                
                if(self.q4Answer[3] == 1):
                    self.checkBox4.setCheckState(Qt.Checked)
                else:
                    self.checkBox4.setCheckState(Qt.Unchecked)
                
                
                self.checkBox1.setText(self.line4[2])
                self.checkBox2.setText(self.line4[3])
                self.checkBox3.setText(self.line4[4])
                self.checkBox4.setText(self.line4[5])
                self.checkBox1.show()
                self.checkBox2.show()
                self.checkBox3.show()
                self.checkBox4.show()
                
            if(self.line4[0] == "3"):
                self.questionType.setText("Type: " + "True/False")
                
                if(self.q4Answer[0] == 1):
                    self.trueButton.setChecked(True)
                else:
                    self.trueButton.setAutoExclusive(False)
                    self.trueButton.setChecked(False)
                    self.trueButton.setAutoExclusive(True)
                
                if(self.q4Answer[1] == 1):
                    self.falseButton.setChecked(True)
                else:
                    self.falseButton.setAutoExclusive(False)
                    self.falseButton.setChecked(False)
                    self.falseButton.setAutoExclusive(True)

                
                self.trueButton.show()
                self.falseButton.show()
        
            if(self.line4[0] == "4"):
                self.questionType.setText("Type: " + "Matching")
                
                self.comboBox1.setCurrentIndex(self.q4Answer[0])
                self.comboBox2.setCurrentIndex(self.q4Answer[1])
                self.comboBox3.setCurrentIndex(self.q4Answer[2])
                self.comboBox4.setCurrentIndex(self.q4Answer[3])
                
                self.match1.setText(self.line4[6])
                self.description1.setText("(A) " + self.line4[2])
                self.match2.setText(self.line4[7])
                self.description2.setText("(B) " + self.line4[3])
                self.match3.setText(self.line4[8])
                self.description3.setText("(C) " + self.line4[4])
                self.match4.setText(self.line4[9])
                self.description4.setText("(D) " + self.line4[5])
                
                self.comboBox1.show()
                self.match1.show()
                self.description1.show()
                self.comboBox2.show()
                self.match2.show()
                self.description2.show()
                self.comboBox3.show()
                self.match3.show()
                self.description3.show()
                self.comboBox4.show()
                self.match4.show()
                self.description4.show()

        ####START OF SCREEN 5 IN QUESTION FUNCTION---------------------------------------------------------------------------------
        
        
        if(self.screen == 5):                                           #This section is exactly the same as the prevous one, but it relates to question #5 (self.screen == 5, self.line5, self.q5Answer)
            if(self.line5[0] == "1"):
                self.questionType.setText("Type: " + "Multiple Choice")
                
                if(self.q5Answer[0] == 1):
                    self.radioButton1.setChecked(True)
                else:
                    self.radioButton1.setAutoExclusive(False)
                    self.radioButton1.setChecked(False)
                    self.radioButton1.setAutoExclusive(True)
                
                if(self.q5Answer[1] == 1):
                    self.radioButton2.setChecked(True)
                else:
                    self.radioButton2.setAutoExclusive(False)
                    self.radioButton2.setChecked(False)
                    self.radioButton2.setAutoExclusive(True)
                
                if(self.q5Answer[2] == 1):
                    self.radioButton3.setChecked(True)
                else:
                    self.radioButton3.setAutoExclusive(False)
                    self.radioButton3.setChecked(False)
                    self.radioButton3.setAutoExclusive(True)
                
                if(self.q5Answer[3] == 1):
                    self.radioButton4.setChecked(True)
                else:
                    self.radioButton4.setAutoExclusive(False)
                    self.radioButton4.setChecked(False)
                    self.radioButton4.setAutoExclusive(True)
                
                
                self.radioButton1.setText(self.line5[2])
                self.radioButton2.setText(self.line5[3])
                self.radioButton3.setText(self.line5[4])
                self.radioButton4.setText(self.line5[5])
                self.radioButton1.show()
                self.radioButton2.show()
                self.radioButton3.show()
                self.radioButton4.show()
                
            if(self.line5[0] == "2"):
                self.questionType.setText("Type: " + "Multi-Select")
                
                if(self.q5Answer[0] == 1):
                    self.checkBox1.setCheckState(Qt.Checked)
                else:
                    self.checkBox1.setCheckState(Qt.Unchecked)
                
                if(self.q5Answer[1] == 1):
                    self.checkBox2.setCheckState(Qt.Checked)
                else:
                    self.checkBox2.setCheckState(Qt.Unchecked)
                
                if(self.q5Answer[2] == 1):
                    self.checkBox3.setCheckState(Qt.Checked)
                else:
                    self.checkBox3.setCheckState(Qt.Unchecked)
                
                if(self.q5Answer[3] == 1):
                    self.checkBox4.setCheckState(Qt.Checked)
                else:
                    self.checkBox4.setCheckState(Qt.Unchecked)
                
                
                self.checkBox1.setText(self.line5[2])
                self.checkBox2.setText(self.line5[3])
                self.checkBox3.setText(self.line5[4])
                self.checkBox4.setText(self.line5[5])
                self.checkBox1.show()
                self.checkBox2.show()
                self.checkBox3.show()
                self.checkBox4.show()
                
            if(self.line5[0] == "3"):
                self.questionType.setText("Type: " + "True/False")
                
                if(self.q5Answer[0] == 1):
                    self.trueButton.setChecked(True)
                else:
                    self.trueButton.setAutoExclusive(False)
                    self.trueButton.setChecked(False)
                    self.trueButton.setAutoExclusive(True)
                
                if(self.q5Answer[1] == 1):
                    self.falseButton.setChecked(True)
                else:
                    self.falseButton.setAutoExclusive(False)
                    self.falseButton.setChecked(False)
                    self.falseButton.setAutoExclusive(True)

                
                self.trueButton.show()
                self.falseButton.show()
        
            if(self.line5[0] == "4"):
                self.questionType.setText("Type: " + "Matching")
                
                self.comboBox1.setCurrentIndex(self.q5Answer[0])
                self.comboBox2.setCurrentIndex(self.q5Answer[1])
                self.comboBox3.setCurrentIndex(self.q5Answer[2])
                self.comboBox4.setCurrentIndex(self.q5Answer[3])
                
                self.match1.setText(self.line5[6])
                self.description1.setText("(A) " + self.line5[2])
                self.match2.setText(self.line5[7])
                self.description2.setText("(B) " + self.line5[3])
                self.match3.setText(self.line5[8])
                self.description3.setText("(C) " + self.line5[4])
                self.match4.setText(self.line5[9])
                self.description4.setText("(D) " + self.line5[5])
                
                self.comboBox1.show()
                self.match1.show()
                self.description1.show()
                self.comboBox2.show()
                self.match2.show()
                self.description2.show()
                self.comboBox3.show()
                self.match3.show()
                self.description3.show()
                self.comboBox4.show()
                self.match4.show()
                self.description4.show()

        ####END OF QUESTION FUCTION-------------------------------------------------------------------------------------
        
        self.questionType.show()             #Shows the type of question

        
    def initQuestion(self):                                       #This function initializes all of the widgets and variables of the question screen
    
        
        self.question_header = QLabel(' ', self)                  #The question header shows the question number at the top of the screen
        self.question_header.setGeometry(30, 30, 540, 80)
        self.question_header.setFont(QFont("Impact", 40))
        self.question_header.setStyleSheet("color: white")
        self.question_header.setAlignment(Qt.AlignCenter)
        
        self.questionType = QLabel(' ', self)                     #The question type shows what type of question the screen shows (Multiple Choice, Multi-Select, True/False, Matching)
        self.questionType.setGeometry(60, 120, 200, 40)
        self.questionType.setFont(QFont("Impact", 15))
        self.questionType.setStyleSheet("color: #00529b")
        self.questionType.setAlignment(Qt.AlignLeft)
        
        self.questionName = QLabel(' ', self)                     #The Question name is the prompt from the database that asks the user what to answer
        self.questionName.setGeometry(60, 145, 480, 40)
        self.questionName.setFont(QFont("Impact", 10))
        self.questionName.setStyleSheet("color: #be2f37")
        self.questionName.setWordWrap(True)
        self.questionName.setAlignment(Qt.AlignLeft)
        
        
        self.nextButton = QPushButton('Next', self)                           #The next button changes the screen to the next question
        self.nextButton.setGeometry(305, 345, 235, 75)
        self.nextButton.setFont(QFont("Impact", 30))
        self.nextButton.setStyleSheet('QPushButton {background-color: #be2f37; color: white;}')
        self.nextButton.clicked.connect(lambda: self.nextQuestion())          #Links the button to the nextQuestion() function
        
        self.previousButton = QPushButton('Previous', self)                   #The next button changes the screen to the previous question
        self.previousButton.setGeometry(60, 345, 235, 75)
        self.previousButton.setFont(QFont("Impact", 30))
        self.previousButton.setStyleSheet('QPushButton {background-color: #00529b; color: white;}')
        self.previousButton.clicked.connect(lambda: self.previousQuestion())  #Links the button to the previousQuestion() function
        
        self.finishButton = QPushButton('Finish', self)                       #The finish button changes the screen to the grade screen and grades the answers
        self.finishButton.setGeometry(305, 345, 235, 75)
        self.finishButton.setFont(QFont("Impact", 30))
        self.finishButton.setStyleSheet('QPushButton {background-color: #be2f37; color: white;}')
        self.finishButton.clicked.connect(lambda: self.finishQuestion())      #Links the button to the finishQuestion() function
        
        self.exitButton = QPushButton('Exit', self)                           #The exit button changes the screen to the Main Screen and nullifies all answers
        self.exitButton.setGeometry(60, 345, 235, 75)
        self.exitButton.setFont(QFont("Impact", 30))
        self.exitButton.setStyleSheet('QPushButton {background-color: #00529b; color: white;}')
        self.exitButton.clicked.connect(lambda: self.exitQuestion())          #Links the button to the exitQuestion() function
        
        self.q1Answer = [0, 0, 0, 0]            #Initializes the answers for every question to not be answering anything
        self.q2Answer = [0, 0, 0, 0]
        self.q3Answer = [0, 0, 0, 0]
        self.q4Answer = [0, 0, 0, 0]
        self.q5Answer = [0, 0, 0, 0]
        
        #For Multiple Choice Questions
        
        self.radioButton1 = QRadioButton(" ", self)                                             #Initializes all of the radio buttons on Multiple Choice questions
        self.radioButton1.setGeometry(80, 180, 215, 50)
        self.radioButton1.setFont(QFont("Impact", 10))
        self.radioButton1.setStyleSheet("color: #be2f37")
        self.radioButton1.toggled.connect(lambda: self.answerRadioButton(self.radioButton1, 0)) #Connects the radio button to the answerRadioButton() function to record answers
        
        self.radioButton2 = QRadioButton(" ", self)
        self.radioButton2.setGeometry(325, 180, 215, 50)
        self.radioButton2.setFont(QFont("Impact", 10))
        self.radioButton2.setStyleSheet("color: #be2f37")
        self.radioButton2.toggled.connect(lambda: self.answerRadioButton(self.radioButton2, 1)) #Connects the radio button to the answerRadioButton() function to record answers
        
        self.radioButton3 = QRadioButton(" ", self)
        self.radioButton3.setGeometry(80, 260, 215, 50)
        self.radioButton3.setFont(QFont("Impact", 10))
        self.radioButton3.setStyleSheet("color: #be2f37")
        self.radioButton3.toggled.connect(lambda: self.answerRadioButton(self.radioButton3, 2)) #Connects the radio button to the answerRadioButton() function to record answers
        
        self.radioButton4 = QRadioButton(" ", self)
        self.radioButton4.setGeometry(325, 260, 215, 50)
        self.radioButton4.setFont(QFont("Impact", 10))
        self.radioButton4.setStyleSheet("color: #be2f37")
        self.radioButton4.toggled.connect(lambda: self.answerRadioButton(self.radioButton4, 3)) #Connects the radio button to the answerRadioButton() function to record answers
        
        
        #For Multi-Select Questions
        
        self.checkBox1 = QCheckBox(" ", self)                                                   #Initializes all of the check boxes on Multi-Select questions
        self.checkBox1.setGeometry(80, 180, 215, 50)
        self.checkBox1.setFont(QFont("Impact", 10))
        self.checkBox1.setStyleSheet("color: #be2f37")
        self.checkBox1.stateChanged.connect(lambda: self.answerRadioButton(self.checkBox1, 0))  #Connects the check box to the answerRadioButton() (even though it is a checkbox - it just worked out like that ;) ) function to record answers
        
        self.checkBox2 = QCheckBox(" ", self)
        self.checkBox2.setGeometry(325, 180, 215, 50)
        self.checkBox2.setFont(QFont("Impact", 10))
        self.checkBox2.setStyleSheet("color: #be2f37")
        self.checkBox2.stateChanged.connect(lambda: self.answerRadioButton(self.checkBox2, 1))
        
        self.checkBox3 = QCheckBox(" ", self)
        self.checkBox3.setGeometry(80, 260, 215, 50)
        self.checkBox3.setFont(QFont("Impact", 10))
        self.checkBox3.setStyleSheet("color: #be2f37")
        self.checkBox3.stateChanged.connect(lambda: self.answerRadioButton(self.checkBox3, 2))
        
        self.checkBox4 = QCheckBox(" ", self)
        self.checkBox4.setGeometry(325, 260, 215, 50)
        self.checkBox4.setFont(QFont("Impact", 10))
        self.checkBox4.setStyleSheet("color: #be2f37")
        self.checkBox4.stateChanged.connect(lambda: self.answerRadioButton(self.checkBox4, 3))
        
        #For True/False Questions
        
        self.trueButton = QRadioButton("True", self)                                            #Initializes the two radio buttons for true/false questions
        self.trueButton.setGeometry(80, 220, 215, 50)
        self.trueButton.setFont(QFont("Impact", 10))
        self.trueButton.setStyleSheet("color: #be2f37")
        self.trueButton.toggled.connect(lambda: self.answerRadioButton(self.trueButton, 0))
        
        self.falseButton = QRadioButton("False", self)
        self.falseButton.setGeometry(325, 220, 215, 50)
        self.falseButton.setFont(QFont("Impact", 10))
        self.falseButton.setStyleSheet("color: #be2f37")
        self.falseButton.toggled.connect(lambda: self.answerRadioButton(self.falseButton, 1))
        
        #For Matching Questions
        
        self.comboBox1 = QComboBox(self)                                                        #Initializes the combo buttons for matching questions
        self.comboBox1.setGeometry(60, 185, 35, 25)
        self.comboBox1.addItems([" ", "A", "B", "C", "D"])
        self.comboBox1.currentIndexChanged.connect(lambda: self.answerComboBox(self.comboBox1, 0))
        
        self.match1 = QLabel(" ", self)                                                         #Initializes the match for matching questions
        self.match1.setGeometry(100, 180, 200, 35)
        self.match1.setFont(QFont("Impact", 10))
        self.match1.setStyleSheet("color: #00529b")
        self.match1.setWordWrap(True)
        
        self.description1 = QLabel(" ", self)                                                   #Initializes the description for matching questions
        self.description1.setGeometry(310, 180, 230, 35)
        self.description1.setFont(QFont("Impact", 10))
        self.description1.setStyleSheet("color: #00529b")
        self.description1.setWordWrap(True)
        
        self.comboBox2 = QComboBox(self)
        self.comboBox2.setGeometry(60, 225, 35, 25)
        self.comboBox2.addItems([" ", "A", "B", "C", "D"])
        self.comboBox2.currentIndexChanged.connect(lambda: self.answerComboBox(self.comboBox2, 1))
        
        self.match2 = QLabel(" ", self)
        self.match2.setGeometry(100, 220, 200, 35)
        self.match2.setFont(QFont("Impact", 10))
        self.match2.setStyleSheet("color: #be2f37")
        self.match2.setWordWrap(True)
        
        self.description2 = QLabel(" ", self)
        self.description2.setGeometry(310, 220, 230, 35)
        self.description2.setFont(QFont("Impact", 10))
        self.description2.setStyleSheet("color: #be2f37")
        self.description2.setWordWrap(True)
        
        
        self.comboBox3 = QComboBox(self)
        self.comboBox3.setGeometry(60, 265, 35, 25)
        self.comboBox3.addItems([" ", "A", "B", "C", "D"])
        self.comboBox3.currentIndexChanged.connect(lambda: self.answerComboBox(self.comboBox3, 2))
        
        self.match3 = QLabel(" ", self)
        self.match3.setGeometry(100, 260, 200, 35)
        self.match3.setFont(QFont("Impact", 10))
        self.match3.setStyleSheet("color: #00529b")
        self.match3.setWordWrap(True)
        
        self.description3 = QLabel(" ", self)
        self.description3.setGeometry(310, 260, 230, 35)
        self.description3.setFont(QFont("Impact", 10))
        self.description3.setStyleSheet("color: #00529b")
        self.description3.setWordWrap(True)
        
        
        self.comboBox4 = QComboBox(self)
        self.comboBox4.setGeometry(60, 305, 35, 25)
        self.comboBox4.addItems([" ", "A", "B", "C", "D"])
        self.comboBox4.currentIndexChanged.connect(lambda: self.answerComboBox(self.comboBox4, 3))
        
        self.match4 = QLabel(" ", self)
        self.match4.setGeometry(100, 300, 200, 35)
        self.match4.setFont(QFont("Impact", 10))
        self.match4.setStyleSheet("color: #be2f37")
        self.match4.setWordWrap(True)
        
        self.description4 = QLabel(" ", self)
        self.description4.setGeometry(310, 300, 230, 35)
        self.description4.setFont(QFont("Impact", 10))
        self.description4.setStyleSheet("color: #be2f37")
        self.description4.setWordWrap(True)
        
        
        self.q1 = 0                                               #Initializes the question number for each question screen
        self.q2 = 0
        self.q3 = 0
        self.q4 = 0
        self.q5 = 0
        
    def generate5Questions(self):                                 #This function chooses 5 random questions from the database and sets them to the variables
    
        random.seed(time.time())                                  #These here generates 5 random numbers from 1 - 50 that are different from each other
    
        self.q1 = random.randint(1, 50)
        while(self.q1 == self.q2 or self.q1 == self.q3 or self.q1 == self.q4 or self.q1 == self.q5):
            random.seed(time.time())
            self.q1 = random.randint(1, 50)
        
        random.seed(time.time())
        
        self.q2 = random.randint(1, 50)
        while(self.q2 == self.q1 or self.q2 == self.q3 or self.q2 == self.q4 or self.q2 == self.q5):
            random.seed(time.time())
            self.q2 = random.randint(1, 50)
            
        random.seed(time.time())
            
        self.q3 = random.randint(1, 50)
        while(self.q3 == self.q1 or self.q3 == self.q2 or self.q3 == self.q4 or self.q3 == self.q5):
            random.seed(time.time())
            self.q3 = random.randint(1, 50)
            
        random.seed(time.time())
        
        self.q4 = random.randint(1, 50)
        while(self.q4 == self.q1 or self.q4 == self.q2 or self.q4 == self.q3 or self.q4 == self.q5):
            random.seed(time.time())
            self.q4 = random.randint(1, 50)
            
        random.seed(time.time())
       
        self.q5 = random.randint(1, 50)
        while(self.q5 == self.q1 or self.q5 == self.q2 or self.q5 == self.q3 or self.q5 == self.q4):
            random.seed(time.time())
            self.q5 = random.randint(1, 50)
            
            
        self.questionsList = open("fblaQuestions.txt", "r")       #Sets the questionsList to the database
        
        self.totalContent = self.questionsList.readlines()        #Sets totalContent to an array of the lines in the database
        
        self.line1 = self.totalContent[self.q1-1]                 #Sets a specific line for each question that contains the type, the prompt, the options, and the answers
        self.line1 = self.line1.split(";")
        
        self.line2 = self.totalContent[self.q2-1]
        self.line2 = self.line2.split(";")
        
        self.line3 = self.totalContent[self.q3-1]
        self.line3 = self.line3.split(";")
        
        self.line4 = self.totalContent[self.q4-1]
        self.line4 = self.line4.split(";")
        
        self.line5 = self.totalContent[self.q5-1]
        self.line5 = self.line5.split(";")
        
        
        self.questionsList.close()                                #Closes the database
        
    def hideAnswerWidgets(self):                                  #This function simply hides all of the widgets on the question page to reset it
        self.nextButton.hide()
        self.previousButton.hide()
        self.finishButton.hide()
        self.exitButton.hide()
        self.question_header.hide()
        self.questionType.hide()
        self.questionName.hide()
        self.radioButton1.hide()
        self.radioButton2.hide()
        self.radioButton3.hide()
        self.radioButton4.hide()
        self.checkBox1.hide()
        self.checkBox2.hide()
        self.checkBox3.hide()
        self.checkBox4.hide()
        self.trueButton.hide()
        self.falseButton.hide()
        self.comboBox1.hide()
        self.match1.hide()
        self.description1.hide()
        self.comboBox2.hide()
        self.match2.hide()
        self.description2.hide()
        self.comboBox3.hide()
        self.match3.hide()
        self.description3.hide()
        self.comboBox4.hide()
        self.match4.hide()
        self.description4.hide()
        
    @pyqtSlot()
    def startQuiz(self):                                          #This function is connected to the start button and starts a new quiz. Each new quiz is (probably) different than the last
        self.img.hide()                                           #Hides the widgets on the Main Screen
        self.button.hide()
        self.quitButton.hide()
        self.label.hide()
        self.label2.hide()
        
        self.screen = 1                                           #Sets the screen to 1 and the question to 1
        
        self.generate5Questions()                                 #Chooses the questions from the database
        
        self.score = 0                                            #Resets the score for the round to 0
        
        self.q1Answer = [0, 0, 0, 0]                              #Resets the answers for the questions
        self.q2Answer = [0, 0, 0, 0]
        self.q3Answer = [0, 0, 0, 0]
        self.q4Answer = [0, 0, 0, 0]
        self.q5Answer = [0, 0, 0, 0]
        
        self.question()                                           #Starts the first question screen
        
    def quitQuiz(self):                                           #Exits the program when the ecit button is pressed
        sys.exit()
    
    def nextQuestion(self):                                       #Advances to the next question from a previous question
        self.screen += 1                                          #Increases the screen number by 1
        
        self.hideAnswerWidgets()                                  #Hides all the widgets for the question screen to reset it
        
        self.question()                                           #Starts a new question
        
    def previousQuestion(self):                                   #Goes back to the preivous question from the next question
        self.screen -= 1                                          #Decreases the screen number by 1
        
        self.hideAnswerWidgets()                                  #Hides all the widgets for the question screen to reset it
        
        self.question()                                           #Starts a new question

    def finishQuestion(self):                                     #Sets the screen to 6 and moves to the grade screen when the finish button is pressed
        self.screen = 6
       
        self.gradeScreen()
       
    def exitQuestion(self):                                       #Sets the screen to 0 and goes to the Main Screen when the exit button is pressed
        self.screen = 0
       
        self.mainScreen()
        
    def printResults(self):                                       #Downloads the results of the quiz onto a PDF document using the FPDF module
        
        self.fileName = "FBLA_Quiz_" + str(self.score) + "-5.pdf" #Sets the file name according to the final score of the round
        
        self.printFile = FPDF()                                   #Creates a new file to print
        
        self.printFile.add_page()                                 #Adds the one page necessary to print
        self.printFile.set_font("Arial", size = 15)               #Sets the font to Arial and the size to 15
        
        self.printFile.cell(200, 10, txt = "FBLA Quiz Results", ln = 1, align = 'C')   #Sets the title of the document in a new cell aligned in the center
        self.printFile.ln(10)                                                          #Adds a new line in between the title and the next line
        
        self.printFile.multi_cell(200, 10, self.line1[1])                              #Adds a new cell that wraps text for longer items with the question prompt for the question
        self.printFile.multi_cell(200, 10, self.q1Grade.text())                        #Uses the same text on the grade screen in a cell that wraps text
        self.printFile.ln(10)
        
        self.printFile.multi_cell(200, 10, self.line2[1])
        self.printFile.multi_cell(200, 10, self.q2Grade.text())
        self.printFile.ln(10)
        
        self.printFile.multi_cell(200, 10, self.line3[1])
        self.printFile.multi_cell(200, 10, self.q3Grade.text())
        self.printFile.ln(10)
        
        self.printFile.multi_cell(200, 10, self.line4[1])
        self.printFile.multi_cell(200, 10, self.q4Grade.text())
        self.printFile.ln(10)
        
        self.printFile.multi_cell(200, 10, self.line5[1])
        self.printFile.multi_cell(200, 10, self.q5Grade.text())
        
        
        
        self.printFile.output(self.fileName)                                           #Actually downloads the file as a PDF
        
    def answerComboBox(self, box, num):                                                #Activates whenever the index of a combobox is changed
        if(self.screen == 1):                                                          #For each screen and question, it sets the answer to what is selected
            self.q1Answer[num] = box.currentIndex()
        if(self.screen == 2):
            self.q2Answer[num] = box.currentIndex()
        if(self.screen == 3):
            self.q3Answer[num] = box.currentIndex()
        if(self.screen == 4):
            self.q4Answer[num] = box.currentIndex()
        if(self.screen == 5):
            self.q5Answer[num] = box.currentIndex()
        
    def answerRadioButton(self, button, num):                                          #Runs whenever a radio button is toggled. Note: When one is toggled, the others automatically untoggle if they are toggled with PyQt5
        if(self.screen == 1):
            if button.isChecked():                                                     #For each screen/question, it sets the answer to 1 if it is toggled and 0 if it is not
                self.q1Answer[num] = 1
            else:
                self.q1Answer[num] = 0
        if(self.screen == 2):
            if button.isChecked():
                self.q2Answer[num] = 1
            else:
                self.q2Answer[num] = 0
        if(self.screen == 3):
            if button.isChecked():
                self.q3Answer[num] = 1
            else:
                self.q3Answer[num] = 0
        if(self.screen == 4):
            if button.isChecked():
                self.q4Answer[num] = 1
            else:
                self.q4Answer[num] = 0
        if(self.screen == 5):
            if button.isChecked():
                self.q5Answer[num] = 1
            else:
                self.q5Answer[num] = 0
        
            
        
if __name__ == '__main__':                   #This final piece of code actaully starts the whole application and executes it. It also stops the app when the window is closed.
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())