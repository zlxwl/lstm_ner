import os
import jieba
import logging
import gensim


def read_files(filepath):
    filelist = []
    for root, dirs, files in os.walk(filepath):
        for file in files:
            filelist.append(os.path.join(root, file))
    return filelist


def _readfile(path):
    '''
        文件读写函数
        :param path: 文件路径
        :return:
        '''
    with open(path, "r", encoding='gbk') as fp:
        content = fp.read()
    return content


def segment(seg_path_input, seg_path_output, stopwords):
    file_nums = 0
    fileNames = os.listdir(seg_path_input)
    print(len(fileNames))
    for file in fileNames: # 遍历每个文件
        # 日志信息
        logging.info('starting ' + str(file_nums) + 'file word Segmentation')
        with open(seg_path_output + "seg_" + file, 'w', encoding='GBK', errors="ignore") as f1:
        # 每个文件单独处理
            with open(seg_path_input + "\\" + file, "r", encoding='GBK', errors="ignore") as f2:
                text = f2.readlines()
                for sentence in text:
                    sentence = list(jieba.cut(sentence))
                    sentence_segment = [word for word in sentence if word not in stopwords]
                    f1.write(" ".join(sentence_segment))
        # 日志信息
        logging.info('finished ' + str(file_nums) + 'file word Segmentation')
        file_nums += 1


# def train_word2vec(corpus, ou)



if __name__ == '__main__':
    logging.basicConfig(level="INFO")
    stopwords_path = 'stopwordsRemind.txt'
    seg_path_input = "C:\\skipgram-gpu\\查件\\查件"
    seg_path_output = "C:\\skipgram-gpu\\seg_out\\"
    stopwords = _readfile(stopwords_path).splitlines()
    segment_file = segment(seg_path_input, seg_path_output, stopwords)


    # from gensim.models import Word2Vec
    # from gensim.models.word2vec import LineSentence
    # input_corpus = "C:\\skipgram-gpu\\查件\\查件\\16561254.txt"
    # output_model = "models/model.model"
    # output_vector = "models/vector.vector"

    # model = Word2Vec(LineSentence(input_corpus), size=50, window=5, min_count=5)
    # model.save(output_model)
    # model.wv.save_word2vec_format(output_model, binary=False)
    # print(stopwords)
