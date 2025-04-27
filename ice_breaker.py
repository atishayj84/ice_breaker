from langchain_ollama import ChatOllama
from langchain.prompts.prompt import PromptTemplate
from langchain_core.output_parsers.string import StrOutputParser
from scraping_packages.linkedin import scrape_linkedin_profile
from dotenv import load_dotenv
from agents.linkedin_lookup_agents import lookup
load_dotenv()

def ice_breaker_with(name = "", mock=True):
    llm = ChatOllama(
        model="llama3",
        temperature=0)

    print("Hello icebreaker")

    summary_template = """
    given the linkedin information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    url = lookup(name)
    linkedin_information = scrape_linkedin_profile(url, mock)

    chain = summary_prompt_template | llm | StrOutputParser()
    res = chain.invoke(input={"information": linkedin_information})

    print(res)


if __name__ == '__main__':
    ice_breaker_with('Atishay Jain American Express', False)