
import re
import random
class supportBot:
    
    negative_res = ("no","nope","nah","naw","not a chance","sorry")
    exit_commands = ("quit","pause","exit","goodbye","bye","later")
    
    
   
    def __init__(self):
        self.support_responses = {
            'ask_about_product': r'.*\s*product.*',
            'technical_support': r'.*technical.*support.*',
            'about_return_policy': r'.*\s*return_policy.*',
            'general_query': r'.*how.*help.*',            
        }
    
    def greet(self):
        self.name = input("hi welcome to our customer support.what is your name ?\n")
        will_help = input(f"Hi {self.name}, I am bot.how can i assist you today?\n")
        if will_help in self.negative_res:
            print("alright have a great day!")
            return 
        self.chat()
        
    def make_exit(self, reply):
        for command in self.exit_commands:
            if reply == command:
                print("Thanks for reaching out.Have a nice day")
                return True
            return False

    def chat(self):
        reply = input("please tell me your query\n").lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))
            
    
    def match_reply(self, reply):
        for intent, regex_pattern in self.support_responses.items():
            found_match = re.match(regex_pattern, reply)
            if found_match and intent == 'ask_about_product':
                return self.ask_about_product()
            elif found_match and intent == 'technical_support':
                return self.technical_support()
            elif found_match and intent == 'about_return_policy':
                return self.about_return_policy()
            elif found_match and intent == 'general_query':
                return self.general_query() 
        return self.no_match_intent() 
    def ask_about_product(self):
        responses = ("our product is a top notch one\n",
                    "you can find more details about the product on our websites \n")
        return random.choice(responses)
    
    def technical_support(self):
        responses = ("please visit our technical support helpline for more infos\n",
                      "you can also call our tech helpline number for more infos\n")
        return random.choice(responses)
    
    def about_return_policy(self):
        responses = ("check if it the product is in original condition...then agree with the returning process\n",
                      "we have a 30 days return policy for every product\n")
        return random.choice(responses)
    
    def general_query(self):
        responses = ("how can i assist you furthur\n", "is there is anything that you would like to ask\n")
        return random.choice(responses)
    

    def no_match_intent(self):
        responses = ( "iam sorry i didnt understand\n","can you repeat the phrase?\n",
                        "please provide more information\n")
        return random.choice(responses)
bot = supportBot()
bot.greet()