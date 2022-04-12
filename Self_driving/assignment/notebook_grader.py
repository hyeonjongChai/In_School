import numpy as np
import matplotlib.pyplot as plt

class BicycleSolution:

    def __init__(self):
        self.xc = 0
        self.yc = 0
        self.theta = 0
        self.delta = 0
        self.beta = 0
        self.L = 2
        self.lr = 1.2
        self.w_max = 1.22
        self.sample_time = 0.01

    def reset(self):
        self.xc = 0
        self.yc = 0
        self.theta = 0
        self.delta = 0
        self.beta = 0

    def step(self, v, w):
        self.xc = self.xc + v * np.cos(self.theta + self.beta) * self.sample_time
        self.yc = self.yc + v * np.sin(self.theta + self.beta) * self.sample_time
        self.theta = self.theta + ((v * np.cos(self.beta) * np.tan(self.delta)/self.L)) * self.sample_time
        self.delta = w * self.sample_time + self.delta
        self.beta = np.arctan((self.lr / self.L) * np.tan(self.delta))


def l2_squared(v, w):
    """
    Compute the squared distance between 2 1D vectors v and w
    Output D is a NxM matrix, where N = dim(v) and M = dim(w)
    D(n,m) = (v_n - w_m)^2
    """
    v = v.reshape([-1, 1])
    w = w.reshape([1, -1])
    v_mat = np.tile(v, w.shape[0])
    w_mat = np.tile(w, (v.shape[0], 1))
    D = (v_mat - w_mat) ** 2
    return D


def grade_bicycle(t_data, v_data, w_data):
    """
    Grades the user input based on the trajectory generated by the solution model.

    Solution passes if:
    The trajectory is close to waypoints.
    Pass conditions are set by a distance threshold and percentage correct.
    """
    model = BicycleSolution()
    solution = np.zeros([t_data.shape[0], 2])
    for i in range(t_data.shape[0]):
        solution[(i, 0)] = model.xc
        solution[(i, 1)] = model.yc
        model.step(v_data[i], w_data[i])

    angles = np.linspace(0, 2 * np.pi, 20)
    circ1 = np.vstack((np.cos(angles) * 8 - 0.5, np.sin(angles) * 8 + 8)).T
    circ2 = np.vstack((np.cos(angles) * 8 + 15.5, np.sin(angles) * 8 + 8)).T
    waypoints = np.vstack((circ1, circ2))
    N = waypoints.shape[0]
    results = {'d_thresh':1.5,
     'pass_percentage':80,
     'solution':solution,
     'waypoints':waypoints,
     'dists2':np.zeros((N, 1)),
     'inds':np.zeros((N, 1), dtype='int32'),
     'pass_dist':True}
    results['dists2'] = l2_squared(waypoints[:, 0], solution[:, 0]) + l2_squared(waypoints[:, 1], solution[:, 1])
    results['inds'] = np.argmin(results['dists2'], 1)
    results['dists2'] = np.min(results['dists2'], 1)
    dists_correct = results['dists2'] ** 0.5 <= results['d_thresh']
    percent_correct = np.sum(dists_correct) / N * 100
    if percent_correct < results['pass_percentage']:
        feedback = 'Assessment failed, your trajectory deviates too much or your model is incorrect.\nOnly {}% of the waypoints were met, 80% needed to pass.'.format(percent_correct)
    else:
        feedback = 'Assessment passed! Your trajectory meets {}% of the waypoints.'.format(percent_correct)
    print(feedback)
    fig, ax = plt.subplots()
    plt.plot((results['waypoints'][:, 0]), (results['waypoints'][:, 1]), '*', label='Waypoints')
    plt.plot((results['solution'][:, 0]), (results['solution'][:, 1]), label='Trajectory')
    for i in range(results['waypoints'].shape[0]):
        center = (
         results['waypoints'][(i, 0)], results['waypoints'][(i, 1)])
        circle = plt.Circle(center, (results['d_thresh']), color='g', fill=False)
        ax.add_artist(circle)

    plt.legend()
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.title('Waypoints and Trajectory Generated')
    plt.show()


if __name__ == '__main__':
    pass