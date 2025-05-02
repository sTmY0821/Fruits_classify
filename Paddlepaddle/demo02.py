import paddle.fluid as fluid
import numpy as np

def reader_creator(corpus_path):
    def reader():
        for line in open(corpus_path, 'r',encoding='utf-8'):
            content = line.strip()
            yield content
    return reader