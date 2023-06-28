from unittest.mock import Mock
from src.make_api_request import api_get_request

def test_api_request_good_response():
    mock_url = 'https://www.mock-url.com/get'
    mock_parameters = ['value 1', 'value 2']
    mock_request_lib = Mock()
    mock_request_lib.get.return_value = Mock()
    mock_request_lib.get.return_value.status_value.return_value = 200
    mock_request_lib.get.return_value.json.return_value = {
      "id": 1,
      "name": "Mock Sanchez",
      "status": "Alive",
      "species": "Human",
      "type": "",
      "gender": "Male",
    }


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
    expected_status_code = 200
    
    true_response, true_stat_code = api_get_request(mock_request_lib, mock_url, mock_parameters)
    
    
    assert expected_response == true_response
    assert expected_status_code == true_stat_code