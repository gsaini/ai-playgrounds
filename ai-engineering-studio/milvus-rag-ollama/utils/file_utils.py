import glob

def load_text_lines(pattern):
    """
    Load text lines from files matching the given pattern.

    Args:
        pattern (str): Glob pattern to match files.

    Returns:
        list: A list of text lines from the matched files.
    """
    text_lines = []
    for file_path in glob.glob(pattern):
        with open(file_path, 'r') as file:
            text_lines.extend(file.readlines())
    return text_lines