# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class User(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, model=None):  # noqa: E501
        """User - a model defined in Swagger

        :param model: The model of this User.  # noqa: E501
        :type model: str
        """
        self.swagger_types = {
            'model': str
        }

        self.attribute_map = {
            'model': 'model'
        }

        self._model = model

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The User of this User.  # noqa: E501
        :rtype: User
        """
        return util.deserialize_model(dikt, cls)

    @property
    def model(self):
        """Gets the model of this User.


        :return: The model of this User.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this User.


        :param model: The model of this User.
        :type model: str
        """
        if model is None:
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501

        self._model = model
