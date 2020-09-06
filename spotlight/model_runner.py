import os

from PIL import Image

from model.data import create_dataset
from model.models import create_model
from model.options.test_options import TestOptions
from model.util import util

opt = None
model = None


def load():
    global opt
    global model

    opt = TestOptions().parse()
    opt.num_threads = 0
    opt.batch_size = 1
    opt.serial_batches = True
    opt.no_flip = True
    opt.display_id = -1
    opt.name = "night2day"
    opt.model = "test"
    opt.no_dropout = True
    opt.preprocess = "none"
    opt.checkpoints_dir = os.environ["CHECKPOINTS_DIR"]

    model = create_model(opt)
    model.setup(opt)
    model.eval()


def run(image_dir_path):
    global opt
    global model

    opt.dataroot = image_dir_path
    dataset = create_dataset(opt)
    for data in dataset:
        model.set_input(data)
        model.test()
        visuals = model.get_current_visuals()
        for label, im_data in visuals.items():
            if label != "fake":
                continue
            im = util.tensor2im(im_data)
            image_pil = Image.fromarray(im)
            return image_pil
