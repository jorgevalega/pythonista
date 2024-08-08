from setuptools import setup, find_packages
from pathlib import Path

setup(name='pro-video-ferramentas-jorgevalega',version=1.0,description='Este pacote irá fornecer ferramentas de processamento de vídeo',long_description=Path('README.md').read_text(),author='Jorge',author_email='jorgevalega@gmail.com',keywords=['camera', 'video', 'processamento'],packages=find_packages())