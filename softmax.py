from builtins import range
import numpy as np
from random import shuffle
from past.builtins import xrange

def softmax_loss_naive(W, X, y, reg):
    """
    Softmax loss function, naive implementation (with loops)

    Inputs have dimension D, there are C classes, and we operate on minibatches
    of N examples.

    Inputs:
    - W: A numpy array of shape (D, C) containing weights.
    - X: A numpy array of shape (N, D) containing a minibatch of data.
    - y: A numpy array of shape (N,) containing training labels; y[i] = c means
      that X[i] has label c, where 0 <= c < C.
    - reg: (float) regularization strength

    Returns a tuple of:
    - loss as single float
    - gradient with respect to weights W; an array of same shape as W
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using explicit loops.     #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    num_train = X.shape[0]
    num_features = W.shape[1]
    sco = X.dot(W)
    for i in range(num_train):
      exp_sum = np.sum(np.exp(sco[i,:]))
      yi_sco = sco[i,y[i]]
      loss = loss-np.log(np.exp(yi_sco)/exp_sum)
      dW[:,y[i]] = dW[:,y[i]]-X[i]
      for j in range (num_features):
        dW[:,j] = dW[:,j]+np.exp(sco[i,j])/exp_sum*X[i,:]
    loss = loss/num_train+0.5*reg*np.sum(W*W)
    dW = dW/num_train+reg*W
    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
    """
    Softmax loss function, vectorized version.

    Inputs and outputs are the same as softmax_loss_naive.
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    num_train = X.shape[0]
    sco = X.dot(W)
    exp_sco = np.exp(sco)
    loss = np.sum(-np.log(exp_sco[np.arange(num_train),y]/np.sum(exp_sco,axis = 1)))
    loss = loss/num_train+0.5*reg*np.sum(W*W)
    sum_exp = np.sum(exp_sco,axis = 1)
    
    margin = exp_sco/sum_exp.reshape([-1,1])
    margin[np.arange(num_train),y] = margin[np.arange(num_train),y]-1
    dW = X.T.dot(margin)/num_train+reg*W
    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW
