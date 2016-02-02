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

from structures.base import Base

class Annotation(Base):
    annotation_id = None
    content = None
    created_at = None


class Disambiguation(Base):
    disambiguation_id = None
    comment = None


class Alias(Base):
    alias_id = None
    name = None
    sort_name = None
    language = None
    primary = None


class Identifier(Base):
    identifier_id = None
    identifier_type = None
    value = None


class IdentifierType(Base):
    identifier_type_id = None
    label = None


class Gender(Base):
    id = None
    name = None


class Language(Base):
    language_id = None
    name = None