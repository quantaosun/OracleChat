import os
import openai
from colorama import Fore, Style, init

# Initialize colorama for colored output
init(autoreset=True)

# Load the OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_gpt():
    print(Fore.CYAN + "Chat with GPT-4. Type 'exit' to stop.")

    # Store the conversation
    conversation = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    while True:
        # Get user input from the command line, colored yellow
        user_message = input(Fore.YELLOW + "You: ")

        # Exit condition
        if user_message.lower() == "exit":
            print(Fore.CYAN + "Exiting the chat.")
            break

        # Add user message to the conversation
        conversation.append({"role": "user", "content": user_message})

        # Send the conversation to OpenAI GPT-4
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=conversation
            )

            # Get the assistant's reply, colored green
            assistant_reply = response['choices'][0]['message']['content']
            print(Fore.GREEN + f"Assistant: {assistant_reply}")

            # Add the assistant's reply to the conversation
            conversation.append({"role": "assistant", "content": assistant_reply})

        except Exception as e:
            print(Fore.RED + f"Error: {str(e)}")

if __name__ == "__main__":
"app-4.0.py" 50L, 1553C                                                                                                                                      1,1           Top
