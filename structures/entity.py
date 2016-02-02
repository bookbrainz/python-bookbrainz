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

from structures.base import Base


class Entity(Base):
    """Resource class, from which all other resource models are derived."""
    entity_gid = None
    uri = None
    type = None

    default_alias_id = None

    last_updated = None

    annotation = None
    annotation_uri = None

    disambiguation = None
    disambiguation_uri = None

    aliases = None
    aliases_uri = None

    identifiers = None
    identifiers_uri = None

    relationships = None
    relationships_uri = None

    revision = None


class CreatorOnly(object):
    creator_type = None

    begin_date = None
    begin_date_precision = None

    @property
    def begin(self):
        return format_date(self.begin_date, self.begin_date_precision)

    end_date = None
    end_date_precision = None

    @property
    def end(self):
        return format_date(self.end_date, self.end_date_precision)

    ended = None

    country_id = None
    gender_id = None

    gender = None


class Creator(CreatorOnly, Entity):
    pass


class PublicationOnly(object):
    publication_type = None


class Publication(PublicationOnly, Entity):
    pass


class EditionOnly(object):
    edition_type = None

    release_date = None
    release_date_precision = None

    @property
    def release(self):
        return format_date(self.release_date, self.release_date_precision)

    pages = None

    # Dimensions, stored as integer millimetre values
    width = None
    height = None
    depth = None

    # Weight in grams
    weight = None

    creator_credit = None
    language = None
    edition_format = None
    edition_status = None
    publisher = None
    publication = None


class Edition(EditionOnly, Entity):
    pass


class PublisherOnly(object):
    publisher_type = None

    begin_date = None
    begin_date_precision = None

    @property
    def begin(self):
        return format_date(self.begin_date, self.begin_date_precision)

    end_date = None
    end_date_precision = None

    @property
    def end(self):
        return format_date(self.end_date, self.end_date_precision)

    ended = None


class Publisher(PublicationOnly, Entity):
    pass


class WorkOnly(object):
    work_type = None
    languages = None


class Work(WorkOnly, Entity):
    pass


def format_date(date, precision):
    if date is None:
        return None

    if precision == 'YEAR':
        return '{:02}'.format(date.year)
    elif precision == 'MONTH':
        return '{:02}-{:02}'.format(date.year, date.month)
    else:
        return '{:02}-{:02}-{:02}'.format(date.year, date.month, date.day)
