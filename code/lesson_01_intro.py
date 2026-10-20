"""Lesson 1.4: Ask Ollama for business AI solutions."""

from ollama import chat

# Collect details so the AI can tailor its suggestions.
name = input("Enter your name: ")
business = input("Enter your business type: ")
problem = input("What problem does your business face? ")

# Build a clear prompt from the user's answers.
prompt = (
    f"Suggest 3 practical AI solutions for a {business} "
    f"that struggles with {problem}. Explain each briefly."
    "Don't ask any questions, just provide the solutions."
)

print(f"\nWelcome, {name}!")
print("\nAsking AI for solutions...")

# Ask the selected Ollama model to generate an answer.
response = chat(
    model="gemma3:1b",
    messages=[
        {"role": "user", "content": prompt}
    ],
)

print("\n--- AI Solutions ---")
print(response.message.content)