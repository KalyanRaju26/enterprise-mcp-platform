from confluence_client import ConfluenceClient
client = ConfluenceClient()

# spaces list
print("\nSPACES_LIST")
print(client.list_spaces())

# get pages
print("\nPAGE_WITH_ID")
page = client.get_page("360449")
print(page["title"])
print(page["content"])

# search pages
print("\nSEARCH_PAGES")
result = client.search_pages("Order Service Architecture")
print(result)

# search content
print("\nSEARCH_CONTENT")
result = client.search_content("order")
print(result)