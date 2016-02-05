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
from entity_types import CreatorType
from dateutil.parser import parse as parse_date
from simple_objects import Gender
from pybb import default_agent

class Creator(Entity):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.creator_type = None

        self.begin_date = None
        self.begin_date_precision = None

        self.end_date = None
        self.end_date_precision = None

        self.ended = None
        self.country_id = None
        self.gender = None

    def fetch_from_json_filled(self, json_data):
        super(self.__class__, self).fetch_from_json(json_data)

        self.begin_date = parse_date(json_data['begin_date']).date()
        self.begin_date_precision = json_data['begin_date_precision']

        self.end_date = parse_date(json_data['end_date']).date()
        self.end_date_precision = json_data['end_date_precision']

        self.creator_type = \
            CreatorType.from_json(json_data['creator_type'])
        self.gender = \
            Gender.from_json(json_data['creator'])
        self.ended = json_data['ended']

    def begin(self):
        return format_date(self.begin_date, self.begin_date_precision)

    def end(self):
        return format_date(self.end_date, self.end_date_precision)

    @classmethod
    def get_multiple_ids(cls, ids, included=[], agent=default_agent):
        pass

    @classmethod
    def add_id_get(cls, id, request_queue, included, agent):
        super(cls,cls).add_id_get(id, request_queue, included. agent)

    @classmethod
    def get_uri(cls, id, agent):
        return '{}/creator/{}'.format(agent.host_name, id)
