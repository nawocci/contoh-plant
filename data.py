import random

responses = [
    {
        "plant": "tomato",
        "disease": "black spot",
        "details": "Black spot is a dangerous disease affecting tomatoes, characterized by dark, sunken lesions on the leaves and fruits. If left untreated, it can lead to significant crop loss. The disease thrives in warm, humid conditions and can spread rapidly through water splashes and contaminated tools. It is essential to implement good agricultural practices, including crop rotation and the use of resistant varieties, to manage and control this disease effectively."
    },
    {
        "plant": "potato",
        "disease": "late blight",
        "details": "Late blight is a serious disease that affects potatoes, notorious for causing the Irish Potato Famine. This disease is caused by the water mold Phytophthora infestans and results in dark, greasy lesions on leaves and stems, which can rapidly lead to plant death. Infected tubers may also develop decay, making them unmarketable. Effective management includes using resistant varieties, proper spacing for airflow, and timely fungicide applications."
    },
    {
        "plant": "corn",
        "disease": "rust",
        "details": "Rust is a common disease in corn, identifiable by its reddish-brown pustules on leaves. These pustules produce spores that can easily spread to other plants, leading to reduced photosynthesis and stunted growth. Rust is favored by warm temperatures and high humidity, making monitoring critical. Crop rotation and resistant hybrid varieties are key strategies for minimizing the impact of this disease."
    },
    {
        "plant": "wheat",
        "disease": "powdery mildew",
        "details": "Powdery mildew is a fungal disease that significantly impacts wheat production. It appears as white, powdery spots on the leaves, stems, and spikes, which can reduce grain yield and quality. This disease thrives in warm, dry conditions, often leading to increased susceptibility in dense crop canopies. Effective control methods include the use of resistant wheat varieties and proper field management to improve air circulation."
    },
    {
        "plant": "rice",
        "disease": "bacterial blight",
        "details": "Bacterial blight is a serious disease affecting rice, causing water-soaked lesions on leaves and stems that can lead to severe yield losses. This disease is especially problematic in humid conditions and can spread through infected seeds or irrigation water. Integrated pest management strategies, including resistant varieties and proper water management, are crucial to control this disease and ensure healthy crop development."
    },
    {
        "plant": "soybean",
        "disease": "root rot",
        "details": "Root rot is a common disease in soybeans, often caused by soil-borne fungi like Phytophthora spp. Infected plants show stunted growth and yellowing leaves, and the roots may appear brown and mushy. This disease can lead to significant yield losses, especially in poorly drained soils. Crop rotation, proper drainage, and planting resistant varieties can help manage this issue effectively."
    },
    {
        "plant": "barley",
        "disease": "leaf rust",
        "details": "Leaf rust is a fungal disease that affects barley, characterized by small, round, rust-colored pustules on the leaves. This disease can severely hinder photosynthesis, leading to reduced grain fill and overall yield. The spores are easily spread by wind and rain, making timely monitoring and control essential. Planting resistant varieties and applying fungicides when necessary are effective management strategies."
    },
    {
        "plant": "grape",
        "disease": "downy mildew",
        "details": "Downy mildew is a serious disease in grapes, caused by the oomycete Plasmopara viticola. It manifests as yellow-green spots on leaves, followed by a white, downy growth on the undersides. This disease can also affect the fruit, leading to rot and decreased quality. Prevention is key, involving the use of resistant varieties, careful vineyard management, and timely fungicide applications to protect plants during wet conditions."
    },
    {
        "plant": "apple",
        "disease": "fire blight",
        "details": "Fire blight is a bacterial disease affecting apples, recognized by wilting, blackened blossoms and shoots that resemble fire-scorched wood. This disease can quickly spread through pollinators and rain, leading to severe damage and loss of entire branches. Effective management strategies include pruning infected areas, using resistant cultivars, and applying bactericides during critical infection periods to mitigate its impact."
    },
    {
        "plant": "peach",
        "disease": "peach leaf curl",
        "details": "Peach leaf curl is a fungal disease that affects peaches, causing dramatic leaf distortion and bright red or purple discoloration in the spring. If left untreated, it can weaken trees and reduce fruit production. The disease is most prevalent in cool, wet weather and can be managed through the application of fungicides during dormancy and by ensuring good air circulation and tree health through proper pruning."
    }
]

def get_random_response():
    return random.choice(responses)