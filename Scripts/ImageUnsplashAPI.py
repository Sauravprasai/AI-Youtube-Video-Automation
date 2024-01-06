import requests, json, re

def download_images_unsplash():
    with open('Text Folder/Images_name.txt', 'r') as file:
        cleaned_names = file.readlines()

    Images_names = [re.sub(r'[^a-zA-Z0-9\s]', '', name) for name in cleaned_names]

    for i, image_name in enumerate(Images_names):
        clean_name = image_name.strip()
        
        url = f"https://api.unsplash.com/search/photos?client_id=Ho41Nb1mQ6VzdmXVp7qm_ztD0GrXJRggq5vled1LhM8&query={clean_name}&count=2"
        
        response = requests.get(url)
        data = json.loads(response.text)
        
        if data["results"]:
            image_url = data["results"][0]["urls"]["full"]
            image_response = requests.get(image_url)
            
            with open(f'Images/Unsplash/{clean_name}.jpg', 'wb') as f:
                f.write(image_response.content)
            
    print("Images from Unsplash downloaded successfully!")