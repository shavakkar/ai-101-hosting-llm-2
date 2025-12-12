Downloaded the LLM from this [Kaggle Link](https://www.kaggle.com/datasets/d0rj3228/googleflan-t5-small?form=MG0AV3)

To test the LLM, use this! 

```bash
curl -X POST http://localhost:8120/generate \
     -H "Content-Type: application/json" \
     -d "{\"prompt\": \"Explain AI simply\"}"