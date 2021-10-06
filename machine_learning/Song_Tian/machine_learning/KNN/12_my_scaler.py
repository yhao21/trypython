import numpy as np

class StandardScaler:

    def __init__(self):
        self.mean_ = None
        self.scale_ = None

    def fit(self,x):
        """根据传入的数据集获得mean和std（scale）"""
        assert x.ndim == 2, 'dataset should be a n by 2 matrix'

        self.mean_ = np.array([np.mean(x[:,i]) for i in range(x.shape[1])])
        self.scale_ = np.array([np.std(x[:,i]) for i in range(x.shape[1])])

        return self

    def transform(self,x):
        """将传入的数据集转换为standardize后的模式"""
        assert x.ndim == 2, 'dataset should be a n by 2 matrix'
        assert self.mean_ is not None and self.scale_ is not None, \
                'you must fit the machine before you transform your dataset!'
        assert x.shape[1] == len(self.mean_), \
                'your dataset must have the same number of columns as what you used to fit'

        #将转换后的x初始状态设为空集，shape与传入的x相同
        output_x = np.empty(shape=x.shape, dtype=float)
        #使用for循环完成每一列的transform
        for col in range(x.shape[1]):
            output_x[:,col] = (x[:,col] - self.mean_[col]) / self.scale_[col]

        return output_x
