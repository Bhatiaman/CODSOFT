from tkinter import *
import math

answer = ""
answerforroot = ""
root = Tk()
root.title('Calculator App')
answerEntryLabel = StringVar()
Label(root, font=('futura', 25, 'bold'),
textvariable = answerEntryLabel,
justify = LEFT, height=2, width=7).grid(columnspan=4, ipadx=120)
answerFinalLabel = StringVar()
Label(root, font=('futura', 25, 'bold'),
textvariable = answerFinalLabel,
justify = LEFT, height=2, width=7).grid(columnspan = 4 , ipadx=120)

def changeAnswerEntryLabel(entry):
    global answer
    global answerforroot
    answer = answer + str(entry)
    answerforroot = answer
    answerEntryLabel.set(answer)

def clearAnswerEntryLabel():
    global answer
    global answerforroot
    answerforroot = answer
    answer = ""
    answerEntryLabel.set(answer)

def evaluateSquareRoot():
    global answer
    global answerforroot
    try:
        sqrtAnswer = math.sqrt(eval(str(answerforroot)))
        clearAnswerEntryLabel()
        answerFinalLabel.set(sqrtAnswer)
    except(ValueError,SyntaxError,TypeError, ZeroDivisionError):
        try:
            sqrtAnswer = math.sqrt(eval(str(answer)))
            clearAnswerEntryLabel()
            answerFinalLabel.set(sqrtAnswer)
        except(ValueError,SyntaxError,TypeError,ZeroDivisionError):
            clearAnswerEntryLabel()
            answerFinalLabel.set("Error!")

def evaluateAnswer():
    global answer
    try:
       eval(answer)
       evaluatedValueAnswerLabelGlobal= str(eval(answer))                    
       clearAnswerEntryLabel()
       answerFinalLabel.set(evaluatedValueAnswerLabelGlobal)

    except(ValueError,SyntaxError,TypeError, ZeroDivisionError):
        clearAnswerEntryLabel()
        answerFinalLabel.set("Error!")

def allClear():
    global answer
    global answerforroot
    answer = ""
    answerforroot = ""
    answerEntryLabel.set("")
    answerFinalLabel.set("")

def createButton(txt,x,y):
    Button(root, font=('futura', 15, 'bold'),
           padx=16,pady=16,text = str(txt),
           command = lambda:changeAnswerEntryLabel(txt),
           height = 2, width=9).grid(row = x , column = y, sticky=E)

buttons = ['AC','√','%','/','7','8','9','*','4','5','6','-','1','2','3','+','','','.','']
buttonsListTraversalCounter = 0

for i in range(3,8):
    for j in range(0,4):
        createButton(buttons[buttonsListTraversalCounter],i,j)
        buttonsListTraversalCounter =buttonsListTraversalCounter + 1

Button(root,font=('futura', 15, 'bold'),
       padx=16,pady=16, text = "√",
       command = lambda:evaluateSquareRoot(),
       height=2, width=9).grid(row = 3 , column = 1, sticky = E)

Button(root,font=('futura', 15, 'bold'),
       padx=16,pady=16, text = "AC",
       command = lambda:allClear(),
       height=2, width=9).grid(row = 3 , column = 0 , sticky = E)

Button(root,font=('futura', 15, 'bold'),
       padx=16,pady=16, text = "0",
       command = lambda:changeAnswerEntryLabel(0),
       height=2, width=21).grid(row = 7 , column = 0 ,
       columnspan=2 , sticky = E)

Button(root,font=('futura', 15, 'bold'),
       padx=16,pady=16, text = "=",
       command = lambda:evaluateAnswer(),
       height=2, width=9).grid(row = 7 , column = 3, sticky = E)

root.mainloop()