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

from base import Attribute
from entity import Entity
from utils import parse_date, format_date
from entity_types import CreatorType
from simple_objects import Gender
import utils


class Creator(Entity):
    creator_type = Attribute('creator_type', cls=CreatorType)

    begin_date = Attribute('begin_date', parse=parse_date)
    begin_date_precision = Attribute('begin_date_precision')

    end_date = Attribute('end_date', parse=parse_date)
    end_date_precision = Attribute('end_date_precision')

    ended = Attribute('ended')
    country_id = Attribute('country_id')
    gender = Attribute('gender', cls=Gender)

    def __init__(self):
        super(Creator, self).__init__()

    def begin(self):
        return format_date(self.begin_date, self.begin_date_precision)

    def end(self):
        return format_date(self.end_date, self.end_date_precision)

    @staticmethod
    def get_uri(id, agent):
        return '{}/creator/{}'.format(agent.host_name, id)

utils.type_to_class['creator'] = Creator
