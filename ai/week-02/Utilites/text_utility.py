text = """
Agentic AI helps build intelligent systems.
Python is useful for automation and data processing.
Comprehensions make code shorter and easier to read.
"""

words=text.split()
preview=words[:5]
summary=" ".join(words[:6])

word_length=len(words)
print(f"Total Words: {word_length}")
print(f"First five words: {preview}")
print(f"Summary : {summary}")
