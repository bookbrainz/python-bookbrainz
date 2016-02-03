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

from base import Base
from user import User


class EntityRevision(Base):
    def __init__(self):
        super(self.__class__, self).__init__()

        self.revision_id = None
        self.user = None
        self.created_at = None
        self.parent_id = None
        self.note = None
        self.entity_uri = None
        self.uri = None

    def _fetch_from_json(self, json_data):
        self.created_at = json_data['created_at']
        self.entity_uri = json_data['entity_uri']
        self.note = json_data['note']
        self.parent_id = json_data['parent_id']
        self.revision_id = json_data['revision_id']
        self.uri = json_data['uri']

        self.user = User.from_json(json_data['user'])
