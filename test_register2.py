import random, hashlib
from collections import namedtuple

db = {}

User = namedtuple('User', ['user_name', 'password_enc', 'salt'])


def register(user_name, password):
    if (user_name and password) and not db.has_key(user_name):
        salt = generate_salt()
        user = User(user_name, encript_password(password, salt), salt)
        db.update({user_name: user})
        print user, 'register successfull.'
        return True
    return False


def login(user_name, password):
    if (user_name and password) and db.has_key(user_name):
        user = db.get(user_name)
        if user.password_enc == encript_password(password, user.salt):
            print user, 'login successful.'
            return True
    return False


def generate_salt():
    base_salt = 520292
    print db.get('latest_salt')
    latest_salt = max(db.get('latest_salt'), base_salt)
    next_salt = latest_salt + random.randint(1, 100)
    db.update({'latest_salt': next_salt})
    return next_salt


def get_md5(s):
    md5 = hashlib.md5()
    md5.update(s)
    return md5.hexdigest()


def encript_password(password, salt):
    return get_md5(get_md5(password) + str(salt))


register('fox', '111111') and login('fox', '111111')
register('tom', '111111') and login('tom', '111111')