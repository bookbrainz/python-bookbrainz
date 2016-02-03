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


class Annotation(Base):
    def __init__(self):
        super(self.__class__, self).__init__()

        self.annotation_id = None
        self.content = None
        self.created_at = None

    def fetch_from_json(self, json_data):
        self.annotation_id = json_data['annotation_id']
        self.content = json_data['content']
        self.created_at = json_data['created_at']


class Disambiguation(Base):
    def __init__(self):
        super(self.__class__, self).__init__()

        self.disambiguation_id = None
        self.comment = None

    def fetch_from_json(self, json_data):
        self.disambiguation_id = json_data['disambiguation_id']
        self.comment = json_data['comment']

class Alias(Base):
    def __init__(self):
        super(self.__class__, self).__init__()

        self.alias_id = None
        self.name = None
        self.sort_name = None
        self.primary = None
        self.language = None

    def fetch_from_json(self, json_data):
        self.alias_id = json_data['alias_id']
        self.name = json_data['name']
        self.sort_name = json_data['sort_name']
        self.primary = json_data['primary']

        self.language = Language()
        self.language.fetch_from_json(json_data['language'])

class Identifier(Base):
    def __init__(self):
        super(self.__class__, self).__init__()

        self.identifier_id = None
        self.identifier_type = None
        self.value = None

    def fetch_from_json(self, json_data):
        self.identifier_id = json_data['identifier_id']
        self.value = json_data['value']

        self.identifier_type = IdentifierType()
        self.identifier_type.fetch_from_json(json_data)


class IdentifierType(Base):
    def __init__(self):
        super(self.__class__, self).__init__()

        self.identifier_type_id = None
        self.label = None

    def fetch_from_json(self, json_data):
        self.identifier_type_id = json_data['identifier_type_id']
        self.label = json_data['label']


class Gender(Base):
    def __init__(self):
        super(self.__class__, self).__init__()

        self.gender_id = None
        self.name = None

    def fetch_from_json(self, json_data):
        self.gender_id = json_data['gender_id']
        self.name = json_data['name']


class Language(Base):
    def __init__(self):
        super(self.__class__, self).__init__()

    language_id = None
    name = None

    def fetch_from_json(self, json_data):
        self.language_id = json_data['language_id']
        self.name = json_data['name']


class EditionFormat(Base):
    def __init__(self):
        super(self.__class__, self).__init__()

        self.edition_format_id = None
        self.label = None

    def fetch_from_json(self, json_data):
        self.edition_format_id = json_data['edition_format_id']
        self.label = json_data['label']


class EditionStatus(Base):
    def __init__(self):
        super(self.__class__, self).__init__()

        self.edition_status_id = None
        self.label = None

    def fetch_from_json(self, json_data):
        self.edition_status_id = json_data['edition_status_id']
        self.label = json_data['label']