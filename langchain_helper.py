from dotenv import load_dotenv
import os
load_dotenv()

# Verify the API key is loaded (for debugging, remove in production)
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found in environment variables")


from langchain_openai import OpenAI
llm = OpenAI(temperature=0.6)

from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
from langchain.chains import LLMChain

def generate_restaurant_name_and_menu_items(cusine):
    prompt_template_name = PromptTemplate(
        input_variables=["cuisine"],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for it.",
    )

    prompt_template_menu = PromptTemplate(
        input_variables=["restaurant_name"],
        template="""Suggest a menu for {restaurant_name}. Return the menu items as a comma separated list."""
    )

    # Create LLMChains from the prompt templates
    name_chain = LLMChain(
        llm=llm,
        prompt=prompt_template_name,
        output_key="restaurant_name"
    )

    menu_chain = LLMChain(
        llm=llm,
        prompt=prompt_template_menu,
        output_key="menu_items"
    )

    # Update the SequentialChain to use the LLMChains
    chain = SequentialChain(
        chains=[name_chain, menu_chain],
        input_variables=["cuisine"],
        output_variables=["restaurant_name", "menu_items"],
    )

    return chain({"cuisine": cusine})