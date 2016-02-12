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

from dateutil.parser import parse as parse_datetime

from base import Base, Attribute
from parallel_requests import RequestQueue
from pybb import default_agent
from utils import entity_type_name_to_class
from relationship import Relationship
from revision import EntityRevision
from simple_objects import Alias, Identifier, Disambiguation, Annotation


def aliases_from_json(json_data):
    return [Alias.from_json(alias) for alias in json_data['objects']]


def identifiers_from_json(json_data):
    return [Identifier.from_json(id) for id in json_data['objects']]


def relationships_from_json(json_data):
    return [Relationship.from_json(rel) for rel in json_data['objects']]


class Entity(Base):
    entity_gid = Attribute('entity_gid')
    uri = Attribute('uri')
    type = Attribute('type', ws_name='_type', parse=entity_type_name_to_class)

    last_updated = Attribute('last_updated', parse=parse_datetime)

    aliases = Attribute('aliases', parse=aliases_from_json)
    aliases_uri = Attribute('aliases_uri')

    annotation = Attribute('annotation', cls=Annotation)
    annotation_uri = Attribute('annotation_uri')

    disambiguation = Attribute('disambiguation', cls=Disambiguation)
    disambiguation_uri = Attribute('disambiguation_uri')

    identifiers = Attribute('identifiers', parse=identifiers_from_json)
    # Commented due to bug that should be named but it wasn't
    # identifiers_uri = Attribute('identifiers_uri')

    relationships = Attribute('relationships', parse=relationships_from_json)
    relationships_uri = Attribute('relationships_uri')

    revision = Attribute('revision', cls=EntityRevision)

    def __init__(self):
        super(Entity, self).__init__()

    @classmethod
    def get_multiple_ids(cls, ids, included, agent=default_agent):
        responses_json = cls.get_multiple_ids_json(ids, included, agent)
        entities = [cls.from_json(json_data) for json_data in responses_json]

        return entities

    @classmethod
    def get_multiple_ids_derived(cls, ids, included, agent=default_agent):
        """ Similar to get_multiple_ids but it returns
        derived classes like Creator or Work (not Entity)

        :param ids: bbids of entities
        :param included:
        :param agent:
        :return: list of entities
        """

        classes = cls.get_entity_types_from_ids(ids, agent)
        responses_json = \
            cls.get_multiple_ids_json_derived(classes, ids, included, agent)

        entities = [type_class.from_json(json_data)
                    for type_class, json_data in zip(classes, responses_json)]

        return entities

    @classmethod
    def get_multiple_ids_json(cls, ids, included, agent):
        request_queue = RequestQueue()
        responses_json = []

        # First round of requests
        for id in ids:
            responses_json.append(
                cls.add_id_get(id, request_queue, included, agent)
            )
        request_queue.send_all()

        # Second round of requests (uses data from the first one)
        for response in responses_json:
            response.update(
                cls.add_id_get_more(response, request_queue, included)
            )
        request_queue.send_all()

        return responses_json

    @staticmethod
    def get_multiple_ids_json_derived(classes, ids, included, agent):
        request_queue = RequestQueue()
        responses_json = []

        # First round of requests
        for cls, id in zip(classes, ids):
            responses_json.append(
                cls.add_id_get(id, request_queue, included, agent)
            )
        request_queue.send_all()

        # Second round of requests (uses data from the first one)
        for cls, response in zip(classes, responses_json):
            response.update(
                cls.add_id_get_more(response, request_queue, included)
            )
        request_queue.send_all()

        return responses_json

    @classmethod
    def add_id_get(cls, id, request_queue, included, agent):
        entity_request = request_queue.get_request(cls.get_uri(id, agent))

        if 'aliases' in included:
            entity_request['aliases'] = \
                request_queue.get_request(
                    cls.get_aliases_uri(id, agent)
                )

        if 'relationships' in included:
            entity_request['relationships'] = \
                request_queue.get_request(
                    cls.get_relationships_uri(id, agent)
                )

        if 'identifiers' in included:
            entity_request['identifiers'] = \
                request_queue.get_request(
                    cls.get_identifiers_uri(id, agent)
                )

        if 'annotation' in included:
            entity_request['annotation'] = \
                request_queue.get_request(
                    cls.get_annotation_uri(id, agent)
                )

        if 'disambiguation' in included:
            entity_request['disambiguation'] = \
                request_queue.get_request(
                    cls.get_disambiguation_uri(id, agent)
                )

        return entity_request

    @classmethod
    def add_id_get_more(cls, entity_json, request_queue, included):
        return {}

    @classmethod
    def delete_multiple_ids(cls, ids, revision_notes, agent=default_agent):
        request_queue = RequestQueue()

        for id, note in zip(ids, revision_notes):
            request_queue.delete_request(
                cls.get_uri(id, agent),
                {'Authorization': 'Bearer {}'.format(agent.oauth_acess_token),
                 'Content-Type': 'application/json'},
                {"revision": {"note": note}}
            )

        request_queue.send_all()

    @classmethod
    def get_entity_types_from_ids(cls, ids, agent):
        """ Gets info about each entity:
        type (like 'creator' or 'work')

        :param ids: bbids of entities
        :param agent: used agent
        :return: list of classes
        """
        entities = Entity.get_multiple_ids(ids, [], agent)
        return [entity.type for entity in entities]

    @staticmethod
    def get_uri(id, agent):
        return '{}/entity/{}'.format(agent.host_name, id)

    @staticmethod
    def get_aliases_uri(id, agent):
        return '{}/entity/{}/aliases'.format(agent.host_name, id)

    @staticmethod
    def get_relationships_uri(id, agent):
        return '{}/entity/{}/relationships'.format(agent.host_name, id)

    @staticmethod
    def get_identifiers_uri(id, agent):
        return '{}/entity/{}/identifiers'.format(agent.host_name, id)

    @staticmethod
    def get_annotation_uri(id, agent):
        return '{}/entity/{}/annotation'.format(agent.host_name, id)

    @staticmethod
    def get_disambiguation_uri(id, agent):
        return '{}/entity/{}/disambiguation'.format(agent.host_name, id)


