FROM continuumio/miniconda3

RUN apt-get update && apt-get install -y \
    gcc g++ \
    libgtk2.0-0 \
    xvfb \
    qtbase5-dev \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /home/jenkins/.conda
RUN conda install -c conda-forge -n base mamba
