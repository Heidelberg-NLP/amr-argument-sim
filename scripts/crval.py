import numpy as np 
from sklearn.metrics import f1_score
from random import shuffle


def find_threshold(candidates, X, Y):
            
    high_score = 0.0
    threshold = 0.0
    for t in candidates:
        x_copy = X.copy()
        x_copy[X<t] = 0
        x_copy[X>=t] = 1
        score = f1_score(x_copy, Y, average="macro")
        if score > high_score:
            high_score = score
            threshold = t
    
    return threshold

def score_test(threshold, X, Y):
    x_copy = X.copy()
    x_copy[X<threshold] = 0
    x_copy[X>=threshold] = 1
    score_macro = f1_score(x_copy, Y, average="macro")
    score_1 = f1_score(x_copy, Y, pos_label=1)
    score_0 = f1_score(x_copy, Y, pos_label=0)
    return score_macro, score_1, score_0

def runcv(ybar, y, topics):
    
    #define possible thresholds 0.01, 0.02, ...
    trs = np.linspace(0, 1.0, 100)
    
    topicids = list(set(topics))
     
    out1 = []
    out2 = []
    out3 = []

    # do 10 random runs
    for _ in range(10):
        out1t = []
        out2t = []
        out3t = []

        #shuffle topics
        shuffle(topicids)

        #threshold cross validation over topics
        for i in range(0, 28, 7):
        
            #split train/test
            tet = topicids[i:i+7]
            trt = topicids[0:i] + topicids[i+7:]
            ybar_train = [ybar[i] for i in range(len(topics)) if topics[i] in trt]
            ybar_test = [ybar[i] for i in range(len(topics)) if topics[i] in tet]
            y_train = [y[i] for i in range(len(topics)) if topics[i] in trt]
            y_test = [y[i] for i in range(len(topics)) if topics[i] in tet]
            
            # to numpy array
            ybar_train = np.array(ybar_train)
            ybar_test = np.array(ybar_test)
            y_train = np.array(y_train)
            y_test = np.array(y_test)
            
            threshold = find_threshold(trs, ybar_train, y_train)
            score_macro, score_1, score_0 = score_test(threshold, ybar_test, y_test) 
            
            # collect result for test fold
            out1t.append(score_macro)
            out2t.append(score_1)
            out3t.append(score_0)
        
        #collect average over 4 different test folds 
        out1.append(np.mean(out1t))
        out2.append(np.mean(out2t))
        out3.append(np.mean(out3t))

    #average over random runs, print
    print("final score", np.mean(out1), "&", np.mean(out2), "&", np.mean(out3))
    print("final score", formatt(out1, out2, out3))

def formatt(x, y, z):
    stringx = str(round(np.mean(x)*100, 2)) +"$^{\pm "+ str(round(np.std(x)*100, 1)) + "}$"
    stringy = str(round(np.mean(y)*100, 2)) +"$^{\pm "+ str(round(np.std(y)*100, 1)) + "}$"
    stringz = str(round(np.mean(z)*100, 2)) +"$^{\pm "+ str(round(np.std(z)*100, 1)) + "}$"
    return stringx + " & " +stringy + " & "+ stringz 


