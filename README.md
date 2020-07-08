# Use this template for a new project

Get this template:

```bash
git clone https://github.com/verdimrc/python-project-skeleton.git <my-new-package>
```

then adapt to your new package name:

1. Change package name & its directory in `setup.py`, `tox.ini`.

2. Readjust `versioneer`:

   1. Modify files:
      - `.gitattributes`: remove line `src/python_project_skeleton/_version.py export-subst`
      - `MANIFEST.in`: remove lines:
        ```
        include versioneer.py`
        include src/python_project_skeleton/_version.py`
        ```
      - `setup.cfg`: remove the whole `[versioneer]` section
      - `src/python_project_skeleton/__init__.py`: remove from `# region versioneer`
        until `# endregion`

   2. Delete files:
      - `src/python_project_skeleton/_version.py`
      - `versioneer.py`

   3. Once the old `versioneer` stuffs are ousted, follow these
      [steps](https://github.com/warner/python-versioneer/blob/master/INSTALL.md)
      to let `versioneer` manage your package's version string.

   4. **NOTE**: if you do not want to use `versioneer` altogether, modify
      `setup.py` and remove these `kwargs` from `setup(...)`:
      - `version=versioneer.get_version()`
      - `cmdclass=versioneer.get_cmdclass()`


## TODO
- make a scaffold template
