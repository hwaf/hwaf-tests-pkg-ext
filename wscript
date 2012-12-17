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
    ctx.env.ROOT_HOME = ctx.env.ROOTSYS

    rootsys = ctx.env.ROOT_HOME
    for k in 'PyROOT ROOT Reflex Cintex XMLIO XMLParser'.split():
        ctx.env['INCLUDES_%s'%k] = ['%s/include' % rootsys]
        ctx.env['LIBPATH_%s'%k] = ['%s/lib' % rootsys]
    return

def build(ctx):
    msg.info("ROOT-home: %s" % ctx.env.ROOT_HOME)

    pybin = ctx.env['PYTHON']
    if isinstance(pybin, list):
        pybin = pybin[0]
        pass

    pybin = ctx.root.find_resource(pybin)
    pybin.sig = waflib.Utils.h_file(pybin.abspath())
    ctx.install_as('${INSTALL_AREA}/bin/python',
                   pybin,
                   chmod=waflib.Utils.O755)
    #ctx
    return

def install(ctx):
    return
