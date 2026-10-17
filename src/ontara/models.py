"""Модели данных Ontara"""

from dataclasses import dataclass, field
from uuid import UUID, uuid4

@dataclass
class WorldEntity:
    """Сущность вымышленного мира"""

    name: str
    type: str
    desc: str = ""
    id: UUID = field(default_factory=uuid4)


@dataclass
class World:
    """Вымышленный мир, содержащий набор сущностей."""

    name: str
    desc: str = ""
    entities: list[WorldEntity] = field(default_factory=list[WorldEntity])
    id: UUID = field(default_factory=uuid4)

