# -*- coding: utf8 -*-

# Copyright (C) 2014-2016  Ben Ockmore, Stanisław Szcześniak

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

from base import Base
from dateutil.parser import parse as parse_date

class Relationship(Base):
    def __init__(self):
        super(self.__class__, self).__init__()

        self.entities = None
        self.last_updated = None
        self.relationship_id = None
        self.relationship_type = None
        self.texts = None
        self.uri = None

    def fetch_from_json_filled(self, json_data):
        self.last_updated = parse_date(json_data['last_updated'])
        self.relationship_id = json_data['relationship_id']
        self.uri = json_data['uri']

        self.entities = relationship_entities_from_json(json_data['entities'])
        self.texts = relationship_texts_from_json(json_data['texts'])

        self.relationship_type = \
            RelationshipType.from_json(json_data['relationship_type'])


class RelationshipType(Base):
    def __init__(self):
        super(self.__class__, self).__init__()

        self.relationship_type_id = None
        self.label = None
        self.deprecated = None
        self.description = None
        self.template = None
        self.child_order = None
        self.parent = None

    def fetch_from_json_filled(self, json_data):
        self.relationship_type_id = json_data['relationship_type_id']
        self.label = json_data['label']
        self.deprecated = json_data['deprecated']
        self.description = json_data['description']
        self.template = json_data['template']
        self.child_order = json_data['child_order']
        self.parent = json_data['parent']


class RelationshipEntity(Base):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.type = None
        self.entity_gid = None
        self.uri = None
        self.position = None

    def fetch_from_json_filled(self, json_data):
        self.type = json_data['entity']['_type']
        self.entity_gid = json_data['entity']['entity_gid']
        self.uri = json_data['entity']['uri']
        self.position = json_data['position']


class RelationshipText(Base):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.position = None
        self.text = None

    def fetch_from_json_filled(self, json_data):
        self.position = json_data['position']
        self.text = json_data['text']


def relationship_entities_from_json(json_data):
    return [RelationshipEntity.from_json(entity)
            for entity in json_data['entities']]


def relationship_texts_from_json(json_data):
    return [RelationshipText.from_json(text)
            for text in json_data]
