@echo off
cd /d "%d~dp0"
start cmd /k "python -i -c "from components import easygp; egp = easygp.EasyGridPacker(); egp.setup_window('Test', '200x200'); print('--- EasyGP Ready ---'); egp.root.attributes('-topmost', True); mainframe = egp.add_frame(); ""