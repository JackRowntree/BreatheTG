from setuptools import setup, find_packages


setup(
    name="breathe_tg_bot",
    version="0.0.1",
    description="TG bot to transmit pollution data",
    url="https://github.com/JackRowntree/BreatheTG",
    packages=find_packages(),
    install_requires = [
        'python-telegram-bot',
        'ksql',
        'pandas',
        'boto3'
    ],
)