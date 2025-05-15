import os
import shutil
import random

# Path awal
original_dataset_dir = 'Dataset/'
base_dir = 'dataset_split/'
os.makedirs(base_dir, exist_ok=True)

# Nama kelas
classes = ['Healthy', 'BacterialSpot']

for cls in classes:
    src_dir = os.path.join(original_dataset_dir, cls)
    all_filenames = os.listdir(src_dir)
    random.shuffle(all_filenames)

    train_size = int(0.8 * len(all_filenames))
    train_filenames = all_filenames[:train_size]
    test_filenames = all_filenames[train_size:]

    for split, split_files in [('train', train_filenames), ('test', test_filenames)]:
        split_dir = os.path.join(base_dir, split, cls)
        os.makedirs(split_dir, exist_ok=True)
        for fname in split_files:
            src_file = os.path.join(src_dir, fname)
            dst_file = os.path.join(split_dir, fname)
            shutil.copy2(src_file, dst_file)
