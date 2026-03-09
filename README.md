# TestDevin

## Program Summary
- Single Python script that calls a local OpenAI-compatible API endpoint (LM Studio default) to generate a chat completion and prints the response.
- Prompts are in Japanese and request a proverb; output is the assistant reply.

## How to Use
- `python LMstudioAPIKey.py`
- Requires the `openai` Python package and a local server at `http://localhost:1234/v1` with a model named `llama3`. Not verified.

## Completion Status
- Prototype: minimal example script with hardcoded settings and no error handling.
