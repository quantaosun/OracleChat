
# Is 20 USD too expensive for you, but still need to use more than free tier of Chatgpt ? 

This repo demonstrate how to set up a chat bot from your local terminal (Mac/Linux) with openai 3.5 model, you still need to pay for to openai to get chat quotes but it is generally much cheapter compared to the monthly subscription if you are not a heavy user. The openai api will be wrapped in the flask app builder in a remote Oracle free tier server (or locally).

<img width="511" alt="image" src="https://github.com/user-attachments/assets/211c2e75-cdc3-4f19-85c3-40b35ee9ebd1">


## Step 0: (optional) get a free VPS, my choice is Oracle Free Tier 
Instance access
```
You connect to a running Linux instance using a Secure Shell (SSH) connection. You'll need the private key from the SSH key pair that was used to create the instance.
Public IP address:
 1**.1**.1**.2** 
Username:
 ubuntu
```
You will get a key file when setting up your remote server, something like ```ssh-key-2024-09-09.key```

### If you don't want to use remote server, you can proceed with your Mac/Linx, no Windows tutorial here, it is also possible but not introduced here.

## Step 1 Set Up a Virtual Environment
### Create a project directory
```
mkdir my_chatbot
cd my_chatbot
```
### Create a Python virtual environment
```
python3 -m venv venv
```

### Activate the virtual environment

```
source venv/bin/activate
```


## Step 2: Install python 3, flask and open-ai

```
# Install Flask for creating the web application
pip install flask

# Install OpenAI to interact with GPT models
pip install openai

# Install colorama for colored output in the terminal (optional for enhanced interaction)
pip install colorama

```
## Step3. Create the app.py Script
```
import os
import openai
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Load the OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_gpt():
    print(Fore.CYAN + "Chat with GPT-3.5. Type 'exit' to stop.")

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

        # Send the conversation to OpenAI GPT-3.5
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
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
                                                                                                                                                             1,1           Top
```
## Step 4. Set Your OpenAI API Key

You need to set your OpenAI API key as an environment variable for the chatbot to interact with the GPT models.

Add this line to your ```~/.bashrc``` 

## Step5. Run the Chatbot
Now, you can run your chatbot and start interacting with GPT-3.5 directly from the command line.

```
python app.py

```
## Step6. Automatically Activate the Virtual Environment
If you want the virtual environment to activate automatically every time you log into the server or open a new shell, you can add the following line to your ```~/.bashrc```

Add these lines to the end of the file, change the path if yours is different

```
source ~/my_chatbot/venv/bin/activate
cd /home/ubuntu/my_chatbot
# start flask app 
python app.py
```
restart the shell or close and reopen

```
source ~/my_chatbot/venv/bin/activate
```
## Step 7 (optional) Only when you use remote server
```
ssh -i ssh-key-2024-09-09.key ubuntu@ 1**.1**.1**.2** 
```
Since we have added ```python app.py``` to the end of ```~/.bashrc```, as long as you can connect to Oracle, it will enter the chatbot by default.
