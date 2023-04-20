import pytest

@pytest.mark.parametrize("skladnik,suma",[(5,10),(2,4)])
def test_dodawania(skladnik, suma):
    assert skladnik+skladnik == suma

@pytest.mark.parametrize("skladnik,suma", [(5, 8), (2, 3)])
def test_dodawania(skladnik, suma):
    assert skladnik + skladnik == suma, "Suma powinna być równa " + str(skladnik + skladnik)