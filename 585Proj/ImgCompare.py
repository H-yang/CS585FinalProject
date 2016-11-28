import numpy as np
from PIL import Image
from PIL import ImageChops
from PIL import ImageOps
import PIL
import os

height = 662
width = 1366

def getImgList(browser):
    path = "./" + browser + "/"
    list = os.listdir(path)
    return list

def num_imgs_match(FF, CH):
    return FF == CH


def adjust(img):
    if(img.height < height or img.width < width):
        # print 'do padding'
        new_size = (width, height)
        padded_img = Image.new("RGB", new_size)
        padded_img.paste(img, (0, 0))

        return padded_img
    else:
        return img

def compare(ch_img, ff_img):

    diff = ImageChops.subtract(ch_img, ff_img)
    diff = ImageOps.invert(diff)




    return diff

def add_layer_to_base(ch_img, diff):
    new_img = Image.blend(ch_img, diff, 0.2)
    return new_img

def concat(ch_img, ff_img, diff, pic_name):
    # list_im = [ch_img, ff_img]
    imgs = [ch_img, ff_img]
    # pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
    min_shape = sorted([(np.sum(i.size), i.size) for i in imgs])[0][1]
    imgs_combine_ch_ff = np.hstack((np.asarray(i.resize(min_shape)) for i in imgs))

    # save that beautiful picture
    imgs_combine_ch_ff = PIL.Image.fromarray(imgs_combine_ch_ff)
    # f_name = str(pic_name) + '.png'
    imgs_combine_ch_ff.save(pic_name)




def run():
    CH_imgs_list = getImgList('CH')
    FF_imgs_list = getImgList('FF')
    is_numbers_match = num_imgs_match(len(FF_imgs_list), len(CH_imgs_list))

    if(not is_numbers_match):
        print 'ERROR'
    else:
        CH_imgs_list = sorted(CH_imgs_list)
        FF_imgs_list = sorted(FF_imgs_list)

        dir_CH = "./CH/"
        dir_FF = "./FF/"
        dir_cmp = "./cmp/"

        for i in xrange(len(FF_imgs_list)):
            # print CH_imgs_list[i]
            # print FF_imgs_list[i]
            ch_img = Image.open(dir_CH+CH_imgs_list[i])
            ff_img = Image.open(dir_FF+FF_imgs_list[i])
            ch_img = adjust(ch_img)
            ff_img = adjust(ff_img)

            diff = compare(ch_img, ff_img)
            new_diff = add_layer_to_base(ch_img, diff)
            diff_file_name = dir_cmp + str(CH_imgs_list[i]) + '-diff.png'
            new_diff.save(diff_file_name)

            concat_pic_name = dir_cmp + str(CH_imgs_list[i]) + '.png'
            concat(ch_img, ff_img, diff, concat_pic_name)

if __name__ == "__main__":
    run()
    print 'DONE!'
    cmp_imgs_list = getImgList('cmp')
    os.system('start' + './cmp/' + cmp_imgs_list[0])