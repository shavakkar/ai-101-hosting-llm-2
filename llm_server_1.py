from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM

app = FastAPI()

# ✅ Load model from local folder
model_path = r"C:/Softwares/LLMS/deepseek-r1-distill-qwen-1.5b"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

class Prompt(BaseModel):
    prompt: str
    max_tokens: int = 128

@app.post("/generate")
def generate_text(data: Prompt):
    inputs = tokenizer(data.prompt, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_new_tokens=data.max_tokens,
        do_sample=True,
        temperature=0.7,
    )
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"response": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("llm_server:app", host="0.0.0.0", port=8120)