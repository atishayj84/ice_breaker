from langchain_community.tools.tavily_search import TavilySearchResults
from pprint import pprint
def get_profile_url_tavily(query: str):
    """ Searches for Linkedin or Twitter profile pages, search for specific domains using include_domains argument"""
    search = TavilySearchResults()

    res = search.run((f"{query}"))
    return res

pprint(get_profile_url_tavily('Atishay Jain'))