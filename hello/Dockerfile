FROM python:3.11

RUN pip install pytest pytest-watch

RUN useradd -m -s /bin/bash -G sudo user

WORKDIR /app
RUN chown -R user:user /app
USER user
CMD ptw
