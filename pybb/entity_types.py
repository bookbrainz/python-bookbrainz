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


class WorkType(Base):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.work_type_id = None
        self.label = None


class PublicationType(Base):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.publication_type_id = None
        self.label = None


class CreatorType(Base):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.creator_type_id = None
        self.label = None


class PublisherType(Base):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.publisher_type_id = None
        self.label = None
