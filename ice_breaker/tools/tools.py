from langchain.serpapi import SerpAPIWrapper


def get_profile_url(name: str):
    """Searches for a LinkedIn Profile Page."""
    search = SerpAPIWrapper()
    res = search.run(f"{name}")
    return res
