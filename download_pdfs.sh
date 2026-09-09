#!/usr/bin/env bash
set -x
urls=(
"https://www.sciencedirect.com/science/article/pii/S2405457726022047/pdf?md5=d76f90cd8331aba7569ad81062c5faf1&pid=1-s2.0-S2405457726022047-main.pdf"
"https://jn.nutrition.org/article/S0022-3166(23)00536-9/pdf"
"https://push-zb.helmholtz-munich.de/deliver.php?id=13071"
"https://journals.plos.org/plosone/article/file?type=printable&id=10.1371/journal.pone.0154400"
"https://research.unipd.it/retrieve/be859f48-54a2-427b-aee5-ea802eaf00e6/nutrients-13-04422-v3.pdf"
"https://ijogr.org/archive/volume/11/issue/3/article/13696/pdf"
"https://www.ajog.org/article/S0002-9378(19)30418-1/pdf"
"https://www.karger.com/Article/Pdf/457359"
"https://pure.ulster.ac.uk/ws/portalfiles/portal/102538408/s12916_021_01914_9.pdf"
"https://core.ac.uk/download/pdf/147608267.pdf"
"https://research-information.bris.ac.uk/ws/portalfiles/portal/185826531/10.1186_s13148_019_0618_0.pdf"
"https://pure.ulster.ac.uk/ws/files/76971407/CLEP_D_18_00378_R1_Submitted_revision1_002_.pdf"
"https://ajcn.nutrition.org/article/S0002-9165(23)07159-9/pdf"
"https://www.medsci.org/v1/i1/czeizel.pdf"
"https://academic.oup.com/ajcn/article-pdf/98/1/92/23829047/92.pdf"
"https://www.ajog.org/article/S0002-9378(05)00365-0/pdf"
"https://www.ahajournals.org/doi/pdf/10.1161/JAHA.119.015652"
"https://www.frontiersin.org/journals/nutrition/articles/10.3389/fnut.2021.670289/pdf"
"https://www.contraceptionjournal.org/article/S0010-7824(07)00247-8/pdf"
"https://bmjopen.bmj.com/content/bmjopen/10/11/e040416.full.pdf"
"https://www.jmest.org/wp-content/uploads/JMESTN42351986.pdf"
"https://jn.nutrition.org/article/S0022-3166(22)08885-X/pdf"
"https://www.ldeo.columbia.edu/~avangeen/publications/documents/Peters_EHP_15.pdf"
"https://ora.uniurb.it/retrieve/handle/11576/2670760/105321/Nutrients_2019.pdf"
"https://bmjopen.bmj.com/content/bmjopen/9/1/e026756.full.pdf"
"https://minerva-access.unimelb.edu.au/bitstreams/b65c8047-c4cd-4945-97a9-f0c5157f3ac2/download"
"https://apcz.umk.pl/QS/article/download/74072/47296/252948"
"https://mdpi-res.com/bookfiles/book/5131/Creatine_Supplementation_for_Health_and_Clinical_Diseases.pdf?v=1787187928"
"https://digitalcommons.lindenwood.edu/context/faculty-research-papers/article/1712/viewcontent/Part_II._Common_questions_and_misconceptions_about_creatine_supplementation__what_does_the_scientific_evidence_really_show_.pdf"
"https://www.frontiersin.org/journals/nutrition/articles/10.3389/fnut.2025.1682746/pdf"
"https://www.tandfonline.com/doi/pdf/10.1186/s12970-017-0173-z"
"https://pdfs.semanticscholar.org/4493/07d42ec7561a0cfff26862339c86dc5aa1b9.pdf"
"https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2019.00015/pdf"
)
for url in "${urls[@]}"; do
  fname=$(echo "$url" | tr '/?&=' '____' | tr -cd 'a-zA-Z0-9._-')
  curl -sL -o "pdfs/${fname: -80}.pdf" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/pdf,*/*" --max-time 30 "$url" &
done
wait
echo "DONE DOWNLOADING"
ls -la pdfs/ | head -50
