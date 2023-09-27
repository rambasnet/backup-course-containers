FROM python:3

RUN pip install pytest

RUN useradd -m -s /bin/bash -G sudo user

WORKDIR /app
RUN chown -R user:user /app
USER user
CMD bash -i
