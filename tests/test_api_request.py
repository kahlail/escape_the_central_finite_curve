from unittest.mock import Mock
from src.make_api_request import api_get_request

def test_api_request_good_response():
    mock_url = 'https://www.mock-url.com/get'
    mock_parameters = ['value 1', 'value 2']
    mock_request_lib = Mock()
    
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{
        "id": 1,
        "name": "Mock Sanchez",
        "status": "Alive",
        "species": "Human",
        "type": "",
        "gender": "Male",
    }
]
    
    mock_request_lib.get.return_value = mock_response
    mock_request_lib.codes.ok = 200

    expected_status_code = 200
    expected_response =[
    {
      "id": 1,
      "name": "Mock Sanchez",
      "status": "Alive",
      "species": "Human",
      "type": "",
      "gender": "Male",
    }
]

    actual_response, actual_stat_code = api_get_request(mock_request_lib, mock_url, mock_parameters)

    assert expected_response == actual_response
    assert expected_status_code == actual_stat_code