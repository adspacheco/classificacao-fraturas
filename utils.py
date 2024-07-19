import os
import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance, ImageOps
import shutil
import random
from keras.utils import img_to_array, load_img
import numpy as np
from tqdm import tqdm
from keras_visualizer import visualizer
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

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

def plot_nn(model, settings={}):
    visualizer(model, file_name='/tmp/output', file_format='png', view=True, settings=settings)
    img = Image.open('/tmp/output.png')
    return img

def plot_history(history):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    ax1.plot(history.history['loss'], 'r-', label='train loss')
    ax1.plot(history.history['val_loss'], 'b--', label='test loss')
    ax1.set_title('Model Loss')
    ax1.set_xlabel('Epochs')
    ax1.set_ylabel('Loss')

    ax1.legend()

    ax2.plot(history.history['accuracy'], 'r-', label='train acc')
    ax2.plot(history.history['val_accuracy'], 'b--', label='test acc')
    ax2.set_title('Model Accuracy')
    ax2.set_xlabel('Epochs')
    ax2.set_ylabel('Accuracy')
    ax2.legend()

    plt.tight_layout()

def plot_confusion_matrix_with_sums(true_labels, predicted_labels, figsize=(10, 7), cmap='viridis', text_color='blue'):
    cm = confusion_matrix(true_labels, predicted_labels)
    sum_per_class = np.sum(cm, axis=1)

    fig, ax = plt.subplots(figsize=figsize)

    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=np.unique(true_labels))
    disp.plot(ax=ax, cmap=cmap, xticks_rotation=45)

    for i, total in enumerate(sum_per_class):
        ax.text(len(disp.display_labels)-0.5, i, f'{total}', va='center', ha='left', fontsize=12, color=text_color)

    plt.xticks(rotation=45, ha='right')

    plt.show()

def plot_images_with_titles(df, rows=2, cols=2, figsize=(8, 8)):
    fig, axes = plt.subplots(rows, cols, figsize=figsize)
    fig.subplots_adjust(hspace=0.4, wspace=0.4)

    for i, ax in enumerate(axes.flat):
        if i < len(df):
            img = plt.imread(df.full_path.iloc[i])
            ax.imshow(img, cmap='gray')
            ax.set_title(f'{df.target.iloc[i]} | Pred: {df.predicted_class.iloc[i]} ({df.target_proba.iloc[i]:.3f})')
            ax.axis('off') 

    plt.show()

def random_transform(image):
    if random.random() > 0.5:
        angle = random.randint(-30, 30)
        image = image.rotate(angle)

    if random.random() > 0.5:
        image = ImageOps.mirror(image)

    if random.random() > 0.5:
        image = ImageOps.flip(image)
    return image

def save_augmented_images(img_path, class_label, count):
    img = Image.open(img_path) 

    save_to_dir = os.path.join(AUG_DIR_PATH, class_label)
    os.makedirs(save_to_dir, exist_ok=True)

    prefix = os.path.splitext(os.path.basename(img_path))[0]

    for i in range(count):
        augmented_img = random_transform(img)
        augmented_img.save(os.path.join(save_to_dir, f"{prefix}_aug_{i}.jpg"))

def count_files_in_directory(base_path, classes):
    counts = {'train': {}, 'test': {}}
    for split in ['train', 'test']:
        for cls in classes:
            dir_path = os.path.join(base_path, split, cls)
            if os.path.exists(dir_path):
                counts[split][cls] = len(os.listdir(dir_path))
            else:
                counts[split][cls] = 0
    return counts

def random_transform(image):
    if random.random() > 0.5:
        angle = random.randint(-30, 30)
        image = image.rotate(angle)

    if random.random() > 0.5:
        image = ImageOps.mirror(image)

    if random.random() > 0.5:
        image = ImageOps.flip(image)
    return image

def save_augmented_images(img_path, class_label, count, start_index, aug_base_path):
    img = Image.open(img_path)

    save_to_dir = os.path.join(aug_base_path, 'train', class_label)
    os.makedirs(save_to_dir, exist_ok=True)

    prefix = os.path.splitext(os.path.basename(img_path))[0]

    for i in range(count):
        augmented_img = random_transform(img)
        augmented_img.save(os.path.join(save_to_dir, f"AUG_{prefix}_{start_index + i}.jpg"))

def copy_files(src_dir, dest_dir):
    for file_name in os.listdir(src_dir):
        full_file_name = os.path.join(src_dir, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest_dir)
