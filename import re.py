import re

class AdBlocker:
    def __init__(self):
        # Regular expressions to match URLs of ad servers
        self.ad_domains = [
            r"doubleclick\.net",
            r"googleadservices\.com",
            r"ad\.example\.com"  # Add more ad domains as needed
        ]
        self.ad_pattern = "|".join(self.ad_domains)

    def is_ad(self, url):
        # Check if the URL matches any of the ad domain patterns
        return re.search(self.ad_pattern, url) is not None

# Example usage
if __name__ == "__main__":
    ad_blocker = AdBlocker()
    test_urls = [
        "https://example.com/page",
        "https://doubleclick.net/ad_banner",
        "https://example.com/content"
    ]
    for url in test_urls:
        if ad_blocker.is_ad(url):
            print(f"{url} is an ad.")
        else:
            print(f"{url} is not an ad.")