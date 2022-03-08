# python + paramiko

## comandos

```ps
# iniciar ambiente virtual
python -m venv venv

# instalar PyQt5
pip3 install PyQt5 PyQt5-tools

# converter .UI par .PY
python -m PyQt5.uic.pyuic -x interface.ui -o interface.py
python -m PyQt5.uic.pyuic -x .\interfaces\interface.ui -o .\interface.py

# converter par exe
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed  .\main.py

# git push
git add --all
git commit -m ":fire:"
git push

```
