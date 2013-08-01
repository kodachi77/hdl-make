#!/usr/bin/env python

import os
import logging
from tempfile import TemporaryFile
from util import path
from subprocess import Popen, PIPE


class Svn(object):
    def __init__(self):
        pass

    def fetch(self, module):
        if not os.path.exists(module.fetchto):
            os.mkdir(module.fetchto)

        cur_dir = os.getcwd()
        os.chdir(module.fetchto)

        basename = path.url_basename(module.url)
        mod_path = os.path.join(module.fetchto, basename)

        cmd = "svn checkout {0} " + module.basename
        if module.revision:
            cmd = cmd.format(module.url + '@' + module.revision)
        else:
            cmd = cmd.format(module.url)

        success = True

        logging.info("Checking out module %s" % mod_path)
        logging.debug(cmd)
        if os.system(cmd) != 0:
            success = False
        os.chdir(cur_dir)

        module.isfetched = True
        module.path = os.path.join(module.fetchto, module.basename)
        return success

    @staticmethod
    def check_revision_number(path):
        cur_dir = os.getcwd()
        revision = None
        stderr = TemporaryFile()

        try:
            os.chdir(path)
            svn_cmd = "svn info 2>/dev/null | awk '{if(NR == 5) {print $2}}'"
            svn_out = Popen(svn_cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=stderr, close_fds=True)
            errmsg = stderr.readlines()
            if errmsg:
                logging.debug("svn error message (in %s): %s" % (path, '\n'.join(errmsg)))

            try:
                revision = svn_out.stdout.readlines()[0].strip()
            except IndexError:
                pass
        finally:
            os.chdir(cur_dir)
            stderr.close()
        return revision