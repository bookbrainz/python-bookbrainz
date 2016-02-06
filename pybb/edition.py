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
from dateutil.parser import parse as parse_date
from simple_objects import CreatorCredit, Language, EditionFormat, EditionStatus
from pybb import default_agent
from parallel_requests import RequestQueue
from publisher import Publisher
from publication import Publication

class Edition(Entity):
    def __init__(self):
        super(self.__class__, self).__init__()

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

        self.publisher_uri = None
        self.publication_uri = None

    def fetch_from_json_filled(self, json_data):
        super(Edition, self).fetch_from_json_filled(json_data)

        self.release_date = parse_date(json_data['release_date']).date()
        self.release_date_precision = json_data['release_date_precision']

        self.pages = json_data['pages']

        self.width = json_data['width']
        self.height = json_data['height']
        self.depth = json_data['depth']

        self.weight = json_data['weight']

        self.creator_credit = \
            CreatorCredit.from_json(json_data['creator_credit'])
        self.language = \
            Language.from_json(json_data['language'])
        self.edition_format = \
            EditionFormat.from_json(json_data['edition_format'])
        self.edition_status = \
            EditionStatus.from_json(json_data['edition_status'])

        if 'publisher' in json_data:
            self.publisher = \
                Publisher.from_json(json_data['publisher'])
        if 'publication' in json_data:
            self.publication = \
                Publication.from_json(json_data['publication'])

        self.publisher_uri = json_data['publisher_uri']
        self.publication_uri = json_data['publication_uri']

    def release(self):
        return format_date(self.release_date, self.release_date_precision)

    @classmethod
    def add_id_get_more(cls, edition_json, request_queue, included):
        edition_new_data = {}
        if 'publisher' in included:
            edition_new_data['publisher'] = \
                request_queue.get_request(cls.get_publisher_uri(edition_json))

        if 'publication' in included:
            edition_new_data['publication'] = \
                request_queue.get_request(cls.get_publication_uri(edition_json))

        return edition_new_data

    @staticmethod
    def get_publisher_uri(entity_json):
        return entity_json['publisher_uri']

    @staticmethod
    def get_publication_uri(entity_json):
        return entity_json['publication_uri']

    @staticmethod
    def get_uri(id, agent):
        return '{}/edition/{}'.format(agent.host_name, id)
