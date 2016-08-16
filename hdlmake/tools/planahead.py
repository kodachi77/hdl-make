#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2013 - 2015 CERN
# Author: Pawel Szostek (pawel.szostek@cern.ch)
# Multi-tool support by Javier D. Garcia-Lasheras (javier@garcialasheras.com)
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
#

"""Module providing support for Xilinx PlanAhead synthesis"""

from __future__ import absolute_import
from .xilinx import ToolXilinx
from hdlmake.srcfile import (UCFFile, NGCFile, XMPFile, XCOFile)


class ToolPlanAhead(ToolXilinx):

    """Class providing the interface for Xilinx PlanAhead synthesis"""

    TOOL_INFO = {
        'name': 'PlanAhead',
        'id': 'planahead',
        'windows_bin': 'planAhead -mode tcl -source ',
        'linux_bin': 'planAhead -mode tcl -source ',
        'project_ext': 'ppr'}

    STANDARD_LIBS = ['ieee', 'ieee_proposed', 'simprims', 'std',
                     'synopsys', 'unimacro', 'unisim', 'XilinxCoreLib']

    SUPPORTED_FILES = [UCFFile, NGCFile, XMPFile, XCOFile]

    CLEAN_TARGETS = {'clean': ["planAhead_*", "planAhead.*", "run.tcl",
                               ".Xil", "$(PROJECT).cache", "$(PROJECT).data",
                               " $(PROJECT).runs", "$(PROJECT).ppr"]}

    TCL_CONTROLS = {'bitstream': 'launch_runs impl_1 -to_step Bitgen\n'
                                 'wait_on_run impl_1'}

    def __init__(self):
        super(ToolPlanAhead, self).__init__()
        self._tool_info.update(ToolPlanAhead.TOOL_INFO)
        self._supported_files.extend(ToolPlanAhead.SUPPORTED_FILES)
        self._standard_libs.extend(ToolPlanAhead.STANDARD_LIBS)
        self._clean_targets.update(ToolPlanAhead.CLEAN_TARGETS)
        self._tcl_controls.update(ToolPlanAhead.TCL_CONTROLS)
