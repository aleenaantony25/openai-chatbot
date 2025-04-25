import openai

# Set your OpenAI API key
openai.api_key = "sk-..."  # Replace with your actual API key

# Function to send a prompt to the ChatGPT model
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Using GPT-3.5 Turbo model
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message["content"].strip()

# Main loop to keep the conversation going
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "bye", "exit"]:
            print("ChatGPT: Goodbye!")
            break
        response = chat_with_gpt(user_input)
        print("ChatGPT:", response)