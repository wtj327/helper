#! /usr/bin/env python
# -*- coding: utf-8 -*-

import helper

# Test class Counting
counting = helper.Counting()
frequency_distribution = counting.pdt_toss_n_dice(2, 6)
print(frequency_distribution)
relative_frequency_distribution = counting.pdt_toss_n_dice(2, 6, rf = True)
print(relative_frequency_distribution)
print()

# Test class Visualize
visualize = helper.Visualize()
visualize.bar_chart_frequency(frequency_distribution)













