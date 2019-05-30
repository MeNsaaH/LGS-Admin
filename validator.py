import re

class Validator():
    """Class for Validating User inputs"""
    
    def validateUser(self, user):
        if self.validateUsername(user['username'])[0] is False:
            return False, self.validateUsername(user['username'])[1]
        
        #validate email data and save to user dictionary
        if self.validateEmail(user['email'])[0] is False:
            return False, self.validateEmail(user['email'])[1]
        
        #validate Password Entry
        if self.validatePassword(user["password"], user["confirmP"])[0] is False:
            return False, self.validatePassword(user['password'], user['confirmP'])[1]
        
        return True, None

    def  validateInput(self, input):
        #create an advance input validator
        input = input.strip()
        if len(input) < 1:
            return False, "username/email cannot be empty"
        inputRegex = re.compile(r'[!#$%&*()," {}+=/<>]')
        mo = inputRegex.search(input)
        if mo is None:
            return True, input
        return False, "username/email should not contain special characters like !@#$&*()+={[]}:;?/><"

        
    def validateUsername(self, username):
        username = username.strip()
        if len(username) < 1:
            return False, "Input Error: Username cannot be empty"
        if " " in username:
            return False, "Input Error: Username must not contain Spaces"
        
        nameRegex = re.compile(r'[!@#$%&*()"{}+=/<>]')
        mo = nameRegex.search(username)
        if mo is None:
            return True, username
        return False, "Input Error: username should not contain special characters like !@#$&*()+={[]}:;?/><"
        

    def validateEmail(self, email):
        email = email.strip()
        if len(email)<1:
            return False, "Input Error: Email address cannot be empty"
        emailRegex = re.compile(r'\w+@st\.futminna\.edu\.ng', re.IGNORECASE)
        mo = emailRegex.findall(email)
        if (mo is not None) and len(mo) > 0:
            return True, email
        else:
            return False, "Invalid Email Address: email must conform to the format email@st.futminna.edu.ng"
        

    def validatePassword(self, password, confirm_p):
        if len(password)<8:
            return False, "Input Error:Password must be more than 8 characters"
        if password != confirm_p:
            return False, "Input Error:Passwords must be the same"
        return True, password
        
