import pytest
from brownie import NineTailsToken, accounts

@pytest.fixture
def token():
    return NineTailsToken.deploy(1000000 * 10**18, {'from': accounts[0]})

def test_initial_supply(token):
    assert token.totalSupply() == 1000000 * 10**18
    assert token.balanceOf(accounts[0]) == 1000000 *10**18

def test_transfer(token):
    token.transfer(accounts[1], 100 *10**18, {'from': accounts[0]})
    assert token.balanceOf(accounts[1]) == 100 * 10**18
    assert token.balanceOf(accounts[0]) == 999900 * 10**18