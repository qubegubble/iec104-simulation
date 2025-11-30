import data_simulator


def test_simulate_voltage_monkeypatched(monkeypatch):
    monkeypatch.setattr(data_simulator.random, "uniform", lambda a, b: 211.23456)
    assert data_simulator.DataSimulator.simulate_voltage() == round(211.23456, 2)


def test_simulate_frequency_monkeypatched(monkeypatch):
    monkeypatch.setattr(data_simulator.random, "uniform", lambda a, b: 49.98765)
    assert data_simulator.DataSimulator.simulate_frequency() == round(49.98765, 2)


def test_simulate_current_and_power(monkeypatch):
    # Return a deterministic value for both current and power
    monkeypatch.setattr(data_simulator.random, "uniform", lambda a, b: 12.3456)
    assert data_simulator.DataSimulator.simulate_current(0, 16) == round(12.3456, 2)
    assert data_simulator.DataSimulator.simulate_power(100, 200) == round(12.3456, 2)
