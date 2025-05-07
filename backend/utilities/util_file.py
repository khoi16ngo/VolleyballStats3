import mimetypes
import os
from services.stat_collectors.assist_stat_collector import get_assist_stats_headers
from services.stat_collectors.attack_stat_collector import get_attack_stats_headers
from services.stat_collectors.block_stat_collector import get_block_stats_headers
from services.stat_collectors.dig_stat_collector import get_dig_stats_headers
from services.stat_collectors.free_ball_stat_collector import get_free_ball_stats_headers
from services.stat_collectors.serve_receive_stat_collector import get_serve_receive_stats_headers
from services.stat_collectors.serve_stat_collector import get_serve_stats_headers

def get_file_extension(file_name: str) -> str:
    '''
    Returns the file extension of the file name.
    For example, if the file name is "file.txt", the function will return "txt".
    '''
    mime_type, _ = mimetypes.guess_type(file_name)
    return mime_type

def remove_file_extension(file_name: str) -> str:
    '''
    Removes the file extension from the file name.
    For example, if the file name is "file.txt", the function will return "file".'''
    base, _ = os.path.splitext(file_name)
    return base

def get_file_name_from_file_path(file_path: str) -> str:
    '''
    Returns the file name from the file path.
    For example, if the file path is "/home/user/file.txt", the function will return "file.txt".
    '''
    # Normalize the file path to handle both \\ and /
    normalized_path = os.path.normpath(file_path)

    # Split the normalized path into components
    file_path_list = normalized_path.split(os.path.sep)

    # Get the last 'number_path' components
    return file_path_list[-1]

def get_file_headers() -> list:
    '''
    Headers will outline all types of actions and action stats for each player.
    Returns a list of headers for the players stats file.
    '''
    headers = ['Player Name']
    headers += get_attack_stats_headers()
    headers += get_block_stats_headers()
    headers += get_assist_stats_headers()
    headers += get_free_ball_stats_headers()
    headers += get_dig_stats_headers()
    headers += get_serve_receive_stats_headers()
    headers += get_serve_stats_headers()
    return headers

def file_exists(file_path: str) -> bool:
    """
    Checks if a file exists at the given file path.
    Returns True if the file exists, otherwise False.
    """
    return os.path.exists(file_path)