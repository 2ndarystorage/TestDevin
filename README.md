# TestDevin

## Program Summary
- Single Python script that calls a local OpenAI-compatible API endpoint (LM Studio default) to generate a chat completion and prints the response.
- Prompts are in Japanese and request a proverb; output is the assistant reply.

## How to Use
- `python LMstudioAPIKey.py`
- Requires the `openai` Python package and a local server at `http://localhost:1234/v1` with a model named `llama3`. Not verified.

## Completion Status
- Prototype: minimal example script with hardcoded settings and no error handling.

## Program Summary
- Python script that uses the OpenAI client against a local OpenAI-compatible server (LM Studio default URL) to request a Japanese proverb and print the response.
- Uses hardcoded model name (`llama3`) and messages; no CLI or config.

## How to Use
- Install dependencies: `pip install openai` (Not verified).
- Run: `python LMstudioAPIKey.py` (Not verified).
- Ensure a local OpenAI-compatible server is running at `http://localhost:1234/v1` with a model named `llama3` (Not verified).

## Completion Status
- Prototype: single hardcoded example without validation, error handling, or configuration.
