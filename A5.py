'''
1. Technical queries
2. Billing issues
3. Plan informations
'''


class chatbot:
    dict = {1:"Basic",2:"Premium",3:"Basic",4:"Premium"}

    def __init__(self) -> None:
        # self.interact()
        print()

    def interact(self):
        print("Welcome to the chatbot service")
        print()
        print("What help do you want ?\n")
        print("1. Technical queries")
        print("2. Billing issues")
        print("3. Plan informations\n")
        while(True):
            c = int(input())
            if c==1:
                self.technical()
                break
            elif c==2:
                self.billing()
                break
            elif c==3:
                self.plan()
                break
            else:
                print("Please enter a valid option")
        print("\nThank you! We hope you have a nice day ahead")        

    def technical(self):
        print("\nWhich of the following issues resembles your issue ?\n")
        print("1. Not getting any connection")
        print("2. Internet speed is very slow")
        print("3. Continuous interruptions in the connection")
        while(True):
            c = int(input())
            if c==1:
                print("\nAre any of the following lights completely turned off ?\n")
                print("1. Power 2.Internet 3.Ethernet 4.WLAN 5.None")
                while(True):
                    ch = int(input())
                    if ch==1 or ch==5:
                        print("Please try restarting your modem, if the problem persists,please raise a complaint so that an attendant will be assigned to you")
                        break
                    elif ch==2 or ch==3 or ch==4:
                        print("There seems to be some issue with the wired setup, technical team will reach out to you.")
                        break
                    else:
                        print("Please enter a valid option")
                break
            elif c==2:
                print("\nFor how long this is issue is faced ?\n")
                print("1. Few Hours 2.Few Days")
                while(True):
                    ch = int(input())
                    if ch==1:
                        print("There seems to be some issue with your area for now, please restart your modem once, while we are trying to restore the speed")
                        break
                    elif ch==2:
                        print("There seems to be some issue with the wired setup, technical team will reach out to you.")
                        break
                    else:
                        print("Please enter a valid option")
                break
            elif c==3:
                print("\nHave there been any of the following problems in your area ?\n")
                print("\n1. Continuous power cuts 2.Heavy rains 3.None\n")
                while(True):
                    ch = int(input())
                    if ch==1 or ch==2:
                        print("There seems to be some issue with the wired setup, technical team will reach out to you.")                        
                        break
                    elif ch==3:
                        print("This is mostly a temporary problem, we will try to restore the continuous connection asap.")
                        break
                    else:
                        print("Please enter a valid option")
                break
            else:
                print("Sorry, we could not understand,Please enter a valid option")
        #print("Thank you! We hope you have a nice day ahead")  



    def billing(self):
        print("\nWhich of the following issues resembles your issue ?\n")
        print("1. Recharged for the service, but validity remains the same")
        print("2. Recharged for the service, but did not get receipt")
        print("3. Where Can I recharge online ?\n")
        while(True):
            c = int(input())
            if c==1:
                while(True):
                    print("\nIf you have received a receipt, please provide your receipt number\n")
                    rno = input()
                    print("You have entered : ",rno)
                    pr=input("Proceed ? (y/n)")
                    if pr=="y" or pr=="Y":
                        print("We will check the details and update the validity asap")
                        break
                    elif pr=="n" or pr=="N":
                        continue
                    else:
                        print("Please enter a valid option")
                break
            elif c==2:
                print("\nWe will check your latest recharge entries and send you the receipt on registered email asap\n")
                break
            elif c==3:
                print("\nPlease click on following link :")
                print("www.kljg.in")
                print("Once you land :")
                print("1. Login with your user ID and OTP received")
                print("2. Click on recharge now")
                print("3. Select from the available plans")
                print("4. Make the payment using suitable option")
                break
            else:
                print("Sorry, we could not understand,Please enter a valid option")
        #print("Thank you! We hope you have a nice day ahead")  

    def plan(self):
        print("\nPlans and their details are as follows :\n")
        d = {"Basic": [600, "30GB", '5 MBPS'],
            "Premium": [800, "40GB", '10 MBPS'],
            "Ultra": [1000, "50GB", '15 MBPS'] }
        print("{:<8} {:<20} {:<10} {:<10}".format('Name','Price Per Month','FUP','Speed'))
        for k, v in d.items():
            ppm,fup,speed = v
            print ("{:<8} {:<20} {:<10} {:<10}".format(k, ppm, fup, speed))

        #print("Thank you! We hope you have a nice day ahead")                      

chat = chatbot()
chat.interact()

'''
import nltk
from nltk.chat.util import Chat, reflections

reflections = {
  "I am"       : "you are",
  "I was"      : "you were",
  "I"          : "you",
  "I'm"        : "you're",
  "I'd"        : "you'd",
  "I've"       : "you've",
  "I'll"       : "you'll",
  "My"         : "your",
  "You are"    : "I am",
  "You were"   : "I was",
  "You have"   : "I have",
  "You'll"     : "I will",
  "Your"       : "my",
  "Yours"      : "mine",
  "You"        : "me",
  "Me"         : "you"
}

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today? ",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ], 
    [
        r"what is your name ?",
        ["I am a bot created by Priyanka. You can call me crazy if you want!",]
    ],
    [
        r"how are you ?",
        ["I'm doing good! How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright","It's okay, never mind",]
    ],
    [
        r"I am fine",
        ["Great to hear that! How can I help you?",]
    ],
    [
        r"i'm good",
        ["Nice to hear that","How can I help you? :)",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude! Seriously? You are asking me this?",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse ;)",]
    ],
    [
        r"(.*) created ?",
        ["Priyanka created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Pune, Maharashtra',]
    ],
    [
        r"How is the weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot here in %1 man","Too cold here in %1 man","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is such an amazing company innit? But they are in huge loss these days :(",]
    ],
    [
        r"(.)raining in (.)",
        ["No rain since last week here in %2","Damn it's raining cats and dogs here in %2"]
    ],
    [
        r"how (.) health(.)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a huge fan of football",]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
    ],
    [
        r"i am looking for online guides and courses to learn data science, can you suggest?",
        ["W3 schools has many great articles with step-by-step explanation along with code, you can explore!"]
    ],
    [
        r"quit",
        ["Bye, take care! Work hard! :) ","It was nice talking to you! See you soon :)"]
    ],
]

def chat():
    print("Hi! I am a chatbot created by Priyanka. How can I serve you?")
    chat = Chat(pairs, reflections)
    chat.converse()
#initiate the conversation

if __name__ == "__main__":
    chat()

'''