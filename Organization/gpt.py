import os
import openai
openai.organization = "org-dbTAYmDzpKNWvuR5dgfi6mfL"
openai.api_key = "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"

def generate_response(prompt):
    completions = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 1024,
        n = 1,
        stop = None,
        temperature = 0
    )

    message = completions.choices[0].text
    return message.strip()

while True:
    prompt = input(">>>")
    print(generate_response(prompt))



