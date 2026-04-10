#!/usr/bin/env python3
"""
Batch image generation using Playground AI (Free tier)
Sign up at https://playgroundai.com for 500 free images/month
"""

import requests
import time
import argparse
from pathlib import Path
from datetime import datetime
import re


class PlaygroundAIGenerator:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.api_url = "https://api.playgroundai.com/v1/images/generations"
        
    def generate_image(self, prompt: str, output_path: str) -> bool:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "modelId": "sd-3.0",  # Free tier model
            "prompt": prompt,
            "width": 1024,
            "height": 768,
            "numImages": 1
        }
        
        try:
            response = requests.post(self.api_url, json=payload, headers=headers)
            
            if response.status_code == 200:
                data = response.json()
                image_url = data['images'][0]['url']
                
                # Download image
                img_response = requests.get(image_url)
                with open(output_path, 'wb') as f:
                    f.write(img_response.content)
                return True
            else:
                print(f"  Error: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"  Error: {str(e)}")
            return False


# Same extractor and main function as above...