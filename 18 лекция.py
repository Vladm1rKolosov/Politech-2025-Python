# # 17 лекция

# # Классификация
# # 1. Загрузка изображения
# # 2. Масштабирования
# # 3. Нормализация
# # 4. Выбор модели
# # 5. Загрузка изображения в модель и получение предсказаний

# from tensorflow.keras.preprocessing import image
# import matplotlib.pyplot as plt

# img_path = "data/cat.png"

# img = image.load_img(img_path, target_size=(224, 224))

# import numpy as np

# # plt.imshow(img)
# # plt.show()

# img_array = image.img_to_array(img)
# print(img_array.shape)

# print(img_array[100, 100])

# print(np.min(img_array))
# print(np.max(img_array))

# img_batch = np.expand_dims(img_array, axis=0)

# from tensorflow.keras.applications.resnet50 import preprocess_input

# img_preprocessed = preprocess_input(img_batch)
# print(img_preprocessed.shape)

# print(img_preprocessed[0, 100, 100])

# print(np.min(img_preprocessed))
# print(np.max(img_preprocessed))

# from tensorflow.keras.applications.resnet50 import ResNet50

# model = ResNet50()

# prediction = model.predict(img_preprocessed)

# from tensorflow.keras.applications.resnet50 import decode_predictions

# print(decode_predictions(prediction))

# # 17.1 лекция

# # Название папок = название категории

# TRAIN_DATA_DIR = "data/train_data"
# VALIDATION_DATA_DIR = "data/val_data"
# TRAIN_SAMPLES = 500
# VALIDATION_SAMPLE = 500

# # кошка или собака -> кошка или НЕ кошка - бинарная классификация
# # кошка или собака - мультиклассовая классификация

# NUM_CLASSES = 2

# IMG_WIDTH = 224
# IMG_HEIGHT = 224

# # Сколько изображений модель принимает за раз
# BATCH_SIZE = 64

# # Аугментация - процедура увеличения кол - ва данных путем их искажения: повороты, сдвиги, масштабирования

# from tensorflow.keras.preprocessing import image
# from tensorflow.keras.models import Model
# from tensorflow.keras.layers import (
#     Input,
#     Flatten,
#     Dense,
#     Dropout,
#     GlobalAveragePooling2D,
# )

# from tensorflow.keras.applications.mobilenet import MobileNet, preprocess_input
# from tensorflow.keras.optimizers import Adam

# import math

# # аугментация и нормализация
# train_datagen = image.ImageDatagenerator(
#     preprocessing_function=preprocess_input,
#     rotation_range=20,  # 500 * 20 * 2 = 20 000
#     width_shift_range=0.2,
#     height_shift_range=0.2,
#     zoom_range=0.2,
# )

# # только нормализация
# val_datagen = image.ImageDatagenerator(preprocessing_function=preprocess_input)

# train_gen = train_datagen.flow_from_directory(
#     TRAIN_DATA_DIR,
#     target_size=(IMG_WIDTH, IMG_HEIGHT),
#     batch_size=BATCH_SIZE,
#     shuffle=True,
#     seed=1,
#     class_mode="categorical",
# )

# val_gen = train_datagen.flow_from_directory(
#     TRAIN_DATA_DIR,
#     target_size=(IMG_WIDTH, IMG_HEIGHT),
#     batch_size=BATCH_SIZE,
#     shuffle=False,
#     class_mode="categorical",
# )

# model = MobileNet(include_top=False, input_shape=(IMG_WIDTH, IMG_HEIGHT, 3))
# for layer in model.layer[:]:
#     layer.traible = False

# input = Input(shape=(IMG_WIDTH, IMG_HEIGHT, 3))

# custom_model = model(input)
# custom_model = GlobalAveragePooling2D(custom_model)
# custom_model = Dense(64, activation="relu")(custom_model)
# custom_model = Dropout(0.5)(custom_model)
# prediction = Dense(NUM_CLASSES, activation="softmax")(custom_model)

# target_model = Model(inputs=input, outputs=prediction)

# target_model.compile(loss="categorical_crossntropy", optimizer=Adam(), metrics=["acc"])

# num_steps = math.ceil(float(TRAIN_SAMPLES) / BATCH_SIZE)

# model.fit(
#     train_gen,
#     steps_per_epoch=num_steps,
#     epochs=7,
#     validation_data=val_gen,
#     validation_steps=num_steps,
# )

# print(val_gen.class_indices)

# target_model.save("data/our_model.h5")

# 17.2 лекция

from keras.models import load_model

# img_path = "data/cat.png"
# img_path = 'data/dog.png'
img_path = "data/luna.png"

img = image.load_img(img_path, target_size=(224, 224))

model = load_model("data/our_model.h5")

img_array = image.img_to_array(img)
img_batch = np.expand_dims(img_array, axis=0)

from tensorflow.keras.applications.resnet50 import preprocess_input

img_preprocessed = preprocess_input(img_batch)

prediction = model.predict(img_preprocessed)

print(prediction)
