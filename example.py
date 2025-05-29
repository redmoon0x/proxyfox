import proxyfox
import time

def main():
    # Get a single proxy
    print("\n1. Get a single proxy:")
    proxy = proxyfox.get_one()
    print(f"Single proxy: {proxy}")

    # Get a single proxy with filters
    print("\n2. Get a single HTTPS proxy from US:")
    proxy = proxyfox.get_one(protocol='https', country='US')
    print(f"US HTTPS proxy: {proxy}")

    # Get multiple proxies
    print("\n3. Get 3 proxies:")
    proxies = proxyfox.get(3)
    print("Three proxies:")
    for proxy in proxies:
        print(f"- {proxy}")

    # Get filtered multiple proxies
    print("\n4. Get 2 fast proxies (speed < 1000ms):")
    proxies = proxyfox.get(2, max_speed_ms=1000)
    print("Fast proxies:")
    for proxy in proxies:
        print(f"- {proxy}")

    # Create an auto-updating proxy pool
    print("\n5. Using auto-updating proxy pool:")
    pool = proxyfox.create_pool(size=5, refresh_interval=10)  # Update every 10 seconds for demo
    
    # Get proxies from pool
    print("Initial proxies in pool:")
    for proxy in pool.all():
        print(f"- {proxy}")
    
    print("\nGetting individual proxies from pool:")
    for _ in range(3):
        proxy = pool.get()
        print(f"Got proxy: {proxy}")

    # Wait for pool to update
    print("\nWaiting 12 seconds for pool to update...")
    time.sleep(12)
    
    print("\nUpdated proxies in pool:")
    for proxy in pool.all():
        print(f"- {proxy}")

if __name__ == "__main__":
    main()
