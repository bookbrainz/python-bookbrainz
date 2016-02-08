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
        pass

    def fetch_from_json(self, json_data):
        """ Parses json_data to called object

        :param json_data: JSON formatted data
        :return: None
        """
        if not json_data:
            self.__init__()
        else:
            self.fetch_from_json_filled(json_data)

    def fetch_from_json_filled(self, json_data):
        """ Parses json_data to called object assuming that
        json_data is not empty

        Should ve overridden in called object's class

        :param json_data: JSON formatted data
        :return: None
        """
        raise NotImplementedError

    @classmethod
    def from_json(cls, json_data):
        """ Returns object of called class with parsed json_data

        :param json_data: JSON formatted data
        :return: instance of cls
        """
        instance = cls()
        instance.fetch_from_json(json_data)
        return instance

    def to_json(self):
        if self:
            return self.to_json_filled()
        else:
            return None

    def to_json_filled(self):
        raise NotImplementedError