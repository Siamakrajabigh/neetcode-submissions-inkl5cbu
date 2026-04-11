
import numpy as np
import numpy.typing as NDArray

class Solution :
    def softmax(self, z:NDArray[np.float64]) -> NDArray[np.float64] :
        num_result = (np.exp(z - np.max(z)))
        denum_result = np.sum(np.exp(z - np.max(z)))
        result = num_result / denum_result
        return np.round(result, 4)
