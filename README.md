# ProxyFetcher

A simple Python package to fetch working proxies with filtering capabilities. Get proxies by speed, protocol (HTTP/HTTPS), and country.

## Installation

```bash
pip install proxyfetcher
```

## Quick Start

```python
from proxy_fetcher import ProxyFetcher

# Create fetcher instance
fetcher = ProxyFetcher()

# Get 5 fastest proxies
fast_proxies = fetcher.get_fast_proxies()
print(fast_proxies)
# ['ip1:port1', 'ip2:port2', ...]

# Get HTTP/HTTPS proxies
http_proxies = fetcher.get_http_proxies()
https_proxies = fetcher.get_https_proxies()

# Get proxies by country
us_proxies = fetcher.get_country_proxies('US')  # United States
uk_proxies = fetcher.get_country_proxies('UK')  # United Kingdom (both 'UK' and 'GB' work)

# Get fast HTTPS proxies from specific country
fast_us_https = fetcher.get_country_proxies(
    country_code='US',
    max_speed_ms=1000,  # Speed < 1000ms
    protocol='https'
)
```

## Features

- Get proxies in simple ip:port format
- Filter by protocol (HTTP/HTTPS)
- Filter by country (using country codes)
- Filter by speed (in milliseconds)
- Get fastest working proxies
- Combine multiple filters

## API Reference

### `ProxyFetcher()`
Create a new ProxyFetcher instance.

### `get_proxies(max_speed_ms: Optional[int] = None, country: Optional[str] = None, protocol: Optional[str] = None) -> List[str]`
Get list of proxies with optional filters.
- `max_speed_ms`: Maximum allowed speed in milliseconds
- `country`: Country code (e.g., 'US', 'UK')
- `protocol`: Protocol filter ('http' or 'https')
- Returns: List of proxy strings in ip:port format

### `get_fast_proxies(limit: int = 5, protocol: Optional[str] = None) -> List[str]`
Get fastest working proxies.
- `limit`: Number of proxies to return (default: 5)
- `protocol`: Optional protocol filter
- Returns: List of fastest proxy strings

### `get_http_proxies(max_speed_ms: Optional[int] = None) -> List[str]`
Get HTTP proxies.
- `max_speed_ms`: Optional speed filter
- Returns: List of HTTP proxy strings

### `get_https_proxies(max_speed_ms: Optional[int] = None) -> List[str]`
Get HTTPS proxies.
- `max_speed_ms`: Optional speed filter
- Returns: List of HTTPS proxy strings

### `get_country_proxies(country_code: str, max_speed_ms: Optional[int] = None, protocol: Optional[str] = None) -> List[str]`
Get proxies from specific country.
- `country_code`: Country code (e.g., 'US', 'UK')
- `max_speed_ms`: Optional speed filter
- `protocol`: Optional protocol filter
- Returns: List of proxy strings from specified country

## Example Usage in Projects

### With Requests
```python
import requests
from proxy_fetcher import ProxyFetcher

fetcher = ProxyFetcher()
proxies = fetcher.get_fast_proxies()

for proxy in proxies:
    proxy_dict = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }
    try:
        response = requests.get('http://example.com', proxies=proxy_dict)
        print(f'Success with proxy: {proxy}')
        break
    except:
        continue
```

### With Selenium
```python
from selenium import webdriver
from proxy_fetcher import ProxyFetcher

fetcher = ProxyFetcher()
proxy = fetcher.get_https_proxies(max_speed_ms=1000)[0]

options = webdriver.ChromeOptions()
options.add_argument(f'--proxy-server={proxy}')
driver = webdriver.Chrome(options=options)
```

### With aiohttp
```python
import aiohttp
from proxy_fetcher import ProxyFetcher

async def main():
    fetcher = ProxyFetcher()
    proxy = fetcher.get_fast_proxies(limit=1)[0]
    
    async with aiohttp.ClientSession() as session:
        async with session.get('http://example.com', proxy=f'http://{proxy}') as response:
            html = await response.text()
```

## Development

### Setting up development environment
```bash
# Clone the repository
git clone https://github.com/proxyfetcher/proxyfetcher.git
cd proxyfetcher

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running tests
```bash
python test.py
```

### Building and publishing to PyPI
```bash
# Build the package
python setup.py sdist bdist_wheel

# Upload to PyPI
twine upload dist/*
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
