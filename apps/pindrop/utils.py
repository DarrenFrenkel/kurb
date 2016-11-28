import re


class ChoicesList(object):
    """
    Helpful container for bi-directional access of "constants"
    Arguments are two-tuples of (value, label)
    >>> choices = ChoicesList((0, 'First'), (1, 'Second'), (5, 'Code Five'))
    >>> choices.SECOND
    1
    >>> choices.CODE_FIVE
    5
    >>> choices[5]
    'Code Five'
    >>> list(choices)
    [(0, 'First'), (1, 'Second'), (5, 'Code Five')]
    """
    def __init__(self, *items):
        # Make two-tuples if we're not given them
        if not isinstance(items[0], (list, tuple,)):
            items = tuple((x, x) for x in items)
        self.items = items
        self.ref = dict(items)
        for val, label in items:
            setattr(self, re.sub('\W', '_', label.upper()), val)

    def __iter__(self):
        return self.items.__iter__()

    def __getitem__(self, key):
        return self.ref[key]
