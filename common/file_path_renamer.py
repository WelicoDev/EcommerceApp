import os

from datetime import datetime

from django.utils.deconstruct import deconstructible

@deconstructible
class PathAndRename(object):
    """File * rename & repath

    Args :
        object : renamed * path"""
    def __init__(self , sub_path):
        self.path = sub_path

    def __call__(self, instance , filename):
        ext = filename.split(".")[-1]
        filename = filename.split(".")[0]
        today = datetime.now().strftime("%Y-%m-%d")
        filename = f"{filename}_{today}.{ext}"

        return os.path.join(self.path ,filename)


