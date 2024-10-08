from water_flow import pressure_loss_from_pipe, pressure_gain_from_water_height, water_colum_heigth
from pytest import approx
import pytest

def test_pressure_loss_from_pipe():
    assert(pressure_loss_from_pipe(0.048692, 0.00, 0.018, 1.75) == approx(0.000, abs =0.001))
    assert(pressure_loss_from_pipe(0.048692, 200.00, 0.000, 1.75) == approx(0.000, abs =0.001))
    assert(pressure_loss_from_pipe(0.048692, 200.00, 0.01, 0.00) == approx(0.000, abs =0.001))
    assert(pressure_loss_from_pipe(0.048692 ,200.00, 0.018, 1.75) == approx(-113.008, abs =0.001))
    assert(pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.65) == approx(-100.462, abs =0.001))
    assert(pressure_loss_from_pipe(0.286870, 1000.00, 0.013 ,1.65) == approx(-61.576, abs =0.001))
    assert(pressure_loss_from_pipe(0.286870, 1800.75, 0.013, 1.65) == approx(-110.884, abs =0.001))

def test_pressure_gain_from_water_height():
    assert(pressure_gain_from_water_height(0.0) == approx(0.000, abs =0.001))
    assert(pressure_gain_from_water_height(30.2) == approx(295.628, abs =0.001))
    assert(pressure_gain_from_water_height(50.0) == approx(489.450, abs =0.001))

def test_water_colum_heigth():
    assert(water_colum_heigth(0.0,0.0) == 0.0)
    assert(water_colum_heigth(0.0, 10.0) == 7.5)
    assert(water_colum_heigth(25.0, 0.0) == 25.0)
    assert(water_colum_heigth(48.3, 12.8) == 57.9)

pytest.main(["-v", "--tb=line", "-rN", __file__])