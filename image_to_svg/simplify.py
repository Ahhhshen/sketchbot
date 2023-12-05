import torch
from torch.nn import Sequential, Module
from torchvision import transforms
from torchvision.utils import save_image

from PIL import Image, ImageStat
import argparse
import os  # Import the os module

parser = argparse.ArgumentParser(description='Sketch simplification demo.')
parser.add_argument('--model', type=str, default='model_gan', help='Model to use.')
parser.add_argument('--img', type=str, default='test.png', help='Input image file.')
parser.add_argument('--out', type=str, default='out.png', help='File to output.')
opt = parser.parse_args()

model_import = __import__(opt.model, fromlist=['model', 'immean', 'imstd'])
model = model_import.model
immean = model_import.immean
imstd = model_import.imstd

use_cuda = torch.cuda.device_count() > 0

model.load_state_dict(torch.load(opt.model + ".pth"))
model.eval()

data = Image.open(opt.img).convert('L')
w, h = data.size[0], data.size[1]
pw = 8 - (w % 8) if w % 8 != 0 else 0
ph = 8 - (h % 8) if h % 8 != 0 else 0
stat = ImageStat.Stat(data)

data = ((transforms.ToTensor()(data) - immean) / imstd).unsqueeze(0)
if pw != 0 or ph != 0:
    data = torch.nn.ReplicationPad2d((0, pw, 0, ph))(data).data

# Get the absolute path for the output file
output_file_path = os.path.abspath(opt.out)

if use_cuda:
    pred = model.cuda().forward(data.cuda()).float()
else:
    pred = model.forward(data)

# Save the image to the specified output file path
save_image(pred[0], output_file_path)
