def api_get_request(req_lib, url: str, params: list):
    try:
        response = req_lib.get(url, params)
        if response.status_code == req_lib.codes.ok:
            return response.json(), response.status_code
    except Exception as e:
            return f'Request failed!: {e}', response.status_code
    return None, None

