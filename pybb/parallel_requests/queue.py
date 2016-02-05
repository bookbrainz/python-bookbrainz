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

import grequests
import json


# TODO handling of exceptions
class RequestQueue(object):
    def __init__(self):
        self.requests = []

    def clear(self):
        del self.requests[:]

    def request(self, request):
        result_dict = {}
        request_object = RequestObject(request, result_dict)
        self.requests.append(request_object)
        return result_dict

    def get_request(self, uri):
        return self.request(grequests.get(uri))

    def send_all(self):
        responses = grequests.map([ob.request for ob in self.requests])
        for index, response in enumerate(responses):
            content = json.loads(response.content)
            self.requests[index].result_dict.update(content)
        self.clear()


class RequestObject(object):
    def __init__(self, request, result_dict):
        self.request = request
        self.result_dict = result_dict
