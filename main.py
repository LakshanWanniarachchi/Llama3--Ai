from llama_index.llms.ollama import Ollama

llm = Ollama(model="llama3" , request_timeout=5000.0)

result = llm.complete("Give me a flask code")

print(result)