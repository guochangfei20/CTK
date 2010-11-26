
from ctk import *
from ctkqt import QTimer

w = ctkMatrixWidget()
w.show()

if not _ctkPythonShellInstance.isInteractive:
  #QTimer().singleShot(0, app(), SLOT('quit()'))
  t = QTimer()
  t.setInterval(250)
  t.connect('timeout()', app(), 'quit()')
  t.start()
