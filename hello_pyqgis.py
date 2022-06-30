import sys
import os

print('sys.path:')
for p in sorted(sys.path):
    print(p)

print('\nPATH:')
for p in sorted(os.environ['path'].split(';')):
    print(p)

from qgis.core import Qgis
print(f'QGIS:{Qgis.version()}')

from qgis.core import QgsApplication
from qgis.testing import start_app
from processing.core.Processing import Processing
app = start_app()
Processing.initialize()

print('Algorithms:')
for a in QgsApplication.instance().processingRegistry().algorithms():
    print(a.id())

