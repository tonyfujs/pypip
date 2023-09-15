import requests as req

def health_check():
    """Check that the API is live"""
    r = req.get('https://api.worldbank.org/pip/v1/health-check')
    out = r.json()
    return out