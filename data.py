import random

responses = [
    {
        "plant": "tomato",
        "disease": "black spot",
        "details": "Black spot is a dangerous disease if found on a tomato. Blablabla"
    },
    {
        "plant": "potato",
        "disease": "late blight",
        "details": "Late blight is a serious disease affecting potatoes. Blablabla"
    },
    {
        "plant": "corn",
        "disease": "rust",
        "details": "Rust is a common disease in corn. Blablabla"
    },
    {
        "plant": "wheat",
        "disease": "powdery mildew",
        "details": "Powdery mildew is a fungal disease affecting wheat. Blablabla"
    },
    {
        "plant": "rice",
        "disease": "bacterial blight",
        "details": "Bacterial blight is a serious disease in rice. Blablabla"
    },
    {
        "plant": "soybean",
        "disease": "root rot",
        "details": "Root rot is a common disease in soybeans. Blablabla"
    },
    {
        "plant": "barley",
        "disease": "leaf rust",
        "details": "Leaf rust is a fungal disease affecting barley. Blablabla"
    },
    {
        "plant": "grape",
        "disease": "downy mildew",
        "details": "Downy mildew is a serious disease in grapes. Blablabla"
    },
    {
        "plant": "apple",
        "disease": "fire blight",
        "details": "Fire blight is a bacterial disease affecting apples. Blablabla"
    },
    {
        "plant": "peach",
        "disease": "peach leaf curl",
        "details": "Peach leaf curl is a fungal disease affecting peaches. Blablabla"
    }
]

def get_random_response():
    return random.choice(responses)