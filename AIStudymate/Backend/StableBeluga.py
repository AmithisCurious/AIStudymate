import gradio as gr
from transformers import pipeline
import torch
from collections import deque

print("CUDA available:", torch.cuda.is_available())
print("Number of GPUs available:", torch.cuda.device_count())


system_prompt = """### System:
Please act as a teacher and guide for my learning. Whenever I ask a question, instead of giving a direct answer, please provide hints, walk me through the problem-solving process, or offer clues that will help me think critically and arrive at the solution on my own. The goal is to help me develop problem-solving skills and deepen my understanding. 

User Prompt: """


pipe = pipeline("text-generation", model="google/gemma-2-2b-it", device=0)


history = deque(maxlen=4)

def generate_response(user_prompt):
    history.append(f"User Prompt: {user_prompt}")

    history_prompt = "\n".join(history)
    combined_prompt = f"{system_prompt}\n{history_prompt}"

    response = pipe(combined_prompt, max_new_tokens=512, do_sample=True, top_p=0.95)

    generated_text = response[0]['generated_text']
    def extract_teacher_response(text):
        marker = user_prompt
        if marker in text:
            return text.split(marker, 1)[1].strip()
        return text.strip()
    res = extract_teacher_response(generated_text)
    history.append(f"**Teacher:** {res}")
    return res

interface = gr.Interface(
    fn=generate_response,
    inputs="text",
    outputs="text",
    title="AI Teacher with Memory",
    description="Ask a question and receive hints or guidance with memory of the last 4 interactions.",
)

interface.launch(share=True)
