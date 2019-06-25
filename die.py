#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from random import randint

class Die():
    """A class modules a die."""
    def __init__(self, num_sides=6):
        """Initialize attributes to describe a car."""
        self.num_sides = num_sides
        
    def roll(self):
        """To return a random number between 1 and num_sides"""
        return randint(1, self.num_sides)
            

