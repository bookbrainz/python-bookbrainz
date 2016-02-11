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

from base import Base, Attribute
from dateutil.parser import parse as parse_datetime


class Relationship(Base):
    relationship_id = Attribute('relationship_id')
    last_updated = Attribute('last_updated', parse=parse_datetime)
    relationship_type = Attribute('relationship_type', cls=RelationshipType)
    uri = Attribute('uri')

    entities = Attribute('entities', parse=relationship_entities_from_json)
    texts = Attribute('texts', parse=relationship_texts_from_json)

    def __init__(self):
        super(Relationship, self).__init__()


class RelationshipType(Base):
    relationship_type_id = Attribute('relationship_type_id')
    label = Attribute('label')
    deprecated = Attribute('deprecated')
    description = Attribute('description')
    template = Attribute('template')
    child_order = Attribute('child_order')
    parent = Attribute('parent')

    def __init__(self):
        super(RelationshipType, self).__init__()


class RelationshipEntity(Base):
    type = Attribute('type', ws_name=('entity', '_type'))
    entity_gid = Attribute('entity_gid', ws_name=('entity', 'entity_gid'))
    uri = Attribute('uri', ws_name=('entity', 'uri'))
    position = Attribute('position')


class RelationshipText(Base):
    position = Attribute('position')
    text = Attribute('text')

    def __init__(self):
        super(RelationshipText, self).__init__()


def relationship_entities_from_json(json_data):
    return [RelationshipEntity.from_json(entity)
            for entity in json_data]


def relationship_texts_from_json(json_data):
    return [RelationshipText.from_json(text)
            for text in json_data]
