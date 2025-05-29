from proxy_fetcher import ProxyFetcher
import time

def test_proxy_fetcher():
    print("Testing ProxyFetcher...")
    fetcher = ProxyFetcher()
    
    tests = [
        ("Fast Proxies (speed < 1000ms)", 
         lambda: fetcher.get_proxies(max_speed_ms=1000)),
        
        ("HTTP Proxies", 
         lambda: fetcher.get_http_proxies()),
        
        ("HTTPS Proxies", 
         lambda: fetcher.get_https_proxies()),
        
        ("US Proxies", 
         lambda: fetcher.get_country_proxies('US')),
        
        ("Fast HTTPS US Proxies", 
         lambda: fetcher.get_country_proxies('US', max_speed_ms=1000, protocol='https')),
        
        ("UK Proxies (using country code 'GB')", 
         lambda: fetcher.get_country_proxies('GB')),
        
        ("UK Proxies (using country code 'UK')", 
         lambda: fetcher.get_country_proxies('UK')),
    ]
    
    for test_name, test_func in tests:
        print(f"\n=== Testing {test_name} ===")
        try:
            start_time = time.time()
            proxies = test_func()
            end_time = time.time()
            
            print(f"Found {len(proxies)} proxies in {end_time - start_time:.2f} seconds")
            print("First 3 proxies:")
            for proxy in proxies[:3]:
                print(f"- {proxy}")
                
            print("✓ Test passed")
            
        except Exception as e:
            print(f"✗ Test failed: {str(e)}")
        
        # Small delay between requests
        time.sleep(1)

if __name__ == "__main__":
    test_proxy_fetcher()
