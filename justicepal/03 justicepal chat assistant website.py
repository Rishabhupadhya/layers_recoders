import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "EMPOWERING COMMUNITIES: BRIDGING THE GAP BETWEEN PEOPLE AND THE LAW"}]

def CustomChatGPT(Enter_your_Query):
    messages.append({"role": "user", "content": Enter_your_Query})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "JusticePal")

demo.launch(share=True)