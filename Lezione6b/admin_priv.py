from user import User

"""9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. In a separate file, create an Admin instance and call
show_privileges() to show that everything is still working correctly.
""" 

class Admin(User):
    def __init__(self, first_name: str,
                  last_name: str,
                    email: str,
                      password: int,
                        num_phone: int,
                          login_attempts: int,
                          privileges :list[str] = []) -> None:
        super().__init__(first_name, last_name, email, password, num_phone, login_attempts)
        
        self.privileges = Privileges(privileges=privileges)

class Privileges:
    def __init__(self,
                 privileges : list[str]) -> None:
        self.privileges = privileges
        
    def show_privileges(self):
        admin = Admin()
        print(f'\nThe admin {admin.first_name} can:')
        for prev in self.privileges:
            print(prev)