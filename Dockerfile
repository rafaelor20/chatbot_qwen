FROM python:3

RUN pip install torch
RUN pip install transformers
RUN pip install sty
RUN pip install accelerate

#COPY main.py ./
COPY main_deepseek.py ./

#ENTRYPOINT python3 main.py
ENTRYPOINT python3 main_deepseek.py