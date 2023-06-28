def api_get_request(req_lib, url: str, params: list):
    response = req_lib.get(url, params)
    response = response.json()
    status = response.status_code
    return response, status

