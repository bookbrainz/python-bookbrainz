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

""" This module includes utilities for making parallel requests
 using grequests. There is a request queue implemented,
 which allows among others to:
    -> add request to the queue (append_request),
    -> add GET request to the queue (get_request)
    -> add DELETE request to the queue (delete_request)
    -> send all requests
"""

import json
import grequests


# TODO handling of exceptions
class RequestQueue(object):
    def __init__(self):
        self.requests = []

    def clear(self):
        del self.requests[:]

    def append_request(self, request):
        """ Adds a grequests request to the queue

        Returns a dict with JSON data but it gets filled after calling send_all.

        :param request: request to add
        :return: JSON data from response in form of dict
        """
        result_dict = {}
        request_object = RequestObject(request, result_dict)
        self.requests.append(request_object)
        return result_dict

    def get_request(self, uri):
        """ Adds a GET request to the queue

        :param uri: request uri
        :return: JSON data from response in form of dict
        """
        return self.append_request(grequests.get(uri))

    def delete_request(self, uri, headers, params):
        """ Adds a DELETE request to the queue

        :param uri: request uri
        :param headers: request headers
        :param params: request JSON data (in form of dict)
        :return: JSON data from response in form of dict
        """
        return self.append_request(
            grequests.delete(uri, headers=headers, params=params))

    def send_all(self):
        """ Sends all requests from queue and clears it after.

        Fills data returned in requests requested before.

        :return: None
        """
        responses = grequests.map([ob.request for ob in self.requests])
        for index, response in enumerate(responses):
            content = json.loads(response.content)
            if content:
                self.requests[index].result_dict.update(content)
        self.clear()


class RequestObject(object):
    def __init__(self, request, result_dict):
        self.request = request
        self.result_dict = result_dict
