# Chatbot with OpenAI and Gradio

This repository contains a Python script (`chat_bot.py`) that implements a chatbot.
- It uses the OpenAI API with the GPT-3.5-turbo model to generate responses.
- It uses the Gradio library to create a simple web interface for interacting with the chatbot.

## Dependencies

The script requires the following Python libraries:

- `openai`: For interacting with the OpenAI API.
- `gradio`: For creating the web interface.

## Setup

1.  **Install dependencies:**
    You can install the required libraries using pip:
    ```bash
    pip install openai gradio
    ```

2.  **Set OpenAI API Key:**
    Open the `chat_bot.py` script and replace the placeholder value of the `api_key` variable with your actual OpenAI API key:
    ```python
    api_key = "YOUR_OPENAI_API_KEY" # Provide OpenAI API key here
    ```
    **Important:** Keep your API key confidential. Do not commit it directly to your repository if it's public.

## Running the Script

Once you have installed the dependencies and set up your API key, you can run the chatbot:

```bash
python chat_bot.py
```

This will launch a Gradio interface in your web browser (or provide a public link if `share=True` is enabled) where you can interact with the chatbot.

## Code Structure

A brief overview of the `chat_bot.py` script:

-   `from openai import OpenAI`: Imports the necessary class from the OpenAI library.
-   `import gradio`: Imports the Gradio library.
-   `client = OpenAI()`: Initializes the OpenAI client. You might need to pass your API key here if not configured globally, e.g., `client = OpenAI(api_key="YOUR_API_KEY")`. (Note: The provided script sets `api_key` in a separate variable, which isn't directly used by `OpenAI()` constructor in the current script version. This section of the README describes common practice, the script itself would need modification to use the `api_key` variable with the `OpenAI()` constructor).
-   `api_key = "*************************"`: A placeholder variable where your OpenAI API key should be inserted. **Important: The current script does not directly use this `api_key` variable when creating the `OpenAI` client. For the API key to be used, the client initialization should be `client = OpenAI(api_key=api_key)`.**
-   `messages = [{"role": "system", "content": "You are a programmer"}]`: Initializes a list called `messages`. This list stores the conversation history between the user and the chatbot. It starts with a system message that sets the context for the chatbot (e.g., telling it to act as a programmer).
-   `CustomChatGPT(user_input)`: This function is the core of the chatbot.
    -   It takes `user_input` (the text typed by the user) as an argument.
    -   Appends the user's message to the `messages` list.
    -   Sends the entire conversation history (`messages`) to the OpenAI API using `OpenAI.chat.completions.create()`, specifying the `gpt-3.5-turbo` model.
    -   Retrieves the chatbot's reply from the API response.
    -   Appends the chatbot's reply to the `messages` list.
    -   Returns the chatbot's reply to be displayed in the interface.
-   `demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="I'm a programmer")`: This line creates the Gradio web interface.
    -   `fn=CustomChatGPT`: Specifies that the `CustomChatGPT` function should be called when the user interacts with the interface.
    -   `inputs="text"`: Defines the input field as a textbox.
    -   `outputs="text"`: Defines the output display as text.
    -   `title="I'm a programmer"`: Sets the title of the web interface.
-   `demo.launch(share=True)`: Starts the Gradio application.
    -   `share=True`: If set to `True`, Gradio attempts to create a public, shareable link to your interface. This is useful for temporary sharing but be mindful of security and API key usage. If `False` or omitted, it usually runs on a local server.
