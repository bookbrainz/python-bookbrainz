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

from base import Attribute
from entity import Entity
from entity_types import PublicationType
import utils


class Publication(Entity):
    publication_type = Attribute('publication_type', cls=PublicationType)

    def __init__(self):
        super(Publication, self).__init__()

    @staticmethod
    def get_uri(id, agent):
        return '{}/publication/{}'.format(agent.host_name, id)

utils.type_to_class['publication'] = Publication
