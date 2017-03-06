def convert_to_txt(user):
    import pandas as pd
    df = pd.read_csv(user+'_tweets.csv')
    alltext = df.text
    tf = open('input.txt', 'w')
    for each in alltext:
        tf.write(each + '\n')
    tf.close()

convert_to_txt('sama')
