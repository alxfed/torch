# -*- coding: utf-8 -*-
"""...
"""
import torch


def main():
    roberta = torch.hub.load('pytorch/fairseq', 'roberta.large')
    roberta.eval()  # disable dropout (or leave in train mode to finetune)

    tokens = roberta.encode('Hello world!')
    assert tokens.tolist() == [0, 31414, 232, 328, 2]
    assert roberta.decode(tokens) == 'Hello world!'

    # Extract the last layer's features
    last_layer_features = roberta.extract_features(tokens)
    assert last_layer_features.size() == torch.Size([1, 5, 1024])

    # Extract all layer's features (layer 0 is the embedding layer)
    all_layers = roberta.extract_features(tokens, return_all_hiddens=True)
    assert len(all_layers) == 25
    assert torch.all(all_layers[-1] == last_layer_features)


    return


if __name__ == '__main__':
    main()
    print('main - done')