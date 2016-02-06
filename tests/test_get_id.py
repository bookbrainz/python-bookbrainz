# -*- coding: utf8 -*-

# Copyright (C) 2016 Stanisław Szcześniak

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

from unittest import TestCase
from pybb.entity import Entity


class TestGetID(TestCase):
    def test_get_entities_by_ids(self):
        entities = Entity.get_multiple_ids(
            ['32f78c16-39d0-4595-afe0-974f89dd71ad'],
            included=frozenset(['aliases'])
        )
        entity = entities[0]
        self.assertEquals(
            entity.aliases[0].name,
            'The Hobbit & The Lord of the Rings'
        )
