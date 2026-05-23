from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot
import unittest
import test_module

draw_line_plot()
draw_bar_plot()
draw_box_plot()

unittest.main(module='test_module', exit=False)