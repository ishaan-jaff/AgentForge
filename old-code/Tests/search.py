import agentforge.tools.google_search as google
import agentforge.tools.intelligent_chunk as smart_chunk
from agentforge.tools.web_scrape import WebScraper

web_scrape = WebScraper()

search_results = google.google_search("spaceships", 5)
url = search_results[2][0]
print(url)
scrapped = web_scrape.get_plain_text(url)
chunks = smart_chunk.intelligent_chunk(scrapped, chunk_size=0)

print(f"\nSearch Results: {search_results}")
print(f"\nURL: {url}")
print(f"\n\nChunks:\n{chunks}")


