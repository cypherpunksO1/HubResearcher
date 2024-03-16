# HubResearcher

Telegram inline-mode bot for repository searching.


# Run!

Docker:

```bash
docker build . --tag hubresearcher
```

```bash
docker run --name hubresearcher -d hubresearcher
```

Docker compose:

```bash
docker-compose up -d
```

Base:

```bash
python3 -m venv env
```

```bash
source env/bin/activate
```

```bash
python3 -m pip install -r requirements.txt
```

```bash
python3 run.py --init
```

```bash
python3 run.py
```