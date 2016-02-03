# -*- coding: utf8 -*-

# Copyright (C) 2014-2016 Ben Ockmore, Stanisław Szcześniak

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

from entity import Entity, format_date


class Edition(Entity):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.edition_type = None

        self.release_date = None
        self.release_date_precision = None

        self.pages = None

        # Dimensions, stored as integer millimetre values
        self.width = None
        self.height = None
        self.depth = None

        # Weight in grams
        self.weight = None

        self.creator_credit = None
        self.language = None
        self.edition_format = None
        self.edition_status = None
        self.publisher = None
        self.publication = None

    def release(self):
        return format_date(self.release_date, self.release_date_precision)
