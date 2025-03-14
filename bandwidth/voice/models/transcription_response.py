# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from bandwidth.voice.models.transcript import Transcript


class TranscriptionResponse(object):

    """Implementation of the 'TranscriptionResponse' model.

    TODO: type model description here.

    Attributes:
        transcripts (list of Transcript): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "transcripts": 'transcripts'
    }

    def __init__(self,
                 transcripts=None):
        """Constructor for the TranscriptionResponse class"""

        # Initialize members of the class
        self.transcripts = transcripts

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
        transcripts = None
        if dictionary.get('transcripts') is not None:
            transcripts = [Transcript.from_dictionary(x) for x in dictionary.get('transcripts')]

        # Return an object of this model
        return cls(transcripts)
