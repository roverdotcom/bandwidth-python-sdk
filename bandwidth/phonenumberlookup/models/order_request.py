# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class OrderRequest(object):

    """Implementation of the 'OrderRequest' model.

    Create TN Lookup Request

    Attributes:
        tns (list of string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "tns": 'tns'
    }

    def __init__(self,
                 tns=None):
        """Constructor for the OrderRequest class"""

        # Initialize members of the class
        self.tns = tns

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        tns = dictionary.get('tns')

        # Return an object of this model
        return cls(tns)
