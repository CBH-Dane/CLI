# How to start
1. Run `pip install -e .`
   1. Pip reads pyproject.toml and sees the project + build system (hatchling)
   2. Hatchling bundles the build for the venv, seeing the package `aa.py` and reads that it's a package named aa & bundles for the build.
   3. Pip reads the bundle and builds out aa.py into the venv, essentially as its own pip package (the `-e` makes a .pth file that points back to source)
   4. Pip reads [project.scripts], sees ``aa = aa:main` and writes a tiny venv script into `.ven/bin/aa` that, when executed, imports aa module and calls main().
2. Run `aa ping` or `aa hello`, from anywhere (part of your pip packages now!)
3. You can see the distribution & build from `C:\Users\<user.name>\AppData\Local\Programs\Python\Python314\Lib\site-packages\aa-0.1.0.dist-info`