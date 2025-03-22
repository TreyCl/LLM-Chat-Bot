# LLM-Chat-Bot

This project implements a simple Python chatbot using the **Ollama** library. The chatbot interacts with the user and generates responses based on context parameters. It allows the user to engage in a conversation while ensuring concise and structured responses. The user can exit the program by typing the "exit" keyword.

## Features

- **Integration with Ollama**: Leverages the `chat` function from the Ollama library to generate AI-based responses.
- **Contextual Responses**: The conversation is guided by specific context parameters (e.g., limiting responses to 50 words).
- **Exit Command**: The program exits when the user types the specified escape word. The default example escape word is **'exit'**.
- **Simple User Input Loop**: Continuously accepts input from the user until the exit command is triggered.

### Prerequisites

To utilize this application, you must install **Python**, **Ollama**, and **pull the model** you wish to use. The example model in use is **llama3.2:latest**.
