from proxy_fetcher import ProxyFetcher

def main():
    # Create a fetcher instance
    fetcher = ProxyFetcher()
    
    # Get 5 fastest proxies
    print("\n=== Fast Proxies ===")
    fast_proxies = fetcher.get_fast_proxies()
    for proxy in fast_proxies:
        print(proxy)
    
    # Get HTTP proxies
    print("\n=== HTTP Proxies ===")
    http_proxies = fetcher.get_http_proxies(max_speed_ms=1000)  # Fast HTTP proxies
    for proxy in http_proxies[:5]:  # Show first 5
        print(proxy)
    
    # Get HTTPS proxies
    print("\n=== HTTPS Proxies ===")
    https_proxies = fetcher.get_https_proxies(max_speed_ms=1000)  # Fast HTTPS proxies
    for proxy in https_proxies[:5]:  # Show first 5
        print(proxy)
    
    # Get US proxies
    print("\n=== US Proxies ===")
    us_proxies = fetcher.get_country_proxies('US')
    for proxy in us_proxies[:5]:  # Show first 5
        print(proxy)
    
    # Get fast HTTPS proxies from specific country
    print("\n=== Fast HTTPS Proxies from United Kingdom ===")
    uk_https_proxies = fetcher.get_country_proxies('GB', 
                                                 max_speed_ms=1000, 
                                                 protocol='https')
    for proxy in uk_https_proxies[:5]:  # Show first 5
        print(proxy)

if __name__ == "__main__":
    print("ProxyFetcher Demo")
    print("=" * 30)
    main()
