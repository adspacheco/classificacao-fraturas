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
