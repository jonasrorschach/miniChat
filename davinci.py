'''
I wanted to create a program where I can work with storing data,
and at the same time configuring and working with chatGPT.
So there is a lot to improve, that I will work on from time to time.

'''

import openai

openai.api_key = 'YOUR_API_KEY_IN_HERE'

data = {}


with open('storagefile.txt', 'a') as w:

    while True:

        prompt = input('Enter your prompt: ')

        prompt_quest = prompt.strip().lower() == 'q'

        if prompt_quest:
            break

        w.write('question: ' + prompt + '\n' )



        response = openai.Completion.create( # API configuration
        engine = 'text-davinci-003',
        prompt = prompt,
        max_tokens = 4000, # the input prompt count as tokens too
        n = 1,
        stop = None,
        temperature = 0.5,

        )



        answer = f'{response.choices[0].text}\n'

        print(answer)

        w.write(answer +'\n')
