
import quadprog
import numpy as np
class mySVM:
    def __init__(self,lmd, kernel):
        self.alpha=[] # weights
        self.lmd=lmd # regularization parameter
        self.kernel = kernel

    # compute the kernel of the data
    def kernel0(self,X):
        return X

    # fit the model to data
    def fit(self, X,Y):
        K = self.kernel.compute(X) # Compute the kernel of the data
        self.alpha = quadprog.solve_qp(H=K, f=2 * Y, A=[], b=[], Aeq=[], beq=[], lb=np.zeros(len(Y), 1),
                                       ub=np.repeat(1 / (self.lmd * 2 * len(Y)), len(Y)))

    # predict on data
    def predict(self,data):
        f = np.empty(len(data))
        for i in range(len(data)):
            f[i] = np.sum(self.alpha[i]*self.K[:,i])

        return f


    # compute prediction accuracy
    def score(self,pred,true):
        mse=np.sum((pred-true)**2)/len(true)
        return mse

