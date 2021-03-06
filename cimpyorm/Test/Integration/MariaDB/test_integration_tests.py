import cimpyorm.auxiliary
from cimpyorm.api import load, parse
import pytest
import cimpyorm

from cimpyorm.backends import MariaDB


def test_parse_load(full_grid):
    try:
        cimpyorm.auxiliary.get_path("SCHEMAROOT")
    except KeyError:
        pytest.skip(f"Schemata not configured")
    path = "integration_test"
    session, m = parse(full_grid, MariaDB(path=path, host="localhost"))
    session.close()
    session, m = load(MariaDB(path=path, host="localhost"))
    session.close()
    MariaDB(path=path, host="localhost").drop()


def test_parse_parse(full_grid):
    try:
        cimpyorm.auxiliary.get_path("SCHEMAROOT")
    except KeyError:
        pytest.skip(f"Schemata not configured")
    path = "integration_test"
    session, m = parse(full_grid, MariaDB(path=path, host="localhost"))
    session.close()
    session, m = parse(full_grid, MariaDB(path=path, host="localhost"))
    assert session.query(m.Terminal).first().ConductingEquipment
    session.close()
    MariaDB(path=path, host="localhost").drop()
