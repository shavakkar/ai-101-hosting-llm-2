from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

app = FastAPI()

# Load model once at startup
model_name = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

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