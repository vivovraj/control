import numpy as np
from numpy import linalg, sin, cos, pi

class FK():
    def __init__(self):
        pass

    def forward(self, q: np.ndarray) -> np.ndarray:
        """
        Calculates the forward kinematics of the center of the motion stage with respect to the world frame

        INPUTS: 
        q - joint positions [x_stage, y_stage, theta_stage]

        OUTPUTS: 
        H_center_world
        """

        return np.zeros((4, 4))
