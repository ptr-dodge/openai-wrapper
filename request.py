import openai as ai
from sys import argv

ai.api_key = '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'


def generate_gpt3_response(user_text, print_output=False):
    completions = ai.Completion.create(
        engine='text-davinci-003',  # Determines the quality, speed, and cost.
        temperature=0.5,            # Level of creativity in the response
        prompt=user_text,           # What the user typed in
        max_tokens=500,             # Maximum tokens in the prompt AND response
        n=1,                        # The number of completions to generate
        stop=None,                  # An optional setting to control response generation
    )

    # Displaying the output can be helpful if things go wrong
    if print_output:
        print(completions)

    # Return the first choice's text
    return completions.choices[0].text


if __name__ == '__main__':
    prompt = ''
    for item in argv[1:]:
        prompt += item + ' '

    print('——————————————————————————————————————————————————————————————————————')
    print(prompt)
    print('——————————————————————————————————————————————————————————————————————')
    print('┃                            GPT OUTPUT                              ┃')
    print('——————————————————————————————————————————————————————————————————————')
    response = generate_gpt3_response(prompt)
    print("\r\n"+response)
    print('——————————————————————————————————————————————————————————————————————')
