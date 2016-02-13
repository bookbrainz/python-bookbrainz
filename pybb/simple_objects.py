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


class Annotation(Base):
    annotation_id = Attribute('annotation_id')
    content = Attribute('content')
    created_at = Attribute('created_at', parse=parse_datetime)


class Disambiguation(Base):
    disambiguation_id = Attribute('disambiguation_id')
    comment = Attribute('comment')


class Language(Base):
    language_id = Attribute('language_id')
    name = Attribute('name')


class Alias(Base):
    alias_id = Attribute('alias_id')
    name = Attribute('name')
    sort_name = Attribute('sort_name')
    primary = Attribute('primary')
    language = Attribute('language', cls=Language)


class IdentifierType(Base):
    identifier_type_id = Attribute('identifier_type_id')
    label = Attribute('label')


class Identifier(Base):
    identifier_id = Attribute('identifier_id')
    value = Attribute('value')
    identifier_type = Attribute('identifier_type', IdentifierType)


class Gender(Base):
    gender_id = Attribute('gender_id')
    name = Attribute('name')


class EditionFormat(Base):
    edition_format_id = Attribute('edition_format_id')
    label = Attribute('label')


class EditionStatus(Base):
    edition_status_id = Attribute('edition_status_id')
    label = Attribute('label')


class CreatorCredit(Base):
    begin_phrase = Attribute('begin_phrase')
    creator_credit_id = Attribute('creator_credit_id')
    names = Attribute('names')


class CreatorCreditName(Base):
    pass
