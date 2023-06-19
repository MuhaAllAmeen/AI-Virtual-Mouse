import tkinter as tk
from tkinter import ttk
from tkinter import font
import sv_ttk




class gui:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x650")
        self.root.title("Virtual Mouse Config")
        self.root.config(background='white')
        s=ttk.Style()

        self.websiteFrame= tk.Frame(self.root)
        self.websiteFrame.config(background='white')
        self.websiteFrame.columnconfigure(0,weight=1)
        self.websiteFrame.columnconfigure(1,weight=1)
        self.websiteFrame.columnconfigure(2,weight=1)


        websiteFont= font.Font(family='Calibri',size=16)
        self.websiteLabel = tk.Label(self.websiteFrame,text="Website: ", font=websiteFont,background='white')

        self.webIn = tk.StringVar()

        self.websiteInput= ttk.Entry(self.websiteFrame, textvariable=self.webIn, width=30)
        self.websiteInput.configure(background='black')

        self.websiteSubmit=tk.Button(self.websiteFrame, text="Submit", height=1, width=10, command= lambda: self.returnWebsite())

        self.websiteLabel.grid(row=0,column=0)
        self.websiteInput.grid(row=0,column=1)
        self.websiteSubmit.grid(row=0,column=2)


        self.websiteFrame.pack(pady=40,fill='x')
        s.configure('credentialFrame', backgroud='white')
        self.credentialFrame = tk.Frame(master=self.root)
        self.credentialFrame.configure(background='white')

        self.BBLabel2 = ttk.Label(master=self.credentialFrame, text="For BB purpose only", font=websiteFont, background='white')
        self.usernameLabel = ttk.Label(master=self.credentialFrame, text='Username: ',background='white')
        self.usernameVar = tk.StringVar()
        self.usernameInput = ttk.Entry(master=self.credentialFrame, textvariable=self.usernameVar, width=30)
      

        self.passwordLabel = ttk.Label(master=self.credentialFrame, text="Password: ",background='white')
        self.passwordVar = tk.StringVar()
        self.passwordInput=ttk.Entry(master=self.credentialFrame,textvariable=self.passwordVar, width=30, show="*")
        

        self.credentialClear = ttk.Button(master=self.credentialFrame, text="Clear", command= lambda : [self.usernameInput.delete(0,tk.END),self.passwordInput.delete(0,tk.END)])


        self.credentialFrame.columnconfigure(0, weight=1)
        self.credentialFrame.columnconfigure(1, weight=1)

        self.BBLabel2.grid(row=0,column=0,padx=10)
        self.usernameLabel.grid(row=1,column=0,padx=10)
        self.usernameInput.grid(row=1,column=1,padx=10)
        self.passwordLabel.grid(row=2,column=0,padx=10,pady=10)
        self.passwordInput.grid(row=2,column=1,padx=10,pady=10)
        self.credentialClear.grid(row=3,column=1,padx=0,pady=10)


        self.credentialFrame.pack()

        self.BBFrame = tk.Frame(master=self.root)
        self.BBFrame.configure(background='white')

        self.BBLabel= ttk.Label(master=self.BBFrame, text='Select the window you would like to open on BB',background='white')

        self.choiceVar = tk.StringVar()
        self.homeCheck = ttk.Radiobutton(master=self.BBFrame,text="Home", value='Home', variable=self.choiceVar,command=self.submitCredentials())
        self.profileCheck = ttk.Radiobutton(master=self.BBFrame,text="Profile", value='Profile', variable=self.choiceVar,command=self.submitCredentials())
        self.activityCheck = ttk.Radiobutton(master=self.BBFrame,text="Activity Stream", value='Activity', variable=self.choiceVar,command=self.submitCredentials())
        self.modulesCheck = ttk.Radiobutton(master=self.BBFrame,text="Modules", value='Modules', variable=self.choiceVar,command=self.submitCredentials())
        self.communitiesCheck = ttk.Radiobutton(master=self.BBFrame,text="Communities", value='Communities', variable=self.choiceVar,command=self.submitCredentials())
        self.calendarCheck = ttk.Radiobutton(master=self.BBFrame,text="Calendar", value='Calendar', variable=self.choiceVar,command=self.submitCredentials())
        self.messageCheck = ttk.Radiobutton(master=self.BBFrame,text="Messages", value='Messages', variable=self.choiceVar,command=self.submitCredentials())
        self.marksCheck = ttk.Radiobutton(master=self.BBFrame,text="Marks", value='Marks', variable=self.choiceVar,command=self.submitCredentials())
        self.toolsCheck = ttk.Radiobutton(master=self.BBFrame,text="Tools", value='Tools', variable=self.choiceVar,command=self.submitCredentials())

        self.credentialSubmit = ttk.Button(master=self.BBFrame, text='Submit', command= lambda : self.submitCredentials())


        self.BBFrame.pack(pady=20)
        self.BBLabel.pack(pady=10)
        self.homeCheck.pack()
        self.profileCheck.pack()
        self.activityCheck.pack()
        self.modulesCheck.pack()
        self.communitiesCheck.pack()
        self.calendarCheck.pack()
        self.messageCheck.pack()
        self.marksCheck.pack()
        self.toolsCheck.pack()
        self.credentialSubmit.pack(pady=20)

        # sv_ttk.set_theme('dark')
        self.root.mainloop()

    def returnWebsite(self):
        return self.webIn.get()

    def submitCredentials(self):
        return self.usernameVar.get(),self.passwordVar.get(),self.choiceVar.get()

# g=gui()
# print(g.submitCredentials())



