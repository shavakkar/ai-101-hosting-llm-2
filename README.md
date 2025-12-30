## Models:
|Model|Filename|
|-----|--------|
|flan-t5-small|llm_server.py|
|Deepseek-R1-Distill-Qwen-1.5B|llm_server_1.py|

## Guide:

Downloaded the LLM from this [Kaggle Link](https://www.kaggle.com/datasets/d0rj3228/googleflan-t5-small?form=MG0AV3)

To test the LLM, use this! 

```bash
curl -X POST http://localhost:8120/generate \
     -H "Content-Type: application/json" \
     -d "{\"prompt\": \"Explain AI simply\"}"