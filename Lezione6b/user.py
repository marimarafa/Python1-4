class User:
    def __init__(self,
                  first_name :str,
                 last_name :str,
                 email :str,
                 password :int,
                 num_phone : int,
                 login_attempts :int) -> None:
        
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.num_phone = num_phone
        self.login_attempts = login_attempts

    def describe_user(self):
        return f'user name :{self.first_name} {self.last_name}, email :{self.email}, password :{self.password}: phone number :{self.num_phone}'
    def great_user(self):
        return f'Welcome {self.first_name} {self.last_name}! It is great to see you'
    def increment_login_attempts(self):
        while self.login_attempts:
            self.login_attempts += 1
            return f'login attempts :{self.login_attempts}'
    def reset_login_attempts(self):
        while self.login_attempts > 0:
            self.login_attempts -=1
            print(f'you have  {self.login_attempts+1} login attempts left')
            if self.login_attempts == 0:
                return("You have 0 login attempts")   
    