
import gradio as gr
import gradio_resources

from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama',  # Using your API key placeholder
)

models = ["llama3.1:70b", "llama3:70b", "gemma:2b", "bgGPT:Q4"]


def predict(message, history, system_prompt, model):

    conversation = []

    system_prompt = system_prompt.strip()

    if len(system_prompt) > 0:
        conversation.append({"role": "system", "content": system_prompt})

    for human, assistant in history:
        conversation.append({"role": "user", "content": human })
        conversation.append({"role": "assistant", "content": assistant})

    conversation.append({"role": "user", "content": message})

    print(conversation)

    stream = client.chat.completions.create(
        model=model,
        messages=conversation,
        stream=True
    )

    partial_message = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
              partial_message = partial_message + chunk.choices[0].delta.content
              yield partial_message


demo = gr.ChatInterface(
    fn=predict,
    additional_inputs=[
        gr.Textbox("", label="System Prompt"),
        gr.Dropdown(
            models,
            value=models[0],
            multiselect=False,
            label="Model"
        )
    ],
    title="&#129433; Llama Local",
    head=gradio_resources.head(),
    js='() => { document.title = "Llama Local"; }',
    theme="monochrome",
    submit_btn="Send",
    retry_btn="Regenerate",
    show_progress='full',
    concurrency_limit=3,
    fill_height=True,
    autofocus=True
)


if __name__ == "__main__":
    print("Starting Llama Local...")
    demo.queue().launch(server_name="0.0.0.0", server_port=7860)
