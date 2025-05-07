
from models.constants.action_qualities import GOOD, PERFECT, POOR, OK, ERROR
from models.quality import Quality

def find_perfect_quality(qualities: list[Quality]) -> Quality | None:
    """
    Find the perfect quality from the list of qualities.
    Returns the quality if found, otherwise returns None.
    """
    return _find_quality(qualities, PERFECT)

def find_good_quality(qualities: list[Quality]) -> Quality | None:
    """
    Find the good quality from the list of qualities.
    Returns the quality if found, otherwise returns None.
    """
    return _find_quality(qualities, GOOD)

def find_ok_quality(qualities: list[Quality]) -> Quality | None:
    """
    Find the OK quality from the list of qualities.
    Returns the quality if found, otherwise returns None.
    """
    return _find_quality(qualities, OK)

def find_poor_quality(qualities: list[Quality]) -> Quality | None:
    """
    Find the poor quality from the list of qualities.
    Returns the quality if found, otherwise returns None.
    """
    return _find_quality(qualities, POOR)

def find_error_quality(qualities: list[Quality]) -> Quality | None:
    """
    Find the error quality from the list of qualities.
    Returns the quality if found, otherwise returns None.
    """
    return _find_quality(qualities, ERROR)

def _find_quality(qualities: list[Quality], specific_name: str) -> Quality | None:
    """
    Find a quality from the list of qualities by the <specific_name>.
    Returns the quality if found, otherwise returns None.
    """
    return next((quality for quality in qualities if quality.name == specific_name), None)