import openai

openai.api_key = "your-api-key-here"

def generate_music(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Згенеруй MIDI-файл на тему: {prompt}",
        max_tokens=100
    )
    return response["choices"][0]["text"].strip()

theme = "Космічна подорож"
print(f"Генерація музики для теми: {theme}")
print(generate_music(theme))
