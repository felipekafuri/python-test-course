import pytest # type: ignore

def test_out_first_test() -> None:
  assert 1 == 1

@pytest.mark.skip
def test_should_be_skipped() -> None:
  assert 1 == 2

@pytest.mark.skipif(4 > 1, reason="Skipped because is 4 > 1")
def test_should_be_skipped_if() -> None:
  assert 1 == 2

@pytest.mark.xfail
def test_dont_care_if_fails() -> None:
  assert 1 == 1

@pytest.mark.slow
def test_slow_test() -> None:
  assert 1 == 1


class Company:
  def __init__(self, name: str, stock_symbol: str):
    self.name = name
    self.stock_symbol = stock_symbol
  
  def __str__(self) -> str:\
    return f"{self.name} ({self.stock_symbol})"


@pytest.fixture
def company() -> Company:
  return Company("Google", "GOOG")


def test_company_name(company: Company) -> None:
  assert company.name == "Google"

@pytest.mark.parametrize(
  "company_name",
  ["Google", "Apple", "Microsoft"],
  ids=["GOOGLE TEST", "APPLE TEST", "MICROSOFT TEST"]
)
def test_parametrize(company_name: str) -> None:
  print(f"company_name: {company_name}")

def raise_covid19_expection() -> None:
  raise ValueError("COVID-19 Error")

def test_raise_covid19_exception_should_pass() -> None:
  with pytest.raises(ValueError) as e:
    raise_covid19_expection()
  assert "COVID-19 Error" == str(e.value)