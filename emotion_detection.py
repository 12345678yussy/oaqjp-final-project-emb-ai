import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    response = requests.post(url, json=input_json, headers=headers)
    
    # Convert response to JSON format
    response_json = response.json()
    
    # Extracting emotions
    emotions = response_json.get('emotionPredictions', [{}])[0].get('emotion', {})
    
    # Get specific emotion scores
    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)
    
    # Finding the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Formatting the output as a dictionary
    formatted_output = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    
    return formatted_output
