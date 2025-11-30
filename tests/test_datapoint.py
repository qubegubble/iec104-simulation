from datapoint import DataPoint


def test_datapoint_fields():
    dp = DataPoint(name="Test", io_address=1, type_iec=36, unit="V", raw={"IOAddress": 1})
    assert dp.name == "Test"
    assert dp.io_address == 1
    assert dp.type_iec == 36
    assert dp.unit == "V"
    assert dp.raw["IOAddress"] == 1
