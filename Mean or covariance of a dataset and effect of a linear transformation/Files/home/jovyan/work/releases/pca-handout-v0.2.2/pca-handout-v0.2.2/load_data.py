from six.moves import urllib
import os

def load_mnist(data_home='.'):
    mnist_path = os.path.join(data_home, "mnist-original.mat")
    from scipy.io import loadmat
    mnist_raw = loadmat(mnist_path)
    mnist = {
        "data": mnist_raw["data"].T,
        "target": mnist_raw["label"][0],
        "COL_NAMES": ["label", "data"],
        "DESCR": "mldata.org dataset: mnist-original",
    }
    return mnist