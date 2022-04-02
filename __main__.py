import os
from os.path import exists
import re
import click
from pathlib import Path
from appdirs import user_config_dir
from shutil import copy
import platform
import pyperclip
import subprocess


source_plantilla_teoria = str(Path(__file__).parent / 'plantilla_teoria.pdf')
source_plantilla_ejercicios = str(Path(__file__).parent / 'plantilla_ejercicios.pdf')

def illustrator(path): 
    subprocess.Popen(['Illustrator', str(path)])

# syntax: python -m illustrator-figures crear-editar "nombre_fig" directorio_figure
@click.group()
def cli():
   pass 

@cli.command(help='crear y editar figura')
@click.argument('nombre')
@click.argument('directorio')
def crear_editar(nombre,directorio):
    nombre = nombre.strip()
    directorio = directorio.strip()
    file_name = nombre+'.pdf'
    # figures = Path(directorio).absolute()
    name_archive_figures = "IMAGES-"+directorio.split("\\")[-1].split(".")[0]
    directory_archive_tex = directorio.split('\\')
    del directory_archive_tex[-1]

    #construye el directorio de archivo tex
    dir_h = ""
    for index,item in enumerate(directory_archive_tex):
        if index == 0:
            dir_h = item
        else:
            dir_h = dir_h + "\\" + item

    directory_figure = str(dir_h+'\\'+name_archive_figures+'\\'+file_name)

    #decide si es teoria o ejercicio
    for n in name_archive_figures.split("-"):
        if n == "TEORIA":
            source = source_plantilla_teoria
            break
        else:
            source = source_plantilla_ejercicios

    # If a file with this name already exists, append a '2'.
    if os.path.exists(directory_figure):
        illustrator(directory_figure)
    else:
        copy(str(source),str(directory_figure))
        illustrator(directory_figure)


@cli.command(help='modificar una figura')
@click.argument('name')
@click.argument('directorio')
def ver_figuras_creadas(nombre,directorio):
    click.echo(f'modificar figura con nombre de la figura: {nombre}; directorio {directorio}')


if __name__ == "__main__":
    cli()
