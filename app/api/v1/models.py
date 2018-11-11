"""User Model"""
users = [
    {
    "user_id":"20",
    "firstname":"mary",
    "lastname":"muthoni",
    "username":"kajojo",
    "email":"jojo@yandex.com",
    "password":"joan"

}, {
    "user_id":"21",
    "firstname":"eunice",
    "lastname":"wanjiru",
    "username":"kapienga",
    "email":"shix@gmail.com",
    "password":"shiro"
}
]

class UserModel:
    """Class user model"""
    def __init__(self):
        """Initialize the user model class"""
        self.db = users

    def add_users(self, firstname, lastname, username, email, password):
        """Adding new users"""
        payload = {
            'user_id' : len(users) + 1,
            'firstname': firstname, 
            'lastname' : lastname,
            'username' : username,
            'email' : email,
            'password' : password      
        }
        usr = self.db.append(payload)
        return usr

    def get_all_users(self):
        """Returning all users"""
        return self.db

    def get_one_user(self, user_id):
        """Returning a specific user"""
        user = [user for user in self.db if user['user_id'] == str(user_id)]
        return user[0]
