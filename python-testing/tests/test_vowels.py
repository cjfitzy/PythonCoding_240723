import pytest
from programs import vowels

def test_fact():
	assert vowels.vowels("claire") == 3
	assert vowels.vowels("supercalifragilistic expialidocious") == 16
	