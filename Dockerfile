FROM anibali/pytorch:latest

WORKDIR /spotlight

COPY requirements.txt /spotlight
RUN sudo apt-get update && sudo apt-get install -y libsm6 libxext6 libxrender-dev libglib2.0-0

RUN pip install -r ./requirements.txt

COPY . /spotlight
ENV CHECKPOINTS_DIR /spotlight/model/checkpoints/
RUN sudo chmod -R a+rwx /spotlight/
CMD ["python","app.py","--gpu_ids=-1"]~
