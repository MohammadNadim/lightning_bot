from tkinter import *
import model


# generate a response
def lightning_response(message):
    response, tag = model.chatbot_response(message)
    #response = 'go home'
    return response, tag

# get text from user and reply a response
def user_input():
    message = inputText.get('1.0','end-1c')
    inputText.delete('0.0',END)

    if message!='':
        logFile.config(state=NORMAL)
        logFile.insert(END, 'You: ' + message + '\n')
        response, tag = lightning_response(message)
        logFile.insert(END, 'Lightning_tag: ' + tag + '\n')
        logFile.insert(END, 'Lightning_response: ' + response + '\n')
        logFile.config(state=DISABLED)


# create a background
background = Tk()
background.title('Lightning')
background.geometry('500x500')

# create a chat window
logFile = Text(background, bg='#d5dfed')
logFile.config(state=DISABLED)

# create a input text field
inputText = Text(background, height=10, width=10, bg='#bcc0c4')

# create a send button
sendButton = Button(background, text='Send', height=5, width=5, command = user_input)

# put everything in the background
logFile.place(x=6, height = 450, width = 490)
inputText.place(x=6, y=450, height = 50, width = 450)
sendButton.place(x=450, y=450, height = 50, width = 50)
background.mainloop()