from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np
from keras.optimizers import SGD
from keras import backend as K
K.set_image_dim_ordering('th')
from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
from keras.layers import Input, Flatten, Dense
from keras.models import Model
import numpy as np
# path to the model weights files.
# dimensions of our images.
img_width, img_height = 512, 512

train_data_dir = 'data/train'
validation_data_dir = 'data/validation'
nb_train_samples = 10000
nb_validation_samples = 2000
nb_epoch = 10

base_model = VGG16(weights='imagenet', include_top=False)

input1 = Input(shape=(3,512,512),name = 'image_input')

#Use the generated model 
base_output = base_model(input1)


#x = base_output.output
#x = GlobalAveragePooling2D()(x)
x = Flatten(name='flatten')(base_output)
x = Dense(512, activation='relu')(x)
print x
x = Dense(10, activation='softmax')(x)

# this is the model we will train
model = Model(input=input1, output=x)

for layer in base_model.layers[:25]:
    layer.trainable = False



# prepare data augmentation configuration
model.compile(loss='categorical_crossentropy',
              optimizer=SGD(lr=1e-4, momentum=0.9),
              metrics=['accuracy'])
# this is the augmentation configuration we will use for training
train_datagen = ImageDataGenerator()

# this is the augmentation configuration we will use for testing:
# only rescaling
test_datagen = ImageDataGenerator()

train_generator = train_datagen.flow_from_directory(
        train_data_dir,
        target_size=(img_width, img_height),
        batch_size=50,
        class_mode='categorical')

validation_generator = test_datagen.flow_from_directory(
        validation_data_dir,
        target_size=(img_width, img_height),
        batch_size=50,
        class_mode='categorical')

model.fit_generator(
        train_generator,
        samples_per_epoch=nb_train_samples,
        nb_epoch=nb_epoch,
        validation_data=validation_generator,
        nb_val_samples=nb_validation_samples)
model.save_weights("new_weights.h5")
