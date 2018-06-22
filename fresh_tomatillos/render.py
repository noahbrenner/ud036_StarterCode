# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import io
import os


MODULE_DIR = os.path.dirname(os.path.abspath(__file__))


def _read_file(relative_path):
    """Return the contents of a file as a Unicode string.

    Args:
        relative_path: Path to the file, relative to this module.

    Returns:
        Contents of the file as a string.
    """
    path = os.path.normpath(os.path.join(MODULE_DIR, relative_path))

    with io.open(path, 'r', encoding='utf-8') as input_file:
        return input_file.read()


def _create_movie_tiles(movies, tile_template):
    """Return a string containing unique HTML for each movie."""
    return '\n'.join(tile_template.format(movie=movie) for movie in movies)


def compile_movies_page(movies):
    """Return generated HTML for movies page."""
    # Get template and static content.  Each template has `{variable}`
    # sections meant to be used with `str.format()`.
    main_page = _read_file('templates/main_page.html')
    movie_tile = _read_file('templates/movie_tile.html')
    scripts = _read_file('static/scripts.js')
    styles = _read_file('static/styles.css')

    # Compile the full movies page, including movie tiles
    rendered_content = main_page.format(
        movie_tiles=_create_movie_tiles(movies, movie_tile),
        scripts=scripts,
        styles=styles)

    return rendered_content
