# -*- mode: python ; coding: utf-8 -*-

# Project name: Secure7NetGuard_1.01_Offline
# Author: Nelsomar Barros
# Github: https://github.com/SecureLogic7/Secure7NetGuard
# Contact: Secure7NetGuard@proton.me

from PyInstaller.utils.hooks import collect_submodules
from PyInstaller.utils.hooks import collect_data_files

block_cipher = None

added_files = []

binaries = []

a = Analysis(['privox_app_v1.py', 'privox_main_v1.py'],
             pathex=['/home/neo/Secure7NetGuard_1.01_Offline'],
             binaries=binaries,
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

# Collect all submodules and data files
submodules = collect_submodules('Secure7NetGuard_1.01_Offline')
data_files = collect_data_files('Secure7NetGuard_1.01_Offline')

a.packages = submodules
a.datas += data_files

a.binaries = binaries

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exef = EXE(pyz,
      a.scripts,
      a.binaries,
      a.zipfiles,
      a.datas,
      [],
      name='secure7netguard',
      debug=False,
      bootloader_ignore_signals=False,
      strip=False,
      upx=True,
      upx_exclude=[],
      runtime_tmpdir=None,
      console=True )

coll = COLLECT(exef,
           a.binaries,
           a.zipfiles,
           a.datas,
           strip=False,
           upx=True,
           upx_exclude=[],
           name='secure7netguard')

app = BUNDLE(coll,
           name='secure7netguard.app',
           icon=None,
           bundle_identifier=None)

# Save the spec file
with open('secure7netguard.spec', 'w') as f:
    f.write("""# -*- mode: python ; coding: utf-8 -*-

# Project name: Secure7NetGuard_1.01_Offline
# Author: Nelsomar Barros
# Github: https://github.com/SecureLogic7/Secure7NetGuard
# Contact: Secure7NetGuard@proton.me

from PyInstaller.utils.hooks import collect_submodules
from PyInstaller.utils.hooks import collect_data_files

block_cipher = None

added_files = []

binaries = []

a = Analysis(['privox_app_v1.py', 'privox_main_v1.py'],
             pathex=['/home/neo/Secure7NetGuard_1.01_Offline'],
             binaries=binaries,
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

# Collect all submodules and data files
submodules = collect_submodules('Secure7NetGuard_1.01_Offline')
data_files = collect_data_files('Secure7NetGuard_1.01_Offline')

a.packages = submodules
a.datas += data_files

a.binaries = binaries

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exef = EXE(pyz,
      a.scripts,
      a.binaries,
      a.zipfiles,
      a.datas,
      [],
      name='secure7netguard',
      debug=False,
      bootloader_ignore_signals=False,
      strip=False,
      upx=True,
      upx_exclude=[],
      runtime_tmpdir=None,
      console=True )

coll = COLLECT(exef,
           a.binaries,
           a.zipfiles,
           a.datas,
           strip=False,
           upx=True,
           upx_exclude=[],
           name='secure7netguard')

app = BUNDLE(coll,
           name='secure7netguard.app',
           icon=None,
           bundle_identifier=None)
""")

# Run PyInstaller with the generated spec file
import subprocess
subprocess.run(['pyinstaller', 'secure7netguard.spec'])