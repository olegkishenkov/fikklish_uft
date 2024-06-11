FROM python:3.12-bookworm
RUN mkdir /opt/project
WORKDIR /opt/project
COPY pyproject.toml /opt/project/
RUN curl -sSL https://install.python-poetry.org | python3 -
# RUN echo "PATH=/root/.local/bin:$PATH" >> /etc/environment
RUN /root/.local/bin/poetry config virtualenvs.create false
RUN /root/.local/bin/poetry install
CMD bash
