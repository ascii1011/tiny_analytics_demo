
import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
from lib.utils import download_image, generate_prompt

__all__ = ["pet_name", "generate_images", "dev_chat_bot", "generate_horror_story", "generic_chat_bot", "study_notes", "create_product_name"]

def pet_name(animal):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=generate_prompt(request.form["animal"]),
        temperature=0.6,
    )
    return response.choices[0].text

def generate_images(request):
    """
    1 to 10 images 
    res: 256x256, 512x512, or 1024x1024 pixels"""
    # keywords example: "a white siamese cat"
    keywords = request.form["keywords"]
    print(f"{keywords=}")

    response = openai.Image.create(
        prompt=keywords,
        n=2,
        size="1024x1024"
    )
    print(f"{len(response['data'])=}")
    result = ""
    for i in range(len(response['data'])):
        image_url = response['data'][i]['url']
        print(f"{i}){image_url=}")
        if result == "":
            result = download_image(image_url, prefix='_'.join(keywords.split()))
        else:
            result += " | " + download_image(image_url, prefix='_'.join(keywords.split()))
    print(f"{result=}")
    return result

def dev_chat_bot(request):
    """
    prompt example:
    "You: How do I combine arrays?\nJavaScript chatbot: You can use the concat() method.\nYou: How do you make an alert appear after 10 seconds?\nJavaScript chatbot"
    """
    chat_input = request.form["chat_input"]
    
    response = openai.Completion.create(
        model="code-davinci-002",
        prompt=chat_input,
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=["You:"]
    )
    print(f"{response=}")
    return response.choices[0].text

def generate_horror_story(request):
    """
    prompt example:               
    Topic: wrench\nTwo-Sentence Horror Story:
    """
    keywords = request.form["keywords"]
    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=keywords,
        temperature=0.8,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )
    print(f"{response=}")
    return response.choices[0].text

def generic_chat_bot(request):
    """
    prompt example:
    The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: I'd like to cancel my subscription.\nAI:
    """
    chat_input = request.form["chat_input"]
    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chat_input,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    print(f"{response=}")
    return response.choices[0].text

def study_notes(request):
    """
    prompt example:
    The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: I'd like to cancel my subscription.\nAI:
    """
    keywords = request.form["keywords"]
    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=keywords,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    print(f"{response=}")
    return response.choices[0].text

def create_product_name(request):
    """
    prompt example:
    Product description: A home milkshake maker\nSeed words: fast, healthy, compact.\nProduct names: HomeShaker, Fit Shaker, QuickShake, Shake Maker\n\nProduct description: A pair of shoes that can fit any foot size.\nSeed words: adaptable, fit, omni-fit.
    """
    keywords = request.form["keywords"]
    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=keywords,
        temperature=0.8,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    print(f"{response=}")
    return response.choices[0].text



