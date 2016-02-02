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

from structures import Entity, Creator, Work, Edition, Publisher, Publication


def entity_get_from_json(self, json_data):
    pass

Entity.get_from_json = entity_get_from_json


def creator_get_from_json(self, json_data):
    super(Creator, self).get_from_json(json_data)

Creator.get_from_json = creator_get_from_json


def work_get_from_json(self, json_data):
    super(Work, self).get_from_json(json_data)

Work.get_from_json = work_get_from_json


def edition_get_from_json(self, json_data):
    super(Edition, self).get_from_json(json_data)

Edition.get_from_json = edition_get_from_json


def publisher_get_from_json(self, json_data):
    super(Publisher, self).get_from_json(json_data)

Publisher.get_from_json = publisher_get_from_json


def publication_get_from_json(self, json_data):
    super(Publication, self).get_from_json(json_data)

Publication.get_from_json = publication_get_from_json