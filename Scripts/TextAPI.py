import requests

API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
def generate_script_and_images(title):
    # response_script = client.chat.completions.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         { "role": "system", "content": "You are a cool at the same time polite bot which provide facts about different stuff and writes a script for YouTube short videos of less than 1 minutes which includes 3 4 facts. Dont use any quotation mark in whole output. Start with some amazing words to attract more audience. Channel name is shortify. Make it as a paragraph without any line break"},
    #         { "role": "user", "content": title},
    #     ]
    # )
    output = query({
        "inputs": "Create a 1 minute script for YouTube short video which includes 3 4 facts about " + title + ". Channel name is shortify. Make it as a paragraph without any line break",
    })

    # response_value = response_script.choices[0].message.content

    # response_images = client.chat.completions.create(
    #     messages=[
    #         {
    #             "role": "system",
    #             "content": "You are a bot which generates something to prompt in AI image generator for every 7 second of the script that is given to you. Make sure to give prompt of 7 8 word for each 7 second of script. There had to be atleast something for each seven second of this script. Seperate each with a line break. Don't even use number like 1,2,3 or titles. Only provide Images name for prompt to generate. This is just example of prompt from AI image prompt generator dont use this to create one:\n Enchanted forest with whimsical creatures and glowing trees \n Majestic castle overlooking a shimmering lake at dawn \n Futuristic cityscape with flying cars and neon lights \n Serene beach with crystal clear turquoise waters and palm trees \n Ancient ruins surrounded by lush jungle and hidden treasures \n Cozy cabin nestled in a snowy mountain landscape \n Vibrant marketplace bustling with colorful fruits and vibrant textiles. ",

    #         },
    #         {
    #             "role": "user",
    #             "content": f"{response_value} Create a prompt for AI image generator every 7 second of the script.",
    #         }
    #     ],
    #     model="gpt-3.5-turbo",
    # )

    # with open('Text Folder/Response.txt', 'w') as file:
    #     file.write(response_script.choices[0].message.content)

    # with open('Text Folder/Images_name.txt', 'w') as file:
    #     file.write(response_images.choices[0].message.content)

    print(output)
