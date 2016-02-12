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
from entity import Entity, format_date, parse_date
from publication import Publication
from publisher import Publisher
from simple_objects import CreatorCredit, Language, EditionFormat, EditionStatus


class Edition(Entity):
    release_date = Attribute('release_date', parse=parse_date)
    release_date_precision = Attribute('release_date_precision')

    # Number of pages
    pages = Attribute('pages')

    # Dimensions, stored as integer millimetre values
    width = Attribute('width')
    height = Attribute('height')
    depth = Attribute('depth')

    # Weight in grams
    weight = Attribute('weight')

    creator_credit = Attribute('creator_credit', cls=CreatorCredit)

    language = Attribute('language', cls=Language)

    edition_format = Attribute('edition_format', cls=EditionFormat)
    edition_status = Attribute('edition_status')

    publisher = Attribute('publisher', cls=Publisher)
    publisher_uri = Attribute('publisher_uri')

    publication = Attribute('publication', cls=Publication)
    publication_uri = Attribute('publication_uri')

    def __init__(self):
        super(Edition, self).__init__()

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
