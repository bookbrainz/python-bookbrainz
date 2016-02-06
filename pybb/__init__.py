from base import Base
from agent import Agent, default_agent
from entity import Entity
from creator import Creator
from work import Work
from edition import Edition
from publisher import Publisher
from publication import Publication
from entity_types import CreatorType, WorkType, PublisherType, PublicationType
from relationship import Relationship
from revision import EntityRevision
from simple_objects import Identifier, IdentifierType, Alias, Annotation,\
    Disambiguation, Language, EditionStatus, EditionFormat, Gender


@staticmethod
def type_to_class(type_name):
    return {
        "Creator": Creator,
        "Work": Work,
        "Edition": Edition,
        "Publisher": Publisher,
        "Publication": Publication
    }[type_name]

Entity.type_to_class = type_to_class
