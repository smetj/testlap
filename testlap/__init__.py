#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  __init__.py
#  
#  Copyright 2012 Jelle Smet <development@smetj.net>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
# 

import timeit
import sys
import platform
from prettytable import PrettyTable

class TestLap():
    '''
    A Python framework to measure and compare the execution speed of different methods in a class.
    
    Class which executes and measures all methods of instance starting with test_
    Returns a table containing the results sorted on executionspeed.
    
    Accepts following parameters:
    
        - instance:     The class containing all test_* methods which needs to be executed.
        - iterations:   How many times echo test_ methods needs to be executed.
        
    '''
        
    def __init__(self, instance, iterations=1):
        self.instance=instance
        self.iterations=iterations
        self.table = PrettyTable()
        self.table.add_column('Function',[], align='l')
        self.table.add_column('Description',[], align='l')
        self.table.add_column('Result',[], align='l')
        self.table.add_column('Seconds',[], align='r')

    def go(self):
        '''
        Starts testing.
        '''
        
        for function in dir(self.instance):
            if function.startswith('test_'):
                sys.stdout.write("Running %s "%(function))
                try:
                    test_instance = timeit.Timer(getattr(self.instance,function))
                    secs = test_instance.timeit(number=self.iterations)
                except Exception as err:
                    sys.stdout.write("Failed: %s"%err)
                    status="Failed"
                    secs=0
                else:
                    status="OK"
                    sys.stdout.write (status)

                self.table.add_row([function, getattr(self.instance,function).__doc__, status, float("%.10f"%secs)])
        self.__header(self.instance.__doc__)
        sys.stdout.write (self.table.get_string(sortby="Seconds"))

    def __header(self, title):
        sys.stdout.write(sys.version)
        sys.stdout.write(platform.platform())
        sys.stdout.write(title)
