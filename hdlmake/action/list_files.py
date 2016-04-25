#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2013 CERN
# Author: Pawel Szostek (pawel.szostek@cern.ch)
#
# This file is part of Hdlmake.
#
# Hdlmake is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hdlmake is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Hdlmake.  If not, see <http://www.gnu.org/licenses/>.

from action import Action
import new_dep_solver as dep_solver

class ListFiles(Action):
    def run(self):
        file_set = self.modules_pool.build_limited_file_set()
        file_list = dep_solver.make_dependency_sorted_list(file_set)
        files_str = [f.path for f in file_list]
        print(self.options.delimiter.join(files_str))

# class ListFiles(Action):
#     def run(self):
#         files_str = []
#         for m in self.modules_pool:
#             if not m.isfetched:
#                 continue
#             files_str.append(self.options.delimiter.join([f.path for f in m.files]))
#         print(" ".join(files_str))
