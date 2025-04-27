from langchain_ollama import ChatOllama
from langchain import hub
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import AgentExecutor, create_react_agent
from tools.tools import get_profile_url_tavily
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults


load_dotenv()
tavily_search = TavilySearchResults()


def lookup(name: str) -> str:
    llm = ChatOllama(model="llama3", temperature=0)

    template = """ 
    Given the full name {name}, Get me link to their linkedin profile page only. Your answer should only contain the URL, end when URL is found
    """

    prompt = PromptTemplate(template = template, input_variables=['name'])

    # tools = [Tool(name = 'Googler for linkedin',
    #              func = get_profile_url_tavily,
    #              description= 'useful for when you need to get the Linkedin page URL'
    # )]
    tools = [Tool(name = 'Googler for linkedin',
                 func = tavily_search,
                 description= 'useful for when you need to search online, use include_domain argument to search for specific domains'
    )]
    react_prompt = hub.pull('hwchase17/react')
    agent = create_react_agent(llm=llm, tools=tools, prompt = react_prompt)

    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose = True, handle_parsing_errors="Check your output and make sure it conforms, use the Action/Action Input syntax") 

    result = agent_executor.invoke(input={'input': prompt.format_prompt(name=name)})

    url = result['output']




print(lookup('Atishay Jain American Express'))




