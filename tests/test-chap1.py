from Chapter_1.Chap1 import tip_calculator, total_bill
from unittest.mock import patch

@patch('builtins.input', side_effect=[100.0, 10])
def test_tip_calc_returns_two_dp_float(mock_input):
    mock_input.side_effect = [100.0, 10]
    bill = float(mock_input())
    tip = float(mock_input())
    output = tip_calculator(bill,tip)
    assert isinstance(output, float)
    assert f"{output:.2f}" == "10.00"

@patch('builtins.input', side_effect=[100.0, 20])
def test_tip_calc_handles_high_tip_percentage(mock_input):
    bill = float(mock_input())
    tip = float(mock_input())
    output = tip_calculator(bill,tip)
    assert isinstance(output, float)
    assert f"{output:.2f}" == "20.00"

@patch('builtins.input', side_effect=[50.0, 0])
def test_tip_calc_handles_zero_tip(mock_input):
    bill = float(mock_input())
    tip = float(mock_input())
    output = tip_calculator(bill,tip)
    assert isinstance(output, float)
    assert f"{output:.2f}" == "0.00"

@patch('builtins.input', side_effect=[1000.0, 0])
def test_total_bill_calc_high_amount(mock_input):
    bill = float(mock_input())
    tip = float(mock_input())
    output = total_bill(bill,tip)
    assert isinstance(output, float)
    assert f"{output:.2f}" == "1000.00"

@patch('builtins.input', side_effect=[1000.0, 80])
def test_total_bill_calc_high_tip_amount(mock_input):
    bill = float(mock_input())
    tip = float(mock_input())
    output = total_bill(bill,tip)
    assert isinstance(output, float)
    assert f"{output:.2f}" == "1800.00"
