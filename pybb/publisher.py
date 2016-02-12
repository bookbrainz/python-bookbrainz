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

from entity import Entity, format_date, parse_date
from entity_types import PublisherType
from base import Attribute


class Publisher(Entity):
    publisher_type = Attribute('publisher_type', cls=PublisherType)

    begin_date = Attribute('begin_date', parse=parse_date)
    begin_date_precision = Attribute('begin_date_precision')

    end_date = Attribute('end_date', parse=parse_date)
    end_date_precision = Attribute('end_date_precision')

    ended = Attribute('ended')

    def __init__(self):
        super(Publisher, self).__init__()

    def begin(self):
        return format_date(self.begin_date, self.begin_date_precision)

    def end(self):
        return format_date(self.end_date, self.end_date_precision)

    @staticmethod
    def get_uri(id, agent):
        return '{}/publisher/{}'.format(agent.host_name, id)
