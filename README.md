To test the LLM, use this! 

```bash
curl -X POST http://localhost:8120/generate \
     -H "Content-Type: application/json" \
     -d "{\"prompt\": \"Explain AI simply\"}"
```