import src.mnist_loader as loader
import src.network as network
if __name__ == '__main__':
    training_data, validation_data, test_data = loader.load_data_wrapper()
    net=network.Network([784,30,10])
    a=list(training_data)
    b=list(test_data)
    net.SGD(a,30,10,3.0,test_data=b)
