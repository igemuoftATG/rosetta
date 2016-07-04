Rosetta & PyRosetta Resources

-   **See “how to prepare structures for use in rosetta” AND “how to
    prepare ligands for use in rosetta” + overview of params files**

    -   Put in POSE (in FAQ)

1.  **Prepare** structures by “relaxing into Rosetta’s energy function”?

    -   **See Relax Application**

2.  For protein-ligand docking (*note that Rosetta does NOT recognize
    ligands by default)*:

    -   Generate a params file for gold w/ info on name of metal, id
        code, type ligand, unk amino acid type, charge, bond, other
        metal-binding atoms, etc.

        -   See:
            /path/to/rosetta/main/database/chemical/residue\_type\_sets

            -   Can generate from input mol file

    -   Are we modelling ligand flexibility? If so, need library of
        ligand conformers in PDB format (MOE, openeye Omega… RCSB(?))

        -   PDB will likely need cleaning

Ligand: gold ions (gold (III)), then gold(I), then copper (I and II) (so
we can assess binding, distance, energy for competition with gold) then
IF POSSIBLE, after everything else, lanthanum

-   **I want to do “X” page**

    -   **Docking**

    -   **Symmetric Interfaces**

-   Symmetry User’s Guide

-   SymDock for predicting symmetric homooligomeric protein assemblies
    from single subunit’s structure

    -   Start with single monomeric structure & use make\_symmdef\_file

        -   Use make\_symmdef\_file\_denovo if we don’t know rigid body
            config

            -   Will perturb/refine starting configuration?

            -   If required symmetry isn’t encoded in this file, either
                do by hand or analyze other protein with same symmetry
                in PDB database, generate symm\_def, and edit to
                randomize initial orientation

    -   Keep seeing “prepacked protein monomer”: **what is
        pre-packing?**

    -   docking:dock\_ppk produces a homomeric output PDB

***If possible, (last thing on list) can we monitor the homodimer
linking to the DNA(?)***

-   Tam can help with DoF

-   Fold and Dock for predicting symmetric homooligomeric protein
    assemblies starting with the **FASTA sequence (+ location of
    fragment libraries + de novo symmdef file)** of a subunit:

    <https://www.rosettacommons.org/docs/latest/application_documentation/structure_prediction/fold-and-dock>

    \*Ab initio options all valid

-   PyRosetta docking tutorial:
    <http://www.pyrosetta.org/tutorials#TOC-Workshop-7:-Docking>

    -   If you are using ligands in PyRosetta, please consult the sample
        script D120\_Ligand\_interface.py and the tool scripts
        mutants.py, molfile2params.py, and load\_ligand.py
        (residue params)

    -   <http://www.pyrosetta.org/obtaining-and-preparing-ligand-pdb-files>

        -   Obtain PDB (RCSB, etc)

        -   Get chemical data files & convert to .mdl via openbabel

        -   Convert .mdl to params file

        -   Obtain ligand PDB (if not present; set ResidueType
            appropriately & rename chain “X”)

            -   May need to insert PDB manually with Python, PyMOL,
                grep, awk, or Biopython, etc.

        -   Load ligand PDB into PyRosetta

        -   Alter fullatom chemical database permanently

        -   Prep for docking

    -   Make sure both chains (for docking) are part of same Pose

        -   Create PDB including both partners

        -   Download & clean

<https://www.rosettacommons.org/docs/latest/application_documentation/design/beta-strand-homodimer-design>

This is for creating a homodimer that will form via a surface
beta-strand; useful to look at changes made at very least

-   Sample degrees of freedom & interpret results

    <https://www.rosettacommons.org/docs/latest/getting_started/Analyzing-Results>

PDB file doesn’t exist in database, but we generated a predicted one
from one **I-TASSER**

-   Can access I-TASSER structures from Tam’s and other’s accounts on
    website with ID & password

**Can we run homooligomeric symmetry in parallel with generating
structure in PyRosetta based on structure?**
