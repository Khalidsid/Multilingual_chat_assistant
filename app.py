import openai
import gradio
import os
os.system("pip install gradio==3.9")
openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

messages = [{"role": "system", "content": "Allow the user to input their query in any language you can understand. Generate 3 responses each in English, German, and Hindi using 200 words or less. Provide the word count and character count of the generated text after each language output."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Real Estate Finance helper")

demo.launch(share=True)
