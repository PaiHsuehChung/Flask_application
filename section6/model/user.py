from db import db
class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        """Find user by username

        :param username: the username
        :type username: str
        :return: if username is exists or not
        :rtype: User(id, username, password) or None
        """
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_userid(cls, _id):
        """Find user by id

        :param _id: The user id
        :type _id: int
        :return: if user is exists or not
        :rtype: User(id, username, password) or None
        """
        return cls.query.filter_by(id=_id).first()
