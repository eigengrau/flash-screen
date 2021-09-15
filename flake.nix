{
  description = "flash-screen";
  inputs = {
    nixpkgs.url = "nixpkgs/nixos-21.05";
    utils.url = "github:numtide/flake-utils";
  };
  outputs = { self, nixpkgs, utils }:
    (utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
          overlays = [
            (final: prev: {
              flash-screen = final.callPackage ./nix/flash-screen.nix { };
            })
          ];
        };
      in rec {
        packages = { flash-screen = pkgs.flash-screen; };
        defaultPackage = packages.flash-screen;
        defaultApp = {
          type = "app";
          program = "${packages.flash-screen}/bin/flash-screen";
        };
      }));
}
