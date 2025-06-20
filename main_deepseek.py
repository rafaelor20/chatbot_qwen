from transformers import pipeline
import torch
from sty import fg

# Verifica GPU disponível
if torch.cuda.is_available():
    device = -1  # GPU ID
else:
    device = -1  # CPU

# pipeline
pipe = pipeline(
    "text-generation",
    "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
    device=device  # ajustado!
)

def ask_question(message):
    try:
        # Ajuste: Reduzi o max_new_tokens para evitar OOM
        response = pipe(
            message,
            max_new_tokens=256
        )
        
        generated_text = response[0]['generated_text']
        # Ajuste: verificar se </think> existe
        if "</think>" in generated_text:
            think, say = generated_text.split("</think>")
            think = think.replace("<think>", "").strip()
            say = say.strip()
        else:
            think = "No <think> tag found"
            say = generated_text.strip()
        
        # display thinking in green
        print(fg.green + think + fg.rs)
        # display response in yellow
        print("\n" + fg.yellow + say + fg.rs)
    
    except torch.cuda.OutOfMemoryError as e:
        print(fg.red + f"⚠️  CUDA Out Of Memory: {e}" + fg.rs)
        print(fg.yellow + "🔄 Liberando cache e tentando novamente..." + fg.rs)
        torch.cuda.empty_cache()

message = [
    {
        "role": "system",
        "content": """
        You are a friendly chatbot named Chatty
        """
    },
    {
        "role": "user",
        "content": """
        Please introduce yourself and add
        'how can I help you today?' at
        the end of the response
        """
    }
]

ask_question(message)

while True:
    prompt = input("\nYour question:")
    message[1]["content"] = prompt
    if prompt.lower() == "exit":
        break
    ask_question(message)
