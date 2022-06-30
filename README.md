# Cookiecuter Personal - Tutorial

<!-- badges: start -->
[![@edev_10](https://img.shields.io/badge/@edev10-Twitter-blue?&logoColor=white)](https://twitter.com/edev_10) 
[![Platzi](https://img.shields.io/badge/Curso_Platzi-Configuración_Avanzada_...-green&logoColor=white)](https://platzi.com/datos/)
<!-- badges: end -->

Aprende a crear tu propia plantilla personalizada utilizando cookiecutter.

## Requiremientos

- [Anaconda](https://www.anaconda.com/download/) >= 4.x
- [git](https://git-scm.com/) >= 2.x
- [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0:
    Esto puede ser instalado con `pip` o `conda` dependiendo cómo tú manejas tus paquetes de Python:

``` bash
pip install cookiecutter
```

o

``` bash
conda install -c conda-forge cookiecutter
```

## Crear un nuevo proyecto

En el directorio en el que quieras guardar tu proyecto generado:

```bash
cookiecutter https://github.com/edev10/cookiecutter-personal --checkout cookiecutter-personal
```


## Estructura de directorios y archivos resultantes

    {{ cookiecutter.project_slug }}
        ├── data
        │   ├── processed      <- The final, canonical data sets for modeling.
        │   └── raw            <- The original, immutable data dump.
        │
        ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
        │                         the creator's initials, and a short `-` delimited description, e.g.
        │                         `1.0-jvelezmagic-initial-data-exploration`.
        │
        ├── .gitignore         <- Files to ignore by `git`.
        │
        ├── environment.yml    <- The requirements file for reproducing the analysis environment.
        │
        └── README.md          <- The top-level README for developers using this project.

---
Proyecto creado con el curso: [Configuración Profesional de Entorno de Trabajo para Ciencia de Datos](https://platzi.com/cursos/entorno-ciencia-datos/) de [Platzi](https://platzi.com/). By: [@edev10](https://twitter.com/edev_10).


