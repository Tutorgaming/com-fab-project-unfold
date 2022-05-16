import numpy as np
from modules.file_manager import read_stl



if __name__ == "__main__":
    stl_path = "./stl/cube.stl"
    vertices, faces = read_stl(stl_path)
    print (vertices)