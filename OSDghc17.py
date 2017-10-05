#from sklearn.feature_extraction.text import CountVectorizer
#from pandas import DataFrame
#import numpy
import json


def extraction(FILE):
    with open(FILE, 'r') as data:
        #returns array of dictionaries
        #each dictionary is a paper
        #each dictionary key is a field
        classified_data = json.load(data)
        for paper in classified_data:
            paper.pop('abstract')
    return classified_data
    
def vectorize(data):    
    count_vectorizer = CountVectorizer()
    counts = count_vectorizer.fit_transform(data['text'].values)
    
def createDF(data):
    #TODO iterate over dictionaries
    frame = DataFrame()
    for dictionary in data:
        #need to append each dataFrame to the last
        frame.append(DataFrame.from_dict(dictionary, orient='title'))
    print frame

def main():
    print("Hello world");
    
    data = extraction('C:\Users\Emily\dev\OSD-COS\classified_preprints.json')
    vect_data = vectorize(data)
    createDF(data)