#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""This module includes some common helper functions
that I use in everyday work
"""

import itertools
import functools


class Counting(object):
    """Some common counting techniques
    """

    def temp(self):
        """A temporary function that is used to test my temporary thoughts
        """
        pass

    def frequency_distribution(self, L, rf=False):
        """
        :param L: a collection of discrete elements
        :param rf: if True, return relative frequency; if False, return frequency
        :return: a dictionary that list all the values in L with the corresponding frequency
                 or relative frequency of that element
        """
        dict_f = {}  # dict, to store the frequency table
        for e in L:
            if e in dict_f:
                dict_f[e] = dict_f[e] + 1
            else:
                dict_f[e] = 1
        if rf:
            n = len(L)
            for k, v in dict_f.items():
                dict_f[k] = v / n
        return dict_f


    def pdt_toss_n_dice(self, dice_num=1, face_num=6, rf=False):
        """
        :param dice_num: the number of dice tossed at the same time
        :param face_num: the number of faces each die has
        :param rf: if rf = False, return frequency distribution; if rf = True, return relative frequency distribution
        :return: a dictionary that represents the probability distribution table of the random variable
                 which denotes the number of total points of each toss
        example: when dice = 1, face = 6, the output is the probability distribution:
                 {1: 1/6, 2: 1/6, 3: 1/6, 4: 1/6, 5: 1/6, 6: 1/6}
        """
        dices = []  # list, to store all dices, each die is a generator (generating faces)
        dice_total = 0
        while dice_total < dice_num:
            faces = (x for x in range(1, face_num + 1, 1))  # generator, number of total faces per die
            dices.append(faces)
            dice_total += 1
        combinations = itertools.product(*dices)  # all tossing result
        all_sample_points = []  # list, to store all sample points in the sample space
        for result in combinations:
            all_sample_points.append(functools.reduce(lambda x, y: x + y, result))
        if rf:
            return self.frequency_distribution(all_sample_points, True)
        else:
            return self.frequency_distribution(all_sample_points)


class Visualize(object):
    """Some common visualization techniques
    """

    def bar_chart_frequency(self, frequency_dict):
        """
        :param frequency_dict: a dict represents a frequency distribution
        :return: print a bar chart illustrating the frequency distribution in frequency_dict
        """

        # find the longest elements
        max_len = 0
        for e in frequency_dict:
            if len(str(e)) > max_len:
                max_len = len(str(e))

        # store the diagram
        rows = []
        for e, f in frequency_dict.items():
            row = []
            num_of_spaces = max_len - len(str(e))
            for _ in range(0, num_of_spaces, 1):
                row.append(' ')
            row.append(e)
            row.append(': ')
            for _ in range(0, f, 1):
                row.append('$')
            rows.append(row)

        # output the diagram
        for r in rows:
            for e in r:
                print(e, end='')
            print()


