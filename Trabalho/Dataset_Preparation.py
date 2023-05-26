import os
import random

random.seed(1234)

with os.scandir("Dataset/Fish_Dataset") as subFolders:
    for id, imageClass in enumerate(subFolders):
        with os.scandir(imageClass.path) as imagesAndMasks:
            for folder in imagesAndMasks:
                if "GT" in folder.name:
                    with os.scandir(folder.path) as files:
                        for fileId, file in enumerate(files):
                            newPath = (
                                "Dataset\Compiled\Classification\Mask\\"
                                + "{:0>3}".format(id)
                                + "_"
                                + "{:0>5}".format(fileId)
                                + "."
                                + file.name.split(".")[1]
                            )
                            os.replace(file.path, newPath)
                else:
                    with os.scandir(folder.path) as files:
                        for fileId, file in enumerate(files):
                            newPath = (
                                "Dataset\Compiled\Classification\Image\\"
                                + "{:0>3}".format(id)
                                + "_"
                                + "{:0>5}".format(fileId)
                                + "."
                                + file.name.split(".")[1]
                            )
                            os.replace(file.path, newPath)
