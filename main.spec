# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['Backend/main.py'],
             pathex=['/Users/daviddidas/Desktop/DLRG_KOMPRESSOR'],
             binaries=[],
             datas=[
                 ('backend/*', 'backend'),  # Include all files in the 'Backend' directory
                 ('frontend/css/*', 'frontend/css'),  # Include all files in the 'Frontend/css' directory
                 ('frontend/html/*', 'frontend/html'),  # Include all files in the 'Frontend/html' directory
                 ('frontend/other/*', 'frontend/other'),  # Include all files in the 'Frontend/other' directory
                 ('identifier.sqlite', '.')  # Include the database file
             ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
