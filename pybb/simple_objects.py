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


class Disambiguation(Base):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.disambiguation_id = None
        self.comment = None


class Alias(Base):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.alias_id = None
        self.name = None
        self.sort_name = None
        self.language = None
        self.primary = None


class Identifier(Base):
    def __init__(self):
        super(self.__class__, self).__init__()
    identifier_id = None
    identifier_type = None
    value = None


class IdentifierType(Base):
    def __init__(self):
        super(self.__class__, self).__init__()
    identifier_type_id = None
    label = None


class Gender(Base):
    def __init__(self):
        super(self.__class__, self).__init__()
    id = None
    name = None


class Language(Base):
    def __init__(self):
        super(self.__class__, self).__init__()
    language_id = None
    name = None


class EditionFormat(Base):
    def __init__(self):
        super(self.__class__, self).__init__()
    edition_format_id = None
    label = None


class EditionStatus(Base):
    def __init__(self):
        super(self.__class__, self).__init__()
    edition_status_id = None
    label = None
