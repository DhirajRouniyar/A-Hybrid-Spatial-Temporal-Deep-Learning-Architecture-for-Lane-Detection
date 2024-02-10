DEVICE = "cuda"
LR = 0.0001
EPOCH = 10
TRAIN_BATCH_SIZE = 1
TEST_BATCH_SIZE = 1
NUM_WORKERS = 8
class_weight = [0.02, 1.02]
TRAIN_PATH = "../dataset/trainset/train_index_new.txt"
VALIDATION_PATH =  "../dataset/trainset/val_index_new.txt"
TRAINED_WEIGHTS_PATH = "./trained_weights/"
TEST_PATH = "../dataset/testset/test_index_0530.txt"
SAVE_PATH = "./train_save/"
SAVE_PATH_VAL = "./val_save/"
SAVE_PATH_TEST_1 = "./test_save_1/"
SAVE_PATH_TEST_2 = "./test_save_2/"
TRAIN_EVAL_BATCH = 100
