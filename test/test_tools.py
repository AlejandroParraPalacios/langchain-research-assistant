from datetime import datetime
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool  # BaseTool

def save_to_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding = "utf-8") as f:
        f.write(formatted_text)
        
    return f"Data successfully saved to {filename}"

save_tool = Tool(
    name = "save_text_to_file",
    func = save_to_txt,
    description = "Saves structured research data to a text file.",
)

# Search tool (valid BaseTool)
search_tool = DuckDuckGoSearchRun()

# Spanish Wikipedia
_api = WikipediaAPIWrapper(top_k_results=3, lang="es", doc_content_chars_max=4000)
wiki_tool = WikipediaQueryRun(api_wrapper=_api)