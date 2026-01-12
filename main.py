from manim import * 
import numpy as np
from manim.mobject.three_d.three_dimensions import Arrow3D

class Vectors(ThreeDScene):
  def construct(self):
    axes = ThreeDAxes()
    axes.x_axis.set_color(RED)
    axes.y_axis.set_color(BLUE)
    axes.z_axis.set_color(GREEN)
    self.add(axes)
    plane = NumberPlane().set_opacity(0.1)
    self.add(plane)


    # THE MATH 
    np.random.seed(0)
    N = 4
    n = 3
    X = np.random.randn(N, n)
    Xc = X - X.mean(0, keepdims=True)
    A, B, C = np.linalg.svd(Xc, full_matrices=False)

    k = 2
    Xp = Xc @ C[:k, :].T # (N,n) @ (k, n).T = (N, k)
    Xr = Xp @ C[:k, :] # (N, k) @ (k, n) = (N, n)



    #Visualize the principal components
    colors = [PURE_RED, PURE_BLUE, PURE_GREEN] 
    pcs = []
    for i, pc in enumerate(C):
      vec = Arrow3D(start=ORIGIN, end=pc, color=colors[i], base_radius=0.05, thickness=0.05)
      pcs.append(vec)
    self.add(*pcs)


    # VIsualize the vectors 
    vs = []
    for i in range(N):
      vec = Vector(Xc[i])
      vec = Arrow3D(start=ORIGIN, end=Xc[i], base_radius=0.05, thickness=0.01, color=BLUE)
      vs.append(vec)
    self.add(*vs)






    def viewer(C):
      def move_camera(v1, v2):
        normal = np.cross(v1, v2)
        normal = normal / np.linalg.norm(normal)
        nx, ny, nz = normal
        theta = np.arctan2(nx, ny)
        phi = np.arccos(nz)
        self.move_camera(phi=phi, theta=theta, run_time=1)

      move_camera(C[0], C[1])
      move_camera(C[1], C[0])
      self.wait(1)
      move_camera(C[1], C[2])
      move_camera(C[2], C[1])
      self.wait(1)
      move_camera(C[2], C[0])
      move_camera(C[0], C[2])
    viewer(C)
