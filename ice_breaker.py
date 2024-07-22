from os import environ
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from third_parties.linkedin import scrap_linked_profile


load_dotenv()
if __name__ == "__main__":
    OPENAI_API_KEY = environ["OPENAI_API_KEY"]
    summary_templates = """
    given the linkedin information {information} about the perfom from I want
            you to create:
    1: a short summary
    2: two interesting facts about them
    """
    summary_prmpt_template = PromptTemplate(
        input_variables=["information"], template=summary_templates
    )
    openai_llm = ChatOpenAI(
        temperature=0, model="gpt-3.5-turbo", api_key=OPENAI_API_KEY
    )
    linkedin_profile_url = environ["MY_GIST"]
    linked_data = scrap_linked_profile(
        linked_in_profile=linkedin_profile_url, mock=True
    )
    chain = summary_prmpt_template | openai_llm
    response = chain.invoke(input={"information": linked_data})
    print(f"Response : {response}")
