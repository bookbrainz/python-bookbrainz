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

from entity import Entity, Attribute
from entity_types import WorkType
from simple_objects import Language


class Work(Entity):
    work_type = Attribute('work_type', cls=WorkType)
    languages = Attribute('languages', parse=languages_from_json)

    def __init__(self):
        super(Work, self).__init__()

    @staticmethod
    def get_uri(id, agent):
        return '{}/work/{}'.format(agent.host_name, id)


def languages_from_json(json_data):
    return [Language.from_json(lang) for lang in json_data]
