
# 已知四元数
# from scipy.spatial.transform import Rotation as R
# quaternion = [-0.579229, 0.579229, -0.405579, 0.405579]
# r = R.from_quat(quaternion)
# euler_angles = r.as_euler('ZYX', degrees=True)
# print("欧拉角 (Z-Y-X顺序，单位：度)：", euler_angles)
# rotation_matrix = r.as_matrix()
# print("旋转矩阵：\n", rotation_matrix)

# 已知旋转角
# from scipy.spatial.transform import Rotation as R
# import numpy as np
# euler_angles_deg = [-90, 0, -110]
# euler_angles_rad = np.radians(euler_angles_deg)
# r = R.from_euler('ZYX', euler_angles_rad)
# quaternion = r.as_quat()
# print("四元数：", quaternion)
# rotation_matrix = r.as_matrix()
# print("旋转矩阵：\n", rotation_matrix)

# 已知旋转矩阵
# from scipy.spatial.transform import Rotation as R
# rotation_matrix = [[0, -0.342024, 0.939691],
#                    [-1, 0, 0],
#                    [0, -0.939691, -0.342024]]
# r = R.from_matrix(rotation_matrix)
# quaternion = r.as_quat()
# print("四元数：", quaternion)
# euler_angles = r.as_euler('ZYX', degrees=True)
# print("欧拉角：", euler_angles)

# base2footprint_transform_matrix:    
#    0.994898           0   -0.100887           0
# 0.000850998    0.999964  0.00839213           0
#    0.100883 -0.00843516    0.994862     0.33751

