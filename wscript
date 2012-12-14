# -*- python -*-

import waflib.Logs as msg
import waflib.Utils

def pkg_deps(ctx):
    return

def options(ctx):
    ctx.load('find_python')
    ctx.load('find_root')
    return

def configure(ctx):
    ctx.load('find_python')
    ctx.find_python()
    ctx.load('find_root')
    ctx.find_root()
    return

def build(ctx):
    msg.info("ROOT-home: %s" % ctx.env.ROOT_HOME)

    pybin = ctx.env['PYTHON']
    if isinstance(pybin, list):
        pybin = pybin[0]
        pass

    pybin = ctx.root.find_resource(pybin)
    pybin.sig = waflib.Utils.h_file(pybin.abspath())
    ctx.install_as('${INSTALL_AREA}/bin', pybin)
    #ctx
    return

def install(ctx):
    return
