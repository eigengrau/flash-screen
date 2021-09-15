{ pkgs }:
pkgs.python38Packages.buildPythonApplication {
  pname = "flash-screen";
  version = "0.2.1.0";
  nativeBuildInputs = [ pkgs.wrapGAppsHook ];
  propagatedBuildInputs = [ pkgs.python38Packages.pygobject3 ]
    ++ (with pkgs; [ gtk3 gobject-introspection gsound ]);
  src = ../.;
}
