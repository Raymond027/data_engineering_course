from unittest.mock import patch

from etl.extract import extract_crypto_data


@patch("etl.extract.requests.get")
def test_extract(mock_get):

    mock_get.return_value.json.return_value = []

    mock_get.return_value.raise_for_status.return_value = None

    result = extract_crypto_data()

    assert result is not None