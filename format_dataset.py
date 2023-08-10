import os
from random import choice
import shutil
def to_v5_directories (images_train_path, images_val_path, labels_train_path, labels_val_path, dataset_source):
    imgs = []
    xmls = []
    trainPath = images_train_path
    valPath = images_val_path
    crsPath =  dataset_source
    train_ratio = 0.8
    val_ratio= 0.2
    totalImgCount = len(os.listdir(crsPath))/2
    for (dirname, dirs, files) in os.walk(crsPath):
        for filename in files:
            if filename.endswith('.txt'):
               xmls.append(filename)
            else:
               imgs.append(filename)
    countForTrain = int(len(imgs)*train_ratio)
    countForVal= int(len(imgs) *val_ratio)
    trainimagePath = images_train_path
    trainlabelPath = labels_train_path
    valimagePath = images_val_path
    vallabelPath = labels_val_path
    for x in range(countForTrain):
        fileJpg = choice(imgs)
        fileXml = fileJpg[:-4]+'.txt'
        shutil.copy(os.path.join(crsPath, fileJpg), os.path.join(trainimagePath, fileJpg))
        shutil.copy(os.path.join(crsPath, fileXml), os.path.join(trainlabelPath, fileXml))
        imgs.remove(fileJpg)
        xmls.remove(fileXml)
    for x in range(countForVal):
        fileJpg = choice(imgs)
        fileXml = fileJpg[:-4] +'.txt'
        shutil.copy(os.path.join(crsPath, fileJpg), os.path.join(valimagePath, fileJpg))
        shutil.copy(os.path.join(crsPath, fileXml), os.path.join(vallabelPath, fileXml))
        imgs.remove(fileJpg)
        xmls.remove(fileXml)
    print("Training images are: ", countForTrain)
    print("Validation images are : ",countForVal)
#    shutil.move(crsPath, valPath)


if __name__ == "__main__":

   to_v5_directories ("/home/shivesh/Downloads/dataset/images/train","/home/shivesh/Downloads/dataset/images/val","/home/shivesh/Downloads/dataset/labels/train","/home/shivesh/Downloads/dataset/labels/val", "/home/shivesh/Downloads/PCB_DATASET/Annotations/Missing_hole")
   to_v5_directories ("/home/shivesh/Downloads/dataset/images/train","/home/shivesh/Downloads/dataset/images/val","/home/shivesh/Downloads/dataset/labels/train","/home/shivesh/Downloads/dataset/labels/val", "/home/shivesh/Downloads/PCB_DATASET/Annotations/Mouse_bite")
   to_v5_directories ("/home/shivesh/Downloads/dataset/images/train","/home/shivesh/Downloads/dataset/images/val","/home/shivesh/Downloads/dataset/labels/train","/home/shivesh/Downloads/dataset/labels/val", "/home/shivesh/Downloads/PCB_DATASET/Annotations/Open_circuit")
   to_v5_directories ("/home/shivesh/Downloads/dataset/images/train","/home/shivesh/Downloads/dataset/images/val","/home/shivesh/Downloads/dataset/labels/train","/home/shivesh/Downloads/dataset/labels/val", "/home/shivesh/Downloads/PCB_DATASET/Annotations/Short")
   to_v5_directories ("/home/shivesh/Downloads/dataset/images/train","/home/shivesh/Downloads/dataset/images/val","/home/shivesh/Downloads/dataset/labels/train","/home/shivesh/Downloads/dataset/labels/val", "/home/shivesh/Downloads/PCB_DATASET/Annotations/Spur")
   to_v5_directories ("/home/shivesh/Downloads/dataset/images/train","/home/shivesh/Downloads/dataset/images/val","/home/shivesh/Downloads/dataset/labels/train","/home/shivesh/Downloads/dataset/labels/val", "/home/shivesh/Downloads/PCB_DATASET/Annotations/Spurious_copper")



