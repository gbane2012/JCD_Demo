import connexion
from swaggerserver.models.body_3 import Body3
from swaggerserver.models.body_4 import Body4
from swaggerserver.models.body_5 import Body5
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def create_user(body):
    """
    Create user
    This can only be done by the logged in user.
    :param body: Created user object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body3.from_dict(connexion.request.get_json())
    return 'do some magic!'


def create_users_with_array_input(body):
    """
    Creates list of users with given input array
    
    :param body: List of user object
    :type body: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [Body4.from_dict(d) for d in connexion.request.get_json()]
    return 'do some magic!'


def create_users_with_list_input(body):
    """
    Creates list of users with given input array
    
    :param body: List of user object
    :type body: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [Body4.from_dict(d) for d in connexion.request.get_json()]
    return 'do some magic!'


def delete_user(username):
    """
    Delete user
    This can only be done by the logged in user.
    :param username: The name that needs to be deleted
    :type username: str

    :rtype: None
    """
    return 'do some magic!'


def get_user_by_name(username):
    """
    Get user by user name
    
    :param username: The name that needs to be fetched. Use user1 for testing. 
    :type username: str

    :rtype: Body4
    """
    return 'do some magic!'


def login_user(username, password):
    """
    Logs user into the system
    
    :param username: The user name for login
    :type username: str
    :param password: The password for login in clear text
    :type password: str

    :rtype: str
    """
    return 'do some magic!'


def logout_user():
    """
    Logs out current logged in user session
    

    :rtype: None
    """
    return 'do some magic!'


def update_user(username, body):
    """
    Updated user
    This can only be done by the logged in user.
    :param username: name that need to be updated
    :type username: str
    :param body: Updated user object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body5.from_dict(connexion.request.get_json())
    return 'do some magic!'
