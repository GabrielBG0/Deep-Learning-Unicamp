from glob import glob
import numpy as np
import shutil
import cv2
from torchvision import transforms
from PIL import Image

aug = transforms.Compose([
    transforms.Resize((300, 300), interpolation=transforms.InterpolationMode.BILINEAR,
                      max_size=None, antialias="True"),
    transforms.RandomAffine(degrees=360, translate=(0.05, 0.2), scale=(0.7, 1.5), shear=(-2, 2),
                            interpolation=transforms.InterpolationMode.BILINEAR,
                            fill=0),
    transforms.CenterCrop(250),
    transforms.Resize((224, 224), interpolation=transforms.InterpolationMode.BILINEAR,
                      max_size=None, antialias="True"),
])

data = glob("Trabalho\\Dataset\\Compiled\\Classification\\*.jpg")

train_perc = 0.40
valid_perc = 0.30
test_perc = 0.30

num_train_samples = int(len(data)*train_perc)
num_valid_samples = int(len(data)*valid_perc)
num_test_samples = int(len(data)*test_perc)
np.random.shuffle(data)  # randomly change the order of the filenames in data
trainset = data[:num_train_samples]
validset = data[num_train_samples:num_train_samples+num_valid_samples]
testset = data[num_train_samples+num_valid_samples:]


i = 0
for img in trainset:
    img_class = img.split("\\")[-1].split("_")[0]
    img = Image.open(img)
    for j in range(30):
        aug_img = aug(img)
        aug_img.save("Trabalho\\Dataset\\Compiled\\Classification\\Train\\" +
                     img_class + "_" + "{:0>5}".format(str(i)) + ".jpg")
        i += 1

for id, img in enumerate(validset):
    # move img to new folder
    shutil.move(img, "Trabalho\\Dataset\\Compiled\\Classification\\Valid\\")

for id, img in enumerate(testset):
    # move img to new folder
    shutil.move(img, "Trabalho\\Dataset\\Compiled\\Classification\\Test\\")
