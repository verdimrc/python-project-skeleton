# Use this template for a new project

First, clone this repo:

```bash
git clone https://github.com/verdimrc/python-project-skeleton.git <my-new-package>
```

Then, follow these steps to perform a one-time customization:

1. Change package name & its directory in `setup.py`, `tox.ini`.

2. Remove the `versioneer` stuffs in this template:
   - Modify files:
     * `.gitattributes`: remove line `src/python_project_skeleton/_version.py export-subst`
     * `MANIFEST.in`: remove lines:
        - `include versioneer.py`
        - `include src/python_project_skeleton/_version.py`
     * `setup.cfg`: remove the whole `[versioneer]` section
     * `src/python_project_skeleton/__init__.py`: remove from `# region versioneer`
       until `# endregion`
   - Delete files:
     * `src/python_project_skeleton/_version.py`
     * `versioneer.py`

3. Once the old `versioneer` stuffs are ousted, follow the [installation
   steps for versioneer](https://github.com/warner/python-versioneer/blob/master/INSTALL.md)
   to let `versioneer` manage your package's version string.
   - **NOTE**: if you do not want to use `versioneer` altogether, modify
     `setup.py` and remove these `kwargs` from `setup(...)`:
     * `version=versioneer.get_version()`
     * `cmdclass=versioneer.get_cmdclass()`


## TODO
- make a scaffold template
