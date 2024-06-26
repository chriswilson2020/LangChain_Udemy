import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parsers import person_intel_parser, PersonIntel

name = "Harrison Chase"


def ice_break(name: str) -> tuple[PersonIntel, str]:
    linkedin_profile_url = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_profile_url["output"]
    )

    summary_template = """
        given the LinkedIn information {information} about a person from I want I want you to create:
        1. a short summary
        2. two interesting facts about them
        \n{format_instructions}
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": person_intel_parser.get_format_instructions()
        },
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    output = chain.invoke(input={"information": linkedin_data})

    print(output["text"])
    return person_intel_parser.parse(output["text"]), linkedin_data.get(
        "profile_pic_url"
    )


if __name__ == "__main__":
    # print("hello LangChain!")
    ice_break(name="Harrison Chase")
