import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from urllib.parse import urljoin

PIP_USER_AGENT = "pipr (https://worldbank.github.io/pypip/)"

def build_request(base_url = "https://api.worldbank.org", 
                  api_handle = "pip/v1", 
                  endpoint = "pip", 
                  **kwargs):
    """
    Build an HTTP request.
    
    Parameters:
    - server (str): Server. For WB internal use only.
    - api_version (str): API version.
    - endpoint (str): PIP API endpoint.
    - **kwargs: Additional parameters to be passed as query parameters.
    
    Returns:
    - requests.Response: A response object from the `requests` library.
    """
    
    #base_url = select_base_url(server)
    
    # Fix params using a hypothetical fix_params function
    params = {k: fix_params(v) for k, v in kwargs.items()}
    
    # Construct the URL
    url = urljoin(base_url, f"{api_handle}/{endpoint}")

    # Create headers
    headers = {
        "User-Agent": PIP_USER_AGENT
    }

    # Prepare the request
    req = requests.Request('GET', url, params=params, headers=headers)
    prepared_req = req.prepare()
    
    return prepared_req
    
    # Set up retry mechanism
    # retry_strategy = Retry(
    #     total=3,  # Number of retries
    #     status_forcelist=[429, 500, 502, 503, 504],  # Status codes to retry on
    #     method_whitelist=["HEAD", "GET", "OPTIONS", "POST"],  # HTTP methods to retry
    #     backoff_factor=1  # Delay factor (in seconds)
    # )
    # adapter = HTTPAdapter(max_retries=retry_strategy)
    # session = requests.Session()
    # session.mount("http://", adapter)
    # session.mount("https://", adapter)
    
    
    
    # response = session.get(url, params=params, headers=headers)
    
    # Handle errors (assuming parse_error_body is a function to handle error responses)
    # if response.status_code != 200:
    #     parse_error_body(response)
    
    # return response

# Example usage:
# response = build_request("server_name", "v1", "some_endpoint", param1="value1", param2="value2")

def fix_params(param):
    """
    Convert a list or tuple of parameters into a comma-separated string.
    
    Parameters:
    - param (list or tuple): The parameter to be processed.
    
    Returns:
    - str or original type: A comma-separated string if param has more than one element, otherwise the original param.
    """
    if isinstance(param, (list, tuple)) and len(param) > 1:
        return ",".join(map(str, param))
    else:
        return param