import numpy as np

def decide_label(string):
    dic = {'DTORCD':0, 'NS':0, 'SS':1, 'HS':1}
    return dic[string]


def get_data(p="../data/UKP_ASPECT.tsv"):
    x_src_all = []
    x_tgt_all = []
    x_topic_all = []
    y_all = []
    with open(p) as f:
        content = [l for l in f.read().split("\n") if l]
    for line in content[1:]:
        line = line.split("\t")
        x_src_all.append(line[1])
        x_tgt_all.append(line[2])
        x_topic_all.append(line[0])
        y_all.append(decide_label(line[3]))
    return x_src_all, x_tgt_all, x_topic_all, y_all        


def get_preds(fip):
    ybar = []
    with open(fip, "r") as f:
        lines = f.read().split("\n")
    if "s2match" in fip:
        # the smatch script outputs 3 extra lines at the end
        last = -3
        first = 1
    else:
        # otherwise it's a normal score file over the UKP_aspect file lines
        last = len(lines)
        first = 1
    for li in lines[first:last]:
        if "s2match" in fip:
            ybar.append([float(x) for x in li.replace("Smatch score F1 ","").split(" ")])
        else:
            ybar.append([float(li)])
    return np.array(ybar)

if __name__ == "__main__":
    
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-predictions_premises", type=str, default=None
                        , help="path to file where one line contains a similarity score")
    parser.add_argument("-predictions_conclusions", type=str, default=None
                        , help="path to file where one line contains a similarity score")
    parser.add_argument("-mixing_value", type=float, nargs="?", default=0.95
                        , help="mixing value: weight of premise sim vs. conclusion sim")
    args = parser.parse_args()
    
    x_src, x_tgt, x_topic, y = get_data()
    
    ratings_p = None
    ratings_c = None
    
    mix_value = args.mixing_value

    if args.predictions_premises != None:
        ratings_p = get_preds(args.predictions_premises)
    if args.predictions_conclusions != None:
        ratings_c = get_preds(args.predictions_conclusions)

    if ratings_p is None:
        ratings_p = np.zeros((len(y), 1))
        mix_value = 0.0
    if ratings_c is None:
        ratings_c = np.zeros((len(y), 1))
        mix_value = 1.0
    
    ratings = (1 - mix_value) * ratings_c + mix_value * ratings_p
    
    from crval import runcv
    runcv(ratings[:,0], y, x_topic)

