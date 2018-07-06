## chase

Chase is the sad, underpaid legal intern that looks up your citations within state laws.

Send him your requests and he'll do all the work for you.


## Getting Started

Chase needs docker, and also uses json files from [statedb](github.com/davidawad/statedb)

```
# Makefile will build the container for you
$ make
# run the container
$ make run
# make requests against chase for keywords of whatever you want
$ time curl -X GET  -H "Content-Type: application/json" -d '{"keyword":"hac"}' '0.0.0.0:8000/search'
[["Section 24:21-5","24:21-5 Schedule I.\n\n5.Schedule I.\n\na.Tests. The director shall place a substance in Schedule I if he finds that the substance: (1) has high potential for abuse; and (2) has no accepted medical use in treatment in the United States; or lacks accepted safety for use in treatment under medical supervision.\n\nb.The controlled dangerous substances listed in this section are included in Schedule I, subject to any revision and republishing by the director pursuant to subsection d. of section 3 of P.L.1970, c.226 (C.24:21-3), and except to the extent provided in any other schedule.\n\nc.Any of the following opiates, including their isomers, esters, and ethers, unless specifically excepted, whenever the existence of such isomers, esters, ethers and salts is possible within the specific chemical designation:\n\n(1)Acetylmethadol\n\n(2)Allylprodine\n\n(3)Alphacetylmethadol\n\n(4)Alphameprodine\n\n(5)Alphamethadol\n\n(6)Benzethidine\n\n(7)Betacetylmethadol\n\n(8)Betameprodine\n\n(9)Betamethadol\n\n(10) Betaprodine\n\n(11) Clonitazene\n\n(12) Dextromoramide\n\n(13) Dextrorphan\n\n(14) Diampromide\n\n(15) Diethylthiambutene\n\n(16) Dimenoxadol\n\n(17) Dimepheptanol\n\n(18) Dimethylthiambutene\n\n(19) Dioxaphetyl butyrate\n\n(20) Dipipanone\n\n(21) Ethylmethylthiambutene\n\n(22) Etonitazene\n\n(23) Etoxeridine\n\n(24) Furethidine\n\n(25) Hydroxypethidine\n\n(26) Ketobemidone\n\n(27) Levomoramide\n\n(28) Levophenacylmorphan\n\n(29) Morpheridine\n\n(30) Noracymethadol\n\n(31) Norlevorphanol\n\n(32) Normethadone\n\n(33) Norpipanone\n\n(34) Phenadoxone\n\n(35) Phenampromide\n\n(36) Phenomorphan\n\n(37) Phenoperidine\n\n(38) Piritramide\n\n(39) Proheptazine\n\n(40) Properidine\n\n(41) Racemoramide\n\n(42) Trimeperidine.\n\nd.Any of the following narcotic substances, their salts, isomers and salts of isomers, unless specifically excepted, whenever the existence of such salts, isomers and salts of isomers is possible within the specific chemical designation:\n\n(1)Acetorphine\n\n(2)Acetylcodone\n\n(3)Acetyldihydrocodeine\n\n(4)Benzylmorphine\n\n(5)Codeine methylbromide\n\n(6)Codeine-N-Oxide\n\n(7)Cyprenorphine\n\n(8)Desomorphine\n\n(9)Dihydromorphine\n\n(10) Etorphine\n\n(11) Heroin\n\n(12) Hydromorphinol\n\n(13) Methyldesorphine\n\n(14) Methylhydromorphine\n\n(15) Morphine methylbromide\n\n(16) Morphine methylsulfonate\n\n(17) Morphine-N-Oxide\n\n(18) Myrophine\n\n(19) Nicocodeine\n\n(20) Nicomorphine\n\n(21) Normorphine\n\n(22) Phoclodine\n\n(23) Thebacon.\n\ne.Any material, compound, mixture or preparation which contains any quantity of the following hallucinogenic substances, their salts, isomers and salts of isomers, unless specifically excepted, whenever the existence of such salts, isomers, and salts of isomers is possible within the specific chemical designation:\n\n(1)3,4-methylenedioxy amphetamine\n\n(2)5-methoxy-3,4-methylenedioxy amphetamine\n\n(3)3,4,5-trimethoxy amphetamine\n\n(4)Bufotenine\n\n(5)Diethyltryptamine\n\n(6)Dimethyltryptamine\n\n(7)4-methyl-2,5-dimethoxylamphetamine\n\n(8)Ibogaine\n\n(9)Lysergic acid diethylamide\n\n(10) Marihuana\n\n(11) Mescaline\n\n(12) Peyote\n\n(13) N-ethyl-3-piperidyl benzilate\n\n(14) N-methyl-3-piperidyl benzilate\n\n(15) Psilocybin\n\n(16) Psilocyn\n\n(17) Tetrahydrocannabinols.\n\nL.1970, c.226, s.5; amended 2007, c.244, s.3."],["Section 40:67-3","40:67-3. Hack or cab stands at hotels\nThe owner or lessee of any public hotel maintaining fifty or more rooms for the accommodation of travelers may, with the permission of the body having control of the streets, designate a space in the street in front of the hotel as a hack or cab stand, and the hacks or cabs which shall be permitted to occupy the same."]]
        0.12 real         0.00 user         0.00 sys

```

## Implementation Details

Chase is implemented in python flask.

He quickly parses through json files and finds relevant information for you.



## Some Notes on setting up in kubernetes

```
# Start minikube
minikube start

# Set docker env
eval $(minikube docker-env)

# Build image
docker build -t foo:0.0.1 .

# Run in minikube
kubectl run hello-foo --image=foo:0.0.1 --image-pull-policy=Never

# Check that it's running
kubectl get pods

```
