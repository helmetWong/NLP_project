from wordCloud_FN import *

def main():
    print (remove_http.__doc__)
    print ("*"*105)
    print (df_remove_http.__doc__)
    print ("*"*105)
    print (remove_punctuation.__doc__)
    print ("*"*105)
    print (df_remove_punctuation.__doc__)
    print ("*"*105)
    print (df_lowerCase.__doc__ )
    print ("*"*105)
    print (tokenization.__doc__)
    print ("*"*105)
    print (df_tokenization.__doc__)
    print ("*"*105)
    print (remove_stopwords.__doc__)
    print ("*"*105)
    print (df_remove_stopwords.__doc__)
    print ("*"*105)
    print (lemmatizer.__doc__)
    print ("*"*105)
    print (df_lemmatizer.__doc__)
    print ("*"*105)
    print (remove_emoji.__doc__)


def saveDocString(filename):
    
    with open (filename, "w") as f:
        f.write('\n'+ (remove_http.__doc__).strip() +'\n\n'+'*'*105 + '\n')
        f.write('\n'+ (df_remove_http.__doc__).strip() +'\n\n'+'*'*105 + '\n')
        f.write('\n'+ (remove_punctuation.__doc__).strip() +'\n\n'+'*'*105 + '\n')
        f.write('\n'+ (df_remove_punctuation.__doc__).strip() +'\n\n'+'*'*105 + '\n')
        f.write('\n'+ (df_lowerCase.__doc__).strip() +'\n\n'+'*'*105 + '\n')
        f.write('\n'+ (tokenization.__doc__).strip() +'\n\n'+'*'*105 + '\n')
        f.write('\n'+ (df_tokenization.__doc__).strip() +'\n\n'+'*'*105 + '\n')
        f.write('\n'+ (remove_stopwords.__doc__).strip() +'\n\n'+'*'*105 + '\n')
        f.write('\n'+ (df_remove_stopwords.__doc__).strip() +'\n\n'+'*'*105 + '\n')
        f.write('\n'+ (lemmatizer.__doc__).strip() +'\n\n'+'*'*105 + '\n')
        f.write('\n'+ (df_lemmatizer.__doc__).strip() +'\n\n'+'*'*105 + '\n')
        f.write('\n'+ (remove_emoji.__doc__).strip() +'\n\n'+'*'*105 + '\n')


if __name__ =="__main__":
    main()
    saveDocString('help.txt')
