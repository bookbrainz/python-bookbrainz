# -*- coding: utf8 -*-

# Copyright (C) 2014  Ben Ockmore, Stanisław Szcześniak

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


class Base:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

class Entity(Base):
    """Resource class, from which all other resource models are derived."""
    entity_gid = None
    uri = None

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
