def api_get_request(req_lib, url: str, payload: dict):
    try:
        response = req_lib.get(url, params=payload)
        if response.status_code == req_lib.codes.ok:
            return response.json(), response.status_code
    except Exception as e:
            return f'Request failed!: {e}', None
    return None, response.status_code

target_url = 'https://rickandmortyapi.com/api/charactr/'
payload = {'name': 'Rick', 'status': 'alive'}