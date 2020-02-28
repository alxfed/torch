# -*- coding: utf-8 -*-
"""...
"""
from __future__ import print_function
import torch


def main():
    # check the version of PyTorch
    print(torch.__version__)

    x = torch.rand(5, 3)
    print(x)

    print('\nCUDA is available?  ', torch.cuda.is_available())

    return


if __name__ == '__main__':
    main()
    print('\ndone')