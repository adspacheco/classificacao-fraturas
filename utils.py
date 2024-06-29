import os
import matplotlib.pyplot as plt
from PIL import Image
import random
from keras.utils import img_to_array, load_img
import numpy as np
from tqdm import tqdm

def validate_and_list_files(base_path):
    all_dirs = os.listdir(base_path)
    all_have_train_test = True
    all_files_jpg = True
    all_files = []

    for dir_name in all_dirs:
        dir_path = os.path.join(base_path, dir_name)
        if os.path.isdir(dir_path):
            train_path = os.path.join(dir_path, 'Train')
            test_path = os.path.join(dir_path, 'Test')
            if os.path.exists(train_path) and os.path.exists(test_path):
                if not (validate_jpg_files(train_path) and validate_jpg_files(test_path)):
                    all_files_jpg = False
                all_files.extend([os.path.join(train_path, file) for file in list_files(train_path)])
                all_files.extend([os.path.join(test_path, file) for file in list_files(test_path)])
            else:
                all_have_train_test = False

    if all_have_train_test and all_files_jpg:
        print("Todos os diretórios possuem 'Train' e 'Test', e todos os arquivos são .jpg, alguns arquivos de exemplo:")
        examples = random.sample(all_files, min(len(all_files), 3))
        print("\nExemplos de arquivos:")
        for example in examples:
            print(example)
            show_image(example)
    else:
        print("Nem todos os diretórios possuem 'Train' e 'Test', ou nem todos os arquivos são .jpg.")

def list_files(dir_path):
    return [file for file in os.listdir(dir_path) if file.lower().endswith('.jpg')]

def validate_jpg_files(dir_path):
    files = os.listdir(dir_path)
    for file in files:
        if not file.lower().endswith('.jpg'):
            return False
    return True

def show_image(image_path):
    image = Image.open(image_path)
    plt.imshow(image)
    plt.axis('off')
    plt.show()

def count_files_and_calculate_percentages(base_path, train_name='Train', test_name='Test'):
    all_dirs = os.listdir(base_path)
    counts = {}

    for dir_name in all_dirs:
        dir_path = os.path.join(base_path, dir_name)
        if os.path.isdir(dir_path):
            train_path = os.path.join(dir_path, train_name)
            test_path = os.path.join(dir_path, test_name)
            if os.path.exists(train_path) and os.path.exists(test_path):
                train_count = count_files(train_path)
                test_count = count_files(test_path)
                total_count = train_count + test_count
                counts[dir_name] = {'Train': train_count, 'Test': test_count, 'Total': total_count}

    for dir_name, count in counts.items():
        train_percentage = (count['Train'] / count['Total']) * 100 if count['Total'] > 0 else 0
        test_percentage = (count['Test'] / count['Total']) * 100 if count['Total'] > 0 else 0
        print(f"Diretório: {dir_name} - Total: {count['Total']}")
        print(f"  Train files: {count['Train']} ({train_percentage:.2f}%)")
        print(f"  Test files: {count['Test']} ({test_percentage:.2f}%)")

    total_train_files = sum(count['Train'] for count in counts.values())
    total_test_files = sum(count['Test'] for count in counts.values())
    total_files = total_train_files + total_test_files

    print("\nResumo:")
    if total_files > 0:
        print(f"  Total Train: {total_train_files} ({(total_train_files / total_files) * 100:.2f}%)")
        print(f"  Total Test: {total_test_files} ({(total_test_files / total_files) * 100:.2f}%)")
    else:
        print("Nenhum arquivo encontrado.")

    return counts

def count_files(dir_path):
    return len([file for file in os.listdir(dir_path) if file.lower().endswith('.jpg')])

def generate_new_dir_name(subdir):
    if subdir.lower() == "fracture dislocation":
        return "fracture_dislocation"
    return subdir.lower().replace(" fracture", "")

def rename_directories_and_files(base_path):
    old_to_new_dir_names = {}
    for subdir in os.listdir(base_path):
        subdir_path = os.path.join(base_path, subdir)
        if os.path.isdir(subdir_path):
            new_subdir_name = generate_new_dir_name(subdir)
            new_subdir_path = os.path.join(base_path, new_subdir_name)
            old_to_new_dir_names[subdir] = new_subdir_name

            if new_subdir_name != subdir:
                os.rename(subdir_path, new_subdir_path)
            else:
                new_subdir_path = subdir_path

            for folder in ['Train', 'Test']:
                folder_path = os.path.join(new_subdir_path, folder)
                if os.path.exists(folder_path):
                    new_folder_path = os.path.join(new_subdir_path, folder.lower())
                    if folder.lower() != folder:
                        os.rename(folder_path, new_folder_path)
                    else:
                        new_folder_path = folder_path

            file_counter = 1
            for folder in ['train', 'test']:
                folder_path = os.path.join(new_subdir_path, folder)
                if os.path.exists(folder_path):
                    for root, _, files in os.walk(folder_path):
                        for file in files:
                            file_ext = os.path.splitext(file)[1]
                            new_file_name = f"{new_subdir_name}_{str(file_counter).zfill(3)}{file_ext}"
                            new_file_path = os.path.join(root, new_file_name)

                            os.rename(os.path.join(root, file), new_file_path)

                            file_counter += 1

    return old_to_new_dir_names

def validate_counts(initial_counts, new_counts, name_mapping):
    for old_dir_name, new_dir_name in name_mapping.items():
        initial_train_count = initial_counts[old_dir_name]['Train']
        initial_test_count = initial_counts[old_dir_name]['Test']
        new_train_count = new_counts[new_dir_name]['Train']
        new_test_count = new_counts[new_dir_name]['Test']

        if initial_train_count != new_train_count or initial_test_count != new_test_count:
            print(f"\nAtenção: A quantidade de arquivos foi alterada para {new_dir_name} após a padronização.")
            return

    print("\nPadronização realizada com sucesso. A quantidade de arquivos permanece inalterada.")


def plot_random_imgs(df, rows=2, columns=5, figsize=(8, 4)):
    fig, axs = plt.subplots(rows, columns, figsize=figsize)
    for i, ax in enumerate(axs.flat):
        idx_img = np.random.choice(list(df.index))
        ax.imshow(plt.imread(df.full_path.iloc[idx_img]))
        ax.set_title(df.target.iloc[idx_img])
        ax.axis('off')
    plt.tight_layout()


def resize_convert_to_array(full_path, img_size=(32, 32)):
    try:
        return img_to_array(load_img(full_path).resize(img_size)) / 255
    except Exception as e:
        print(e)
        return np.array([])

def save_obj(obj, full_path):
    try:
        joblib.dump(obj, full_path)
    except Exception as e:
        print(e)

def load_obj(full_path):
    try:
        obj = joblib.load(full_path)
        return obj
    except Exception as e:
        print(e)

def process_images(df, new_imgs_size):
    imgs_train = []
    targets_train = []
    imgs_test = []
    targets_test = []

    for line in df.itertuples():
        if line.type_dataset == 'train':
            aux_array = resize_convert_to_array(line.full_path, new_imgs_size)
            if len(aux_array) == 0:
                df.loc[line.Index, 'img_processada'] = False
            else:
                imgs_train.append(aux_array)
                targets_train.append(line.target)
                df.loc[line.Index, 'img_processada'] = True
        elif line.type_dataset == 'test':
            aux_array = resize_convert_to_array(line.full_path, new_imgs_size)
            if len(aux_array) == 0:
                df.loc[line.Index, 'img_processada'] = False
            else:
                imgs_test.append(aux_array)
                targets_test.append(line.target)
                df.loc[line.Index, 'img_processada'] = True

    return imgs_train, targets_train, imgs_test, targets_test
