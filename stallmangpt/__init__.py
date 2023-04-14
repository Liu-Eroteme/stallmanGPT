import os
import re
import sys
import openai
import openai.error

class MissingAPIKeyError(Exception):
    pass

def get_openai_api_key():
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        raise MissingAPIKeyError("The OPENAI_API_KEY environment variable is not set. Please set it before using this tool.")
    return key

openai.api_key = get_openai_api_key()

def prompt_openai(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a linux terminal assistant."}, {"role": "user", "content": prompt}],
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].message['content'].strip() # type: ignore
    except openai.error.RateLimitError as e:
        print("You have reached your OpenAI API usage limit. Please wait and try again later.")
        sys.exit(1)


def get_confidence_rating(command, request, retries=0):
    prompt = f"Rate the following command from 0-100 based on how well it accomplishes '{request}':\n{command}. Your reply should consist of a single natural number ranging from 0-100 only, do not explain."
    response = prompt_openai(prompt)
    try:
        match = re.search(r'\b(100|[0-9]{1,2})\b', response)
        if match:
            rating = float(match.group(0))
        elif retries < 1:
            return get_confidence_rating(command, request, retries+1)
        else:
            sys.exit("Error: Could not parse confidence rating. Exiting.")
    except ValueError:
        if retries < 1:
            return get_confidence_rating(command, request, retries+1)
        else:
            sys.exit("Error: Could not parse confidence rating. Exiting.")
    return rating

def main():
    if len(sys.argv) < 2:
        print("Usage: stallmangpt [text]")
        sys.exit(1)

    request = sys.argv[1]
    improvement_counter = 0
    confidence_threshold = 80
    command = ""
    explanation = ""
    retry_limit = 3

    while improvement_counter < 10:
        prompt = f"Please generate a Linux command - and only a command. do not explain it. do not add any text that is not part of the command - that will do this: '{request}'" if not command else f"The following command did not pass the confidence rating threshold of {confidence_threshold}:\n{command}\nPlease improve the command based on the intended goal: '{request}'"
        command = prompt_openai(prompt)
        confidence = get_confidence_rating(command, request)
        if confidence >= confidence_threshold:
            explanation = prompt_openai(f"Explain the following Linux command and how it accomplishes the goal '{request}':\n{command}")
            break
        improvement_counter += 1
        if improvement_counter == 10:
            sys.exit("The program could not generate a satisfactory command after 10 attempts. Exiting.")

    print(f"Command: {command}\nExplanation: {explanation}")

    retry_counter = 0
    while retry_counter < retry_limit:
        choice = input("Do you want to execute the command? (y/n): ").lower()
        if choice in ["y", "yes"]:
            os.system(command)
            break
        elif choice in ["n", "no"]:
            main()
            break
        else:
            print("Invalid choice.")
        retry_counter += 1

if __name__ == "__main__":
    main()
