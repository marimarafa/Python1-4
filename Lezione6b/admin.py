"""9-11. Imported Admin: Start with your work from Exercise 9-8. Store the classes User, Privileges, and Admin in one module. Create a separate file, make an Admin instance, 
and call show_privileges() to show that everything is working correctly.
"""



from admin_priv import Admin


admin :Admin = Admin(first_name= "sofia",last_name="Bob",email="sofiabob23@gmail.com",password=767934,num_phone=33256788,login_attempts=5,privileges=["delete post","ban user","add post"])
admin.privileges.show_privileges()
print("\n")