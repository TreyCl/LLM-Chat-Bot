from ollama import chat
import sys

contextParameters = " Do not use more than 50 words."  #Example text used for framing the model context
contextKey = "(Do not refer to the text in these parentheses when responding to the user." + contextParameters + ")"  #Reframes parameter prompts when refering to contextParameters
escapeWord = "exit" #Used to break the program loop
userRole = "user" #Defines the users role for prompting
llmModel = "llama3.2:latest"


while True:

    #Combines user input with context parameters to dictate conversational cadence and formality
    content = input("You: ") + contextKey

    #Checks input to see if it matches the escapeWord. If True, the program breaks the loop and exits; if False, the program proceeds as normal
    if content == escapeWord + contextKey:
        break
    else:
        response = chat(model= llmModel, messages=[{"role": userRole, "content": content}])
        print(response['message']['content'])

sys.exit(0)
