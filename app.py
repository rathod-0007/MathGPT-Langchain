import streamlit as st
from langchain_groq import ChatGroq
from langchain_classic.chains import LLMMathChain, LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_classic.agents.agent_types import AgentType
from langchain_classic.agents import initialize_agent, Tool
# from dotenv import load_dotenv
from langchain_classic.callbacks import StreamlitCallbackHandler

##streamlit
st.set_page_config(page_title="LangChain MathGPT", page_icon="🤖", layout="centered")
st.title("LangChain – MathGPT using Google Gemma2")

groq_api_key = st.sidebar.text_input(label="Groq API Key", type="password")

if not groq_api_key:
    st.info("❌ Please enter your Groq API key to use the app.")
    st.stop()

llm=ChatGroq(model="groq/compound", groq_api_key=groq_api_key)

#tool initialization
wikipedia_wrapper=WikipediaAPIWrapper()
wikipedia_tool=Tool(
    name="Wikipedia",
    func=wikipedia_wrapper.run,
    description="Useful for when you need to look up a topic or get general information about something."
)

#math tool chain
math_chain=LLMMathChain.from_llm(llm=llm)
calculator=Tool(
    name="Calculator",
    func=math_chain.run,
    description="Useful for when you need to perform calculations or solve mathematical problems."
)

prompt="""
You are MathGPT, an AI designed to assist with mathematical problems.
Display all your calculations step-by-step.
Question:{question}
Answer:
"""

prompt_template=PromptTemplate(
    input_variables=["question"],
    template=prompt
)

#combine all tools into chain
chain=LLMChain(llm=llm,prompt=prompt_template)

reasoning_tool=Tool(
    name="Reasoning Tool",
    func=chain.run,
    description="Useful for when you need to reason through a problem step-by-step."
)

#intialise agents
assistant_agent=initialize_agent(
    tools=[wikipedia_tool, calculator, reasoning_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
)

if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"assistant","content":"Hello! I am MathGPT, your AI assistant for mathematical problems. How can I help you today?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])


#ineraction
question=st.text_area("Enter your mathematical question here...", "I have 5 apples and I buy 3 more. How many apples do I have now?")

if st.button("Find Answer"):
    if question:
        with st.spinner("Generate Response"):
            st.session_state.messages.append({"role":"user","content":question})
            st.chat_message("user").write(question)

            st_cb=StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            response=assistant_agent.run(st.session_state.messages, callbacks=[st_cb])

            st.session_state.messages.append({"role":"assistant","content":response})
            st.write("### Response")
            st.success(response)

    else:
        st.warning("❌ Please enter a mathematical question to proceed.")