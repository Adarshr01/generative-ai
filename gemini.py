import api_key as api
import google.generativeai as gai

class talk():
    def __init__(self):
        gai.configure(api_key=api.API_KEY)
        
    def contalk(self):
        self.user_messages=input("How may i help you !\n(Press '0' to Exit )>> ")
        while(self.user_messages!="0"): 
            try:           
                model=gai.GenerativeModel("gemini-1.5-flash")
                response=model.generate_content(self.user_messages)
                print(response.text) 
                self.user_messages=input(">>")
                
                
            except:
                self.user_messages=0
                 
                
                
                
adarsh=talk()
adarsh.contalk()

