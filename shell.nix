# shell.nix
let
  # We pin to a specific nixpkgs commit for reproducibility.
  # Last updated: 2024-04-29. Check for new commits at https://status.nixos.org.
  pkgs =
    import
      (fetchTarball "https://github.com/NixOS/nixpkgs/archive/1073dad219cb244572b74da2b20c7fe39cb3fa9e.tar.gz")
      { };
in
pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (
      python-pkgs: with python-pkgs; [
        # select Python packages here
        pandas
        requests
      ]
    ))
  ];
}
