from flask import Flask, request, Response
import pathlib, os

def startup_tasks():
    global v_storage
    v_storage = pathlib.Path(os.getenv("VSTORAGE_DIR"))
    v_storage.mkdir(parents=True, exist_ok=True)