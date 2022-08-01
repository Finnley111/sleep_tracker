# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 14:26:57 2022

@author: finnl
"""
#v1


# Load packages
import matplotlib.pyplot as plt
import pickle
from scipy import signal
import numpy as np
import pandas as pd
import os
from os import path

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import math

from datetime import date

import tkinter as tk
from tkinter import ttk
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

today = date.today()


class User():
    def __init__(self, name, birth_date, sleep_goal):
        self.name = name
        self.birth_date = birth_date
        self.sleep_goal = sleep_goal
        
        self.age = today.strftime("%d/%m/%Y")
        
    def getName(self):
        return self.name
        

user = User(input("enter your name:"), input("enter your date of birth (DD/MM/YYYY):"),input("enter your name:"))