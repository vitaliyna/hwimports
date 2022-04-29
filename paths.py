from dataclasses import replace
from pathlib import Path
import argparse
import os
import logging

logger = logging.getLogger()
handler = logging.FileHandler('logs.log')
logger.addHandler(handler)

parser = argparse.ArgumentParser(description="Упорядочивает файлы в директории")
logger.error('Добавляются аргументы коммандной строки "restructrure" и "directory"')
parser.add_argument('restructrure', type = str)
parser.add_argument('directory', type = str)
args = parser.parse_args()

files = os.listdir('d:/belhard/directory')
logger.error('определяется директория, в которой будут создаваться новые директории с файлами')
for x in files:
    edited_files = x.replace('-', '/')
    dirpath, filename = os.path.split(edited_files)
    if Path('d:/belhard/directory/' + dirpath).is_dir():
        print(f"Директория {'d:/belhard/directory/' + dirpath} уже существует")
        logger.error(f"Директория {'d:/belhard/directory/' + dirpath} уже существует")
    else:
        os.makedirs('d:/belhard/directory/' + dirpath)
        logger.error(f'создалась директория d:/belhard/directory/ {dirpath}')
    if Path('d:/belhard/directory/' + dirpath + '/' + filename).is_file():
        print("Файл уже существует")
        logger.error("Файл уже существует")       
    else:
        with open('d:/belhard/directory/' + dirpath + '/' + filename, 'x'):
            pass
        logger.error(f'создался файл {filename} в диретории  d:/belhard/directory/ {dirpath}')
    


