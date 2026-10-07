from .collection_tools import collection_tools as _collection_tools
from .parent_affinity import parent_affinity_tools


def collection_tools(collection, session):
    """The collection tools plus my_parents_affinity (read-only; it needs the store but not the session)."""
    return [*_collection_tools(collection, session), *parent_affinity_tools(collection)]


__all__ = ["collection_tools"]
