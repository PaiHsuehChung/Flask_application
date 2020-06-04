from flask_restful import Resource, reqparse
from model.user import UserModel

class UserRegister(Resource):
    """Register account
    :endpoint: /register
    :json data: {"username":<username>, "password":<password>}

    :status code: 
        :The user is exists: 400
        :Create successful: 201
    """

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This can not be blank."
    )

    parser.add_argument('password',
        type=str,
        required=True,
        help="This can not be blank."
    )

    def post(self):
        """
        :endpoint: /register
        :post body: {"username":<username>, "password":<password>}

        :return: Create successful or not.
        :rtype: JSON Message.
        """
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"Message":'The user name has already exists !'}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"Message":"User created successful!"}, 201
