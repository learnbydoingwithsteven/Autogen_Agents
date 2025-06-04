import autogen

# Configure local LLM served by Ollama
config_list = [
    {
        "model": "llama2",
        "api_key": "ollama",
        "base_url": "http://localhost:11434/v1",
    }
]
llm_config = {"config_list": config_list}

assistant = autogen.AssistantAgent(name="assistant", llm_config=llm_config)
user_proxy = autogen.UserProxyAgent(name="user_proxy", human_input_mode="NEVER")

task = "Plan data collection methods for a study."

if __name__ == "__main__":
    user_proxy.initiate_chat(assistant, message=task)
