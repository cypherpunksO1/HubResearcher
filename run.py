import asyncio
import argparse

from src.main.base import init_models


parser = argparse.ArgumentParser()
parser.add_argument('--init', action='store_true', help='Create db tables')
args = parser.parse_args()


if __name__ == "__main__":
    if args.init:
        print("DB tables is created.")
        init_models()
    else:
        from src.main.bot import bot_main

        asyncio.run(bot_main())
