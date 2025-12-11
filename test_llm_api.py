import requests
import json
url = "https://aigc-api.hkust-gz.edu.cn/v1/chat/completions"
headers = { 
"Content-Type": "application/json", 
"Authorization": "3d73fa38f346421d9dc26b869a5d04307614a1d77ca949528d7c2c00c2361640" 
}
data = { 
"model": "Qwen", # # "Qwen" "DeepSeek-R1-671B" "gpt-3.5-turbo" version in gpt-4o-mini, "gpt-4" version in gpt-4o-2024-08-06
"messages": [{"role": "user", "content": "who are you"}],
"temperature": 0
}
response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.json())
