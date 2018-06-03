import pickle
if __name__=='__main__':
    f=open('../data/mnist.pkl/mnist.pkl')
    train,validate,test=pickle.load(open('../data/mnist.pkl/mnist.pkl','rb'),encoding='iso-8859-1')
    print(train[0][0][0])
    print(train[0][10][0])
    print(validate[1][0])
    # for num in train[0]:
    #     print(num,end=' ')
    print(validate[1])
    print(test[1])