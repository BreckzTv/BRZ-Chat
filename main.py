import requests
from config import OLLAMA_API_URL

print("== Ollama Terminal-Chat ==")
print("Tippe 'exit' zum Beenden.\n")

while True:
    prompt = input("> ")
    if prompt.lower() in ("exit", "quit"):
        break

    try:
        res = requests.post(OLLAMA_API_URL, json={
            "model": "gemma3:1b",
            "prompt": prompt,
            "stream": False
        })
        print("\nAntwort:\n", res.json().get("response", "Keine Antwort erhalten."), "\n")
    except Exception as e:
        print("Fehler beim Senden:", e)
