# -*- coding: utf8 -*-

# Copyright (C) 2016 Stanisław Szcześniak

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


class Base(object):
    """base class for all other bookbrainz db classes

    Role of fetch_from_json is to parse data from JSON to the object on
    which it is called. If data is None or empty then default constructor
    without any parameters is called. If it is not, then fetch_from_json_filled
    is called, which assumes that its data is not empty.

    This class has no attributes and args in constructor.
    """

    def __init__(self):
        for attr in self.get_attributes():
            setattr(self, attr.attr_name, None)

    @classmethod
    def from_json(cls, json_data):
        """ Returns object of called class with parsed json_data

        :param json_data: JSON formatted data
        :return: instance of cls
        """
        instance = cls()

        if json_data is not None:
            for attr in instance.get_attributes():
                attr.set_from_json(instance, json_data)

        return instance

    def get_attributes(self):
        cls = self.__class__
        candidates = [getattr(cls, attr) for attr in dir(cls)]
        return [value for value in candidates if
                getattr(value, '__class__', None) is Attribute]


class Attribute(object):
    """Attribute class
    """
    def __init__(self, name, ws_name='', parse=None, cls=None):
        self.attr_name = name
        self.ws_name = ws_name if ws_name else name
        self.parse = parse
        self.cls = cls

    def set_from_json(self, instance, json_data):
        value = Attribute.get_value_by_ws_name(json_data, self.ws_name)

        if value and self.parse:
            value = self.parse(value)

        if value and self.cls:
            value = self.cls.from_json(value)

        setattr(instance, self.attr_name, value)

    @staticmethod
    def get_value_by_ws_name(json_data, ws_name):
        if type(ws_name) is tuple:
            value = json_data
            for name in ws_name:
                value = value[name]
        else:
            value = json_data.get(ws_name)

        return value
