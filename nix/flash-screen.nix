{ gtk3, gobject-introspection, gsound, python3Packages, wrapGAppsHook }:
python3Packages.buildPythonApplication {
  pname = "flash-screen";
  version = "0.2.1.0";
  nativeBuildInputs = [ wrapGAppsHook gobject-introspection ];
  propagatedBuildInputs = [ python3Packages.pygobject3 ]
    ++ [ gtk3 gobject-introspection gsound ];
  src = ../.;
}
