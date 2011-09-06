#!/usr/bin/python
#coding:utf-8

'''some doc string'''

__version__ = '0.1.0'

from distutils.core import setup
import sys
import os
import re
import py2exe
includes = ["encodings",
            "encodings.*",
            "csv",
#            "PySide.QtWebKit",
#            "PySide.QtWebKit.*",
#            "PySide.QtNetwork",
#            "PySide.QtNetwork.*",
            ]

#===============================================================================
# Valid values for bundle_files are:
#
# 3 (default)
# don't bundle
# 2
# bundle everything but the Python interpreter
# 1
# bundle everything, including the Python interpreter
# If zipfile is set to None, the files will be bundle
# within the executable instead of library.zip.
#===============================================================================

setupoptions = {"py2exe":
            {   "compressed": 1,
                "optimize": 0,
                "includes": includes,
                "bundle_files": 3,
            }
          }

def Usage():
    '''Show Usage.'''
    print """Usage:
    %s [python script path]""" % sys.argv[0]

def is_in_eclipse():
    '''return true if we are using eclipse,
otherwise, return false
the test method is to looking for 'PYDEV_CONSOLE_ENCODING' 'utf-8'
in os.environ{}
'''
    if os.environ.has_key('PYDEV_CONSOLE_ENCODING'):
        return True

def execute(cmd):
    f = os.popen(cmd)
    content = f.read()

    if is_in_eclipse():
        print(content.decode('gbk').encode(os.environ['PYDEV_CONSOLE_ENCODING']))
    else:
        print content


MANIFEST_TEMPLATE = """
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
  <assemblyIdentity
    version="5.0.0.0"
    processorArchitecture="x86"
    name="%(prog)s"
    type="win32"
  />
  <description>%(prog)s</description>
  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">
    <security>
      <requestedPrivileges>
        <requestedExecutionLevel
            level="asInvoker"
            uiAccess="false">
        </requestedExecutionLevel>
      </requestedPrivileges>
    </security>
  </trustInfo>
  <dependency>
    <dependentAssembly>
      <assemblyIdentity
            type="win32"
            name="Microsoft.VC90.CRT"
            version="9.0.21022.8"
            processorArchitecture="x86"
            publicKeyToken="1fc8b3b9a1e18e3b">
      </assemblyIdentity>
    </dependentAssembly>
  </dependency>
  <dependency>
    <dependentAssembly>
        <assemblyIdentity
            type="win32"
            name="Microsoft.Windows.Common-Controls"
            version="6.0.0.0"
            processorArchitecture="X86"
            publicKeyToken="6595b64144ccf1df"
            language="*"
        />
    </dependentAssembly>
  </dependency>
</assembly>
"""

RT_MANIFEST = 24

def pack_file(filename, icon_path):
    py_scriptName = filename
    while len(sys.argv) > 1:
        del sys.argv[1]

    sys.argv.append("py2exe")

    if(not os.path.exists(py_scriptName)):
        raise Exception("Bad script name, {0} doesn't exists.".format(filename))
    version_str = "0.1"
    data_files = [(".", [
                            'app.ini',
                            'main.exe.manifest',
                            ]),
                         ("Microsoft.VC90.CRT", [
                             'Microsoft.VC90.CRT.manifest',
                             'msvcm90.dll',
                             'msvcp90.dll',
                             'msvcr90.dll',
                         ],
                   ),
                 ]

    if re.search(r'\.py$', filename, re.IGNORECASE):
        setup(
            version = version_str,
            description = "prog desc",
            name = 'prog',
            options = setupoptions,
            zipfile = None,
            console = [
                {
                    "script": py_scriptName,
                    "company_name" :"Morya#is-coder.com",
                    "copyright" : "No Copyright Reserved",
                    "icon_resources": [(1, icon_path)],
                    "other_resources" : [(
                        RT_MANIFEST, 1,
                        MANIFEST_TEMPLATE % dict(prog="prog"))
                    ],
                }
            ],
            data_files = data_files,
        )
    else:
        setup(
            version = version_str,
            description = "prog",
            name = 'prog',
            options = setupoptions,
            zipfile = None,
            windows = [
                {
                    "script": py_scriptName,
                    "company_name" :"Morya#is-coder.com",
                    "copyright" : "No Copyright Reserved",
                    "icon_resources": [(1, icon_path)],
                    "other_resources" : [(
                        RT_MANIFEST, 1,
                        MANIFEST_TEMPLATE % dict(prog="prog"))
                    ],
                }
            ],
            data_files = data_files,
        )

if __name__ == '__main__':
    if os.path.exists("dist"):
        pass

    pyScripts = [
        ('main.pyw', "images/git.ico" ),
    ]
    
    if len(sys.argv) > 1:
        pack_file( sys.argv[1], None)
    else:
        for py_scriptName, icon_path in pyScripts:
            pack_file( py_scriptName, icon_path )

    if 0:
        import glob
        exes = glob.glob("dist" + os.sep + "*.exe")
        for exe in exes:
            if exe.upper() != "w9xpopen.exe".upper():
                os.system('upx ' + exe)

    print "Done"