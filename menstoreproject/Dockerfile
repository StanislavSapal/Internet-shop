FROM python:3.10.9

SHELL ["/bin/bash", "-c"]

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim

RUN useradd -rms /bin/bash menstore && chmod 777 /opt /run

WORKDIR /menstore

RUN mkdir /menstore/static && mkdir /menstore/media && chown -R menstore:menstore /menstore && chmod 755 /menstore

COPY --chown=menstore:menstore . .

RUN pip install -r requirements.txt

USER menstore

CMD ["gunicorn", "-b", "172.31.19.9:8000", "menstoreproject.wsgi:application"]