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
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def fetch_from_json(self, json_data):
        if not json_data:
            self.__init__()
        else:
            self.fetch_from_json_filled(json_data)

    def fetch_from_json_filled(self, json_data):
        raise NotImplementedError

    @classmethod
    def from_json(cls, json_data):
        instance = cls()
        instance.fetch_from_json(json_data)
        return instance
