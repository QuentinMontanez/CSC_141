import Admin as ad
print(ad)

class User:
    """A class representing a admin user with perivileges"""
    def __init__(Admin, User, permission):
        """Initialize the restaurant"""
        Admin.User=  User.name()
        Admin.permission = permission
    def describe_privileges(Admin):
        """Display a summary of the Admin User"""
        msg = f"{Admin.User} has the power to {Admin.permission}"
        print(f"\n{msg}")
    def open_privileges(Admin):
        """Display a message that tells what the admin is allowed to do"""
        msg= f"{Admin.User} has permission to invite anyone they like"
        print(f"\n{msg}")
Admin= Admin=('Vanessa', 'Lucas')
print(User)
print(Admin)
show_privileges= "Inviting and Kicking People"
print(show_privileges)



