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

"""This module specifies a class, Resource, which is designed to be used as the
base class for all resource models specified in this package."""

from base import Base


class Entity(Base):
    """Resource class, from which all other resource models are derived."""
    def __init__(self):
        super(self.__class__, self).__init__()
        self.entity_gid = None
        self.uri = None
        self.type = None

        self.default_alias_id = None

        self.last_updated = None

        self.annotation = None
        self.annotation_uri = None

        self.disambiguation = None
        self.disambiguation_uri = None

        self.aliases = None
        self.aliases_uri = None

        self.identifiers = None
        self.identifiers_uri = None

        self.relationships = None
        self.relationships_uri = None

        self.revision = None


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
        self.gender_id = None

        self.gender = None

    def begin(self):
        return format_date(self.begin_date, self.begin_date_precision)

    def end(self):
        return format_date(self.end_date, self.end_date_precision)


class Publication(Entity):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.publication_type = None


class Edition(Entity):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.edition_type = None

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

    def release(self):
        return format_date(self.release_date, self.release_date_precision)


class Publisher(Entity):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.publisher_type = None

        self.begin_date = None
        self.begin_date_precision = None

        self.end_date = None
        self.end_date_precision = None

        self.ended = None

    def begin(self):
        return format_date(self.begin_date, self.begin_date_precision)

    def end(self):
        return format_date(self.end_date, self.end_date_precision)


class Work(Entity):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.work_type = None
        self.languages = None

def format_date(date, precision):
    if date is None:
        return None

    if precision == 'YEAR':
        return '{:02}'.format(date.year)
    elif precision == 'MONTH':
        return '{:02}-{:02}'.format(date.year, date.month)
    else:
        return '{:02}-{:02}-{:02}'.format(date.year, date.month, date.day)
