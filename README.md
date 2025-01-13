# chatbot_qwen
Create a Better Chatbot with Qwen

## Requirements
Download <a href="https://docs.docker.com/desktop/" target="_blank">Docker Desktop</a> and make sure the engine is running.

## Video Instructions
<a href="https://youtube.com/shorts/YWUvD6qe56g"><img src="https://github.com/user-attachments/assets/fa2fe923-4622-4e4d-9e01-a338e77afbc1" width="600px"></a>

## Text Instructions
1. clone this repository using WSL2 with
`git clone https://github.com/MariyaSha/chatbot_qwen.git`
2. navigate there with
`cd chatbot_qwen`
3. build Docker image with
`docker build -t chatbot .`
5. run Docker container with
`docker run -it --gpus=all chatbot`

## Credits
this tutorial is using the <a href="https://github.com/QwenLM/Qwen" target="_blank">Qwen Large Language Model</a>.

