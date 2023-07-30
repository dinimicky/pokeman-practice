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

    def __len__(self):
        pass

    def __getitem__(self, index) -> Any:
        return super().__getitem__(index)


def main():
    db = Pokemon("pokeman", 224, 'train')
    
    
if __name__ == "__main__":
    main()    
