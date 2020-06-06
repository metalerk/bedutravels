def list2str(l):
    """Unwraps strings from a list"""

    if isinstance(l, list):
        return l.pop()
    return l