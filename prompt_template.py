from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

email_prompt_template = PromptTemplate(
    input_variable=["tone", "recipient", "subject"],
    template="""
You are a helpful email assistant. 
Your task is to write an email in a {tone} tone to the {recipient} about the {subject}
""",
)


model = ChatOpenAI(model="gpt-4o-mini")
chain = email_prompt_template | model

response = chain.invoke(
    {
        "tone": "professional",
        "recipient": "John Doe",
        "subject": "Meeting",
    }
)

print(response.content)
