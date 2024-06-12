{
  inputs.nixpkgs.url = github:NixOS/nixpkgs/nixos-23.05;

  inputs.practicebank.url = github:eldridgejm/practicebank/0.1.5;
  inputs.practicebank.inputs.nixpkgs.follows = "nixpkgs";

  outputs = {
    self,
    nixpkgs,
    practicebank,
  }: let
    supportedSystems = ["x86_64-linux" "x86_64-darwin" "aarch64-darwin"];
    forAllSystems = f: nixpkgs.lib.genAttrs supportedSystems (system: f system);
  in {
    devShell = forAllSystems (
      system: let
        pkgs = nixpkgs.legacyPackages.${system};
      in
        pkgs.mkShell {
          buildInputs = [
            # python environment
            (
              pkgs.python3.withPackages (p: [
                practicebank.defaultPackage.${system}
              ])
            )
          ];
        }
    );
  };
}
