from ontara import __version__
from ontara.models import WorldEntity, World

def test_version_is_valid() -> None:
    assert __version__ == "0.0.1.dev0"

def test_world_entity_creation() -> None:
    entity = WorldEntity(name="Terra", type="planet")

    assert entity.name == "Terra"
    assert entity.type == "planet"
    assert entity.desc == ""
    assert entity.id is not None

def test_world_entities_have_unique_ids() -> None:
    first = WorldEntity(name="Terra", type="planet")
    second = WorldEntity(name="Mars", type="planet")

    assert first.id != second.id

def test_world_creation() -> None:
    world = World(name="Astra")

    assert world.name == "Astra"
    assert world.desc == ""
    assert world.entities == []
    assert world.id is not None

def test_world_can_contain_entities() -> None:
    world = World(name="Astra")
    entity = WorldEntity(name="Terra", type="planet")

    world.entities.append(entity)

    assert len(world.entities) == 1
    assert world.entities[0] is entity

def test_worlds_have_independent_entity_lists() -> None:
    first_world = World(name="Astra")
    second_world = World(name="Nexus")

    first_world.entities.append(
        WorldEntity(name="Terra", type="planet")
    )

    assert len(first_world.entities) == 1
    assert len(second_world.entities) == 0