import json
import sys
import types
from types import SimpleNamespace
from datapoint import DataPoint

fake_c104 = sys.modules.setdefault("c104", types.ModuleType("c104"))

class _Point:
    pass
fake_c104.Point = _Point
from types import SimpleNamespace as _SN
fake_c104.Type = _SN(M_ME_NC_1=None)

import batch_server


def test_convert_meta_io_address_to_int():
    p = SimpleNamespace(io_address=262176)
    assert batch_server.convertMetaIoAddressToInt(p) == 262176


def test_simulate_for_meta_frequency(monkeypatch):
    p = SimpleNamespace(io_address=262176)
    monkeypatch.setattr(batch_server.DataSimulator, "simulate_frequency", staticmethod(lambda: 42.42))
    assert batch_server._simulate_for_meta(p) == 42.42


def test_simulate_for_meta_voltage(monkeypatch):
    p = SimpleNamespace(io_address=262177)
    monkeypatch.setattr(batch_server.DataSimulator, "simulate_voltage", staticmethod(lambda: 211.11))
    assert batch_server._simulate_for_meta(p) == 211.11


def test_load_datapoints_file_assigns_missing_io(tmp_path):
    data = {
        "one": {"Type IEC": 36, "Unit / Einheit": "V"},
        "two": {"IOAddress": 10, "Type IEC": 36, "Unit / Einheit": "A"}
    }
    p = tmp_path / "dp.json"
    p.write_text(json.dumps(data), encoding="utf-8")
    out = batch_server.load_datapoints_file(str(p), start_io=5)
    
    assert 5 in out
    assert 10 in out
    assert out[5].name == "one"
    assert out[10].name == "two"
    assert isinstance(out[5], DataPoint)
