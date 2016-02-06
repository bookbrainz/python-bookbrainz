from agent import Agent, default_agent
from base import Base
from creator import Creator
from edition import Edition
from entity import Entity
from entity_types import CreatorType, WorkType, PublisherType, PublicationType
from publication import Publication
from publisher import Publisher
from relationship import Relationship
from revision import EntityRevision
from simple_objects import Identifier, IdentifierType, Alias, Annotation,\
    Disambiguation, Language, EditionStatus, EditionFormat, Gender
from work import Work


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
