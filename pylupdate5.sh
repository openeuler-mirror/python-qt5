#!/bin/sh

@PYTHON3@ -Ic "import PyQt5.pylupdate_main" &> /dev/null
if [ $? -eq 0 ]; then
  exec @PYTHON3@ -Im PyQt5.pylupdate_main ${1+"$@"}
else
  exec @PYTHON2@ -c "import sys; del sys.path[0]; import PyQt5.pylupdate_main; PyQt5.pylupdate_main.main()" ${1+"$@"}

fi
