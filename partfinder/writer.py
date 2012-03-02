#Copyright (C) 2011 Robert Lanfear and Brett Calcott
#
#This program is free software: you can redistribute it and/or modify it
#under the terms of the GNU General Public License as published by the
#Free Software Foundation, either version 3 of the License, or (at your
#option) any later version.
#
#This program is distributed in the hope that it will be useful, but
#WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#General Public License for more details. You should have received a copy
#of the GNU General Public License along with this program.  If not, see
#<http://www.gnu.org/licenses/>. PartitionFinder also includes the PhyML
#program and the PyParsing library both of which are protected by their
#own licenses and conditions, using PartitionFinder implies that you
#agree with those licences and conditions as well.

import logging
log = logging.getLogger("writer")

class Writer(object):
    def __init__(self):
        pass

    def final(self):
        pass
        # write out the final stuff
        #

class ReportWriter(Writer):
    # ONE Day.... 
    pass

class BinaryWriter(Writer):

    def final(self, analysis):

        write pickle out


# Things to do
#
# QUESTION: Why is it not conssintent
#
# 0. Separet core from analysis_method.py
# 1. make a summary object in analysis. Summary(object)
# 2. xform to binary here
# 3. make a comparator for it
