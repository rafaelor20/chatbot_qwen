# chatbot_qwen
Create a Better Chatbot with Qwen

## Requirements
Download <a href="https://docs.docker.com/desktop/" target="_blank">Docker Desktop</a> and make sure the engine is running.

## Instructions
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
