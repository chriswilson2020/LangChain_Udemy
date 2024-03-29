import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

if __name__ == "__main__":
    # print("hello LangChain!")
    summary_template = """
        given the LinkedIn information {information} about a person from I want I want you to create:
        1. a short summary
        2. two interesting facts about them
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_profile_url = linkedin_lookup_agent(name="Christopher Wilson", company="NovioSense")
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url['output'])
    # print(linkedin_data)
    # print(linkedin_data)

    output = chain.invoke(input={"information": linkedin_data})

    print(output["text"])
