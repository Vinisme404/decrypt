#!/usr/bin/env python
# -*- coding:utf-8 -*-

from PIL import Image


def mod(x, y):

    return x % y


def toasc(strr):

    return int(strr, 2)


def func(le, str1, str2):

    a = ""

    b = ""

    im = Image.open(str1)

    lenth = le * 8

    width = im.size[0]

    height = im.size[1]

    count = 0

    for h in range(0, height):

        for w in range(0, width):

            pixel = im.getpixel((w, h))

            if count % 3 == 0:

                count += 1

                b = b + str((mod(int(pixel[0]), 2)))

                if count == lenth:
                    break

            if count % 3 == 1:

                count += 1

                b = b + str((mod(int(pixel[1]), 2)))

                if count == lenth:
                    break

            if count % 3 == 2:

                count += 1

                b = b + str((mod(int(pixel[2]), 2)))

                if count == lenth:
                    break

        if count == lenth:
            break

    with open(str2, "wb") as f:

        for i in range(0, len(b), 8):

            stra = toasc(b[i:i + 8])

            f.write(chr(stra))

            stra = ""

    f.close()


le = 30


new = "C:/Users/94019/Desktop/Darius.png"

tiqu = "C:/Users/94019/Desktop/getflag.txt"

func(le, new, tiqu)