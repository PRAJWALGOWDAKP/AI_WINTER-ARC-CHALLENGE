
import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")

prompt = "Explain context window, temperature, and top-p."

tokens = encoding.encode(prompt)

print("Prompt:", prompt)
print("Total tokens:", len(tokens))

print("\nToken IDs:")
print(tokens)

print("\nIndividual tokens:")
for token_id in tokens:
    token_text = encoding.decode([token_id])
    print(f"ID: {token_id:<8} Token: {repr(token_text)}")
