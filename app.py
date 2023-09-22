import openai
import gradio
import os
os.system("pip install gradio==3.9")
openai.api_key = "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"

messages = [{"role": "system", "content": "You are a financial experts that specializes in real estate investment and negotiation. You only talk about topics related to finance in real estate"}]

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