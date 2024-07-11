from crewai_tools import tool


class Tools_handler():
    def search():

        @tool("Duck_Duck_Go_Search")
        def ddgsearch(query: str) -> str:
            """Searching for information on the Internet.
            :param query: string, information that needs to be found on the Internet

                example:
            {
                "query": "Why the sky is blue?",
            }
            """
            from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
            from langchain_community.tools import DuckDuckGoSearchResults

            wrapper = DuckDuckGoSearchAPIWrapper(region="wt-wt", time="d", max_results=7)
            search = DuckDuckGoSearchResults(api_wrapper=wrapper)

            return search.run(query)

        return ddgsearch


    def search_for_imahes():

        @tool("Duck_Duck_Go_Search_For_Images")
        def ddgsearch_for_images(query: str) -> str:
            """Searching for images on the Internet.
            :param query: string, information about what image needs to be found on the Internet

                example:
            {
                "query": "butterfly",
            }

            """
            from duckduckgo_search import DDGS
            result = DDGS().images(
                keywords=query,
                safesearch="off",
                max_results=1,
            )

            return result[0]['image']

        return ddgsearch_for_images