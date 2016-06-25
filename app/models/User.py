from system.core.model import Model
import re

class User(Model):
    def __init__(self):
        super(User, self).__init__()
    
    def get_users(self):
        return self.db.query_db("SELECT * FROM users")

    def get_user_by_email(self, email):
        query = "SELECT * from users where email = :email LIMIT 1"
        data = {'email': email}
        return self.db.get_one(query, data)

    def get_user_by_id(self, user_id):
        query = "SELECT * from users where id = :id LIMIT 1"
        data = {'id': user_id}
        return self.db.get_one(query, data)

    def insert_user(self, new_user):
        user_pwd = self.bcrypt.generate_password_hash(new_user['password'])
        query = "INSERT into users (name, alias, email, password, dob, created_at) values(:name, :alias, :email, :password, :dob, NOW())"
        data = {'name': new_user['name'], 'alias': new_user['alias'], 'email': new_user['email'], 'password': user_pwd, 'dob': new_user['dob'], }
        return self.db.query_db(query, data)

    def user_validation(self, new_user):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []

        if not new_user['name'] or not new_user['alias'] or not new_user['email'] or not new_user['password'] or not new_user['pwd_conf'] or not new_user['dob']:
            errors.append('All fields are mandatory!')
        if len (new_user['name']) < 2:
            errors.append('Name must have at least 2 characters')
        if len (new_user['alias']) < 2:
            errors.append('Alias must have at least 2 characters')
        if not new_user['dob']:
            errors.append('Date of Birth is mandatory!')
        if not EMAIL_REGEX.match (new_user['email']):
            errors.append('Invalid e-mail!')
        if len (new_user['password']) < 8:
            errors.append('Password must have at least 8 characters!')
        if new_user['password'] != new_user['pwd_conf']:
            errors.append('Passwords are not a match!')
        if self.get_user_by_email (new_user['email']):
            errors.append('E-mail already exists!')

        if errors:
            return {"status": False, "errors": errors}
        else:
            return { "status": True}

    def pwd_validation(self, password, pwd_validate):
        return self.bcrypt.check_password_hash(password, pwd_validate)