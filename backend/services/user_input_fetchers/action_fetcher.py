from models.action import Action
from models.constants.action_types import SERVE, SERVE_RECEIVE_PASS, FREE_BALL, DIG, SET, ATTACK, BLOCK

def find_serve_action(actions: list[Action]):
    """
    Find the serve action from the list of actions.
    Returns the action if found, otherwise returns None.
    """
    return _find_action(actions, SERVE)

def find_serve_receive_pass_action(actions: list[Action]):
    """
    Find the serve receive action from the list of actions.
    Returns the action if found, otherwise returns None.
    """
    return _find_action(actions, SERVE_RECEIVE_PASS)

def find_free_ball_action(actions: list[Action]):
    """
    Find the free ball action from the list of actions.
    Returns the action if found, otherwise returns None.
    """
    return _find_action(actions, FREE_BALL)

def find_dig_action(actions: list[Action]):
    """
    Find the dig action from the list of actions.
    Returns the action if found, otherwise returns None.
    """
    return _find_action(actions, DIG)

def find_set_action(actions: list[Action]):
    """
    Find the set action from the list of actions.
    Returns the action if found, otherwise returns None.
    """
    return _find_action(actions, SET)

def find_attack_action(actions: list[Action]):
    """
    Find the attack action from the list of actions.
    Returns the action if found, otherwise returns None.
    """
    return _find_action(actions, ATTACK)

def find_block_action(actions: list[Action]):
    """
    Find the block action from the list of actions.
    Returns the action if found, otherwise returns None.
    """
    return _find_action(actions, BLOCK)

def _find_action(actions: list[Action], specific_name: str):
    """
    Find an action from the list of actions by the <specific_name>.
    Returns the action if found, otherwise returns None.
    """
    return next((action for action in actions if action.name == specific_name), None)