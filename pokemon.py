import csv
import glob
import os
import random
from typing import Any


from torch.utils.data import Dataset


class Pokemon(Dataset):
    def __init__(self, root, resize, mode) -> None:
        super().__init__()

        self.root = root
        self.resize = resize
        self.name2label = {}
        for name in sorted(os.listdir(os.path.join(root))):
            if not os.path.isdir(os.path.join(root, name)):
                continue

            self.name2label[name] = len(self.name2label.keys())
            
        print(self.name2label)
        
    def load_csv(self, filename):
        images = []
        for name in self.name2label:
            # 'pokeman/{label}/000001.png'
            images += glob.glob(os.path.join(self.root, name, '*.png'))
            images += glob.glob(os.path.join(self.root, name, '*.jpg'))
            images += glob.glob(os.path.join(self.root, name, '*.jpeg'))
        
        # 1165 ['pokeman/bulbasaur/00000158.png'
        print(len(images), images)
        random.shuffle(images)
        with open(os.path.join(self.root, filename), mode='w', newline='') as f:
            writer = csv.writer(f)
            for img in images:
                name = img.split(os.sep)[-2]
                label = self.name2label[name]
                writer.writerow([img, label])
            print('write into csv file', filename)
            
        

    def __len__(self):
        pass

    def __getitem__(self, index) -> Any:
        return super().__getitem__(index)


def main():
    db = Pokemon("pokeman", 224, 'train')
    db.load_csv('images.csv')
    
    
if __name__ == "__main__":
    main()    
