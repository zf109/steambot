"""
    utility functions
"""

def ifnone(none_var, replace_var=''):
    """Simple handler for None values."""
    if none_var:
        return none_var
    return replace_var

def flat_list(ls):
    return [item for sublist in ls for item in sublist]

def ifnokey(dct, key, rep_var=None):
    """If the key of the dict is not found, it returns the rep_var's value."""
    try:
        return dct[key]
    except KeyError:
        return rep_var
