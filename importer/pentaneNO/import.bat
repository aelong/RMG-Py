:: run cantherm and analysis
ECHO aloha gents
call activate rmg_env
call python /Code/RMG-Py/importChemkin.py --species chem.inp --reactions chem.inp --thermo therm.dat --known SMILES.txt --port 8084 --noqm -v
::call gprof2dot -f pstats  importChemkin.profile | dot -Tpdf -o importChemkin.profile.pdf
PAUSE