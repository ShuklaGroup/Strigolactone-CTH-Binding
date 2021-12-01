round()
{
echo $(printf %.$2f $(echo "scale=$2;(((10^$2)*$1)+0.5)/(10^$2)" | bc))
};

cmplx=protein_helix_nohydrogen #name of the protein
mkdir Initial_Amber_Files_${cmplx}
echo Initial_Amber_Files_${cmplx}
cd Initial_Amber_Files_${cmplx}

pdbAdrs='/home/sobecks2/6BRT' #put address of your project's folder
cp ${pdbAdrs}/pdb_list.txt .

c=0.15 # Desired Concentration
while read line
do
	mkdir ${line}
        cd ${line}
        cp ${pdbAdrs}/${line}.pdb .
        #cp ${pdbAdrs}/GR2.frcmod .
        #cp ${pdbAdrs}/GR2.lib .

        echo "source /home/mc26/amber18/dat/leap/cmd/leaprc.protein.ff14SB" > tleap_${line}.in 
       #change path from jiming to MC26 and do this below either
        echo "source leaprc.gaff">> tleap_${line}.in
        echo "source leaprc.water.tip3p">> tleap_${line}.in
        echo "loadoff atomic_ions.lib">> tleap_${line}.in
	echo "loadamberparams frcmod.ionsjc_tip3p">> tleap_${line}.in
        echo "complex=loadpdb ${line}.pdb">> tleap_${line}.in
        echo "solvatebox complex TIP3PBOX 11 1.0">> tleap_${line}.in
        echo "quit">> tleap_${line}.in

	tleap -f  tleap_${line}.in
    pwd
    m=$(grep "residues" leap.log | cut -c 9-13)
    echo $m
    n=$(echo 0.018*${m}*${c} |bc)
        echo "NUMBER!!!!"
        echo $n 
        N=$(round $n 0)
        M=$((${N} + 13)) #may need to change this number based on how things run
        echo $M
#run with water ions, have to find proper number of sodium and chloride ions to make the proper concentration and have a neutral charge
#first build a "bad" box, then use a parameter file to get proepr number of ions
	
cat > tleap_${line}.in << EOF
source /home/mc26/amber18/dat/leap/cmd/leaprc.protein.ff14SB 
source leaprc.gaff
source leaprc.water.tip3p
loadoff atomic_ions.lib
loadamberparams frcmod.ionsjc_tip3p
complex=loadpdb ${line}.pdb
solvatebox complex TIP3PBOX 11 1.0
addions complex Na+ ${M}
addions complex Cl- ${N}
saveamberparm complex ${line}.prmtop ${line}.inpcrd
savepdb complex ${line}_SetUp.pdb
quit
EOF
	tleap -f  tleap_${line}.in
	cd ..
done < pdb_list.txt
