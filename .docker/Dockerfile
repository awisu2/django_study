# python3 requirements.txtでinstall する image
# 開発、本番などの環境別基本imageとして利用を想定
FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN python -m pip install -U pip

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "--version" ]
