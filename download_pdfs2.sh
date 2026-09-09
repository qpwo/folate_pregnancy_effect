#!/usr/bin/env zsh
set -x
pairs=(
"sciencedirect_S2405457726022047|https://www.sciencedirect.com/science/article/pii/S2405457726022047/pdf?md5=d76f90cd8331aba7569ad81062c5faf1&pid=1-s2.0-S2405457726022047-main.pdf"
"jn_nutrition_S0022-3166_23_00536-9|https://jn.nutrition.org/article/S0022-3166(23)00536-9/pdf"
"helmholtz_13071|https://push-zb.helmholtz-munich.de/deliver.php?id=13071"
"ijogr_13696|https://ijogr.org/archive/volume/11/issue/3/article/13696/pdf"
"ajog_EAGeR|https://www.ajog.org/article/S0002-9378(19)30418-1/pdf"
"karger_457359|https://www.karger.com/Article/Pdf/457359"
"ulster_FASSTT_followup|https://pure.ulster.ac.uk/ws/portalfiles/portal/102538408/s12916_021_01914_9.pdf"
"core_FASSTT|https://core.ac.uk/download/pdf/147608267.pdf"
"ajcn_folic_pregnancy|https://ajcn.nutrition.org/article/S0002-9165(23)07159-9/pdf"
"medsci_czeizel|https://www.medsci.org/v1/i1/czeizel.pdf"
"ajcn_FASSTT_findings|https://academic.oup.com/ajcn/article-pdf/98/1/92/23829047/92.pdf"
"ajog_twinning|https://www.ajog.org/article/S0002-9378(05)00365-0/pdf"
"ahajournals_JAHA|https://www.ahajournals.org/doi/pdf/10.1161/JAHA.119.015652"
"contraception_folate|https://www.contraceptionjournal.org/article/S0010-7824(07)00247-8/pdf"
"bmjopen_e040416|https://bmjopen.bmj.com/content/bmjopen/10/11/e040416.full.pdf"
"jmest_42351986|https://www.jmest.org/wp-content/uploads/JMESTN42351986.pdf"
"jn_creatine_folate|https://jn.nutrition.org/article/S0022-3166(22)08885-X/pdf"
"columbia_Peters_EHP|https://www.ldeo.columbia.edu/~avangeen/publications/documents/Peters_EHP_15.pdf"
"ora_uniurb_creatine|https://ora.uniurb.it/retrieve/handle/11576/2670760/105321/Nutrients_2019.pdf"
"bmjopen_CPO|https://bmjopen.bmj.com/content/bmjopen/9/1/e026756.full.pdf"
"apcz_umk_creatine|https://apcz.umk.pl/QS/article/download/74072/47296/252948"
"tandfonline_creatine|https://www.tandfonline.com/doi/pdf/10.1186/s12970-017-0173-z"
"semanticscholar_creatine|https://pdfs.semanticscholar.org/4493/07d42ec7561a0cfff26862339c86dc5aa1b9.pdf"
)
for pair in "${pairs[@]}"; do
  name="${pair%%|*}"
  url="${pair#*|}"
  curl -sL -o "pdfs/${name}.pdf" \
    -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" \
    -H "Accept: application/pdf,*/*" \
    --max-time 45 "$url" &
done
wait
echo "DONE"
for f in pdfs/*.pdf; do echo "$(wc -c < "$f") $f"; done | sort -rn | head -50
