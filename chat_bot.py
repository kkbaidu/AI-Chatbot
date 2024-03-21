from openai import OpenAI
import gradio 

client = OpenAI()

api_key = "*************************" #Provide OpenAI API key here

messages = [{"role": "system", "content": "You are a programmer"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = OpenAI.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="I'm a programmer")

demo.launch(share=True)