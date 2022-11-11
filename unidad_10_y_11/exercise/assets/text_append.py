import os


def append_text(path, text):
    """this function creates an sequence diagram instead of four diagrams files

    :param path: the path where the file is
    :type path: string
    :param text: the output of each test method
    :type text: string
    """
    with path.open("a") as f:
        f.write(text)

sequence_diagram_filename = os.path.join(os.path.dirname(__file__), '..', 'doc', 'diagrama_secuencia.md')