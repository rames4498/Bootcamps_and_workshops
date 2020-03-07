'''
def count_down(value):
    for x in range(value, 0, -1):
        yield x

c = count_down(5)
print(next(c))
print(next(c))
'''
# iterator_example.py
"""
This should give an iterator with a emoticon.
"""

import random

class CoolEmoticonGenerator(object):
    """docstring for CoolEmoticonGenerator."""

    strings = "!@#$^*_-=+?/,.:;~"
    grouped_strings = [("(", ")"), ("<", ">"), ("[", "]"), ("{", "}")]

    def create_emoticon(self, grp):
        """actual method that creates the emoticon"""
        face_strings_list = [random.choice(self.strings) for _ in range(3)]
        face_strings = "".join(face_strings_list)
        emoticon = (grp[0], face_strings, grp[1])
        emoticon = "".join(emoticon)
        return emoticon

    def __iter__(self):
        """returns the self object to be accessed by the for loop"""
        return self

    def __next__(self):
        """returns the next emoticon indefinitely"""
        grp = random.choice(self.grouped_strings)
        return self.create_emoticon(grp)
