import os

def run_in_sandbox(file_path):
    os.system(f"docker run --rm -v {file_path}:/testfile.exe ubuntu:latest bash -c './testfile.exe'")
