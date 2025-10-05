# -*- mode: python ; coding: utf-8 -*-

# Project name: Secure7NetGuard_1.01_Offline
# Author: Nelsomar Barros
# Github: https://github.com/SecureLogic7/Secure7NetGuard
# Contact: nelsom.one8@gmail.com

a = Analysis(
    ['run.py'],  # Changed from 'src/app.py' to 'run.py'
    pathex=['.'],  # Adiciona o diretório atual para que o PyInstaller encontre src/ e o runtime
    binaries=[],
    datas=[
        ('pyarmor_runtime_000000', 'pyarmor_runtime_000000'),  # Adiciona o runtime do PyArmor
    ],
    hiddenimports=[
        'flask', 'requests', 'stripe', 'cryptography', 'sqlalchemy',
        'cryptography.fernet', 'os', 'tkinter'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exec = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Secure7NetGuard_Linux',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

