British Journal of Nutrition (2020), 123, 220–231
© The Authors 2019
doi:10.1017/S0007114519002617

# Computer-based tailored dietary counselling improves the nutrient adequacy of the diet of French pregnant women: a randomised controlled trial

Clélia M. Bianchi¹, François Mariotti¹*, Anne Lluch², Claire Journet¹, Yaëlle Stehr³, Hélène Beaussier⁴, Julien Fournier⁴, Stéphane Dervaux⁵, Dylan Cohen-Tanuggi⁵, Elodie Reulet¹, Eric O. Verger⁶, Elie Azria³,⁷ and Jean-François Huneau¹

¹UMR PNCA, AgroParisTech, INRA, Université Paris-Saclay, 75005 Paris, France
²Global Nutrition Department, Danone Nutricia Research, Centre Daniel Carasso, RD 128, 91737 Palaiseau Cedex, France
³Notre Dame de Bon Secours Maternity Unit, Groupe Hospitalier Paris Saint-Joseph, 75014 Paris, France
⁴Clinical Research Center, Groupe Hospitalier Paris Saint-Joseph, 75014 Paris, France
⁵UMR MIA-Paris, AgroParisTech, INRA, Université Paris-Saclay, 75005 Paris, France
⁶NUTRIPASS, IRD, Université de Montpellier, SupAgro, 34000 Montpellier, France
⁷UMR1153 – Obstetrical, Perinatal and Pediatric Epidemiology (EPOPé Research Team), DHU Risks in Pregnancy, Paris Descartes University – INSERM, 75014 Paris, France

(Submitted 6 March 2019 – Final revision received 8 October 2019 – Accepted 10 October 2019 – First published online 18 December 2019)

**Abstract**
During pregnancy, mothers-to-be should adapt their diet to meet increases in nutrient requirements. Pregnant women appear to be keener to adopt healthier diets, but are not always successful. The objective of the present study was to determine whether a guided, stepwise and tailored dietary counselling programme, designed using an optimisation algorithm, could improve the nutrient adequacy of the diet of pregnant women, beyond generic guidelines. Pregnant women (n 80) who attended Notre-Dame-de-Bon-Secours Maternity Clinic were randomly allocated to the control or intervention arm. Dietary data were obtained twice from an online 3-d dietary record. The nutrient adequacy of the diet was calculated using the PANDiet score, a 100-point diet quality index adapted to the specific nutrient requirements for pregnancy. Women were supplied with generic dietary guidelines in a reference booklet. In the intervention arm, they also received nine sets of tailored dietary advice identified by an optimisation algorithm as best improving their PANDiet score. Pregnant women (n 78) completed the 12-week dietary follow-up. Initial PANDiet scores were similar in the control and intervention arms (60·4 (sd 7·3) v. 60·3 (sd 7·3), P = 0·92). The PANDiet score increased in the intervention arm (+3·6 (sd 9·3), P = 0·02) but not in the control arm (−0·3 (sd 7·3), P = 0·77), and these changes differed between arms (P = 0·04). In the intervention arm, there were improvements in the probabilities of adequacy for α-linolenic acid, thiamin, folate and cholesterol intakes (P < 0·05). Tailored dietary counselling using a computer-based algorithm is more effective than generic dietary counselling alone in improving the nutrient adequacy of the diet of French women in mid-pregnancy.

**Key words: Tailored dietary advice: Dietary counselling: Pregnancy: Nutrient adequacy: Behaviour change techniques**

In recent decades, more evidence has become available in favour of the developmental origin of health and disease paradigm(1–3). Indeed, good maternal nutrition, defined by meeting the additional requirements of pregnancy without excessive intakes of unfavourable nutrients, is critical to both the mother’s health and well-being and also to that of her child in utero and later in childhood and even adult life(4,5). In developed countries, inadequate intakes of both macro- and micronutrients have been observed during pregnancy(6,7), with high intakes of fat, saturated fats(6) and sugars(8), low intakes of fibre and polyunsaturated fats(6), the n-6:n-3 ratio of which is inadequate(9,10). Intakes of vitamin and minerals identified as critical during pregnancy are also of concern, with inadequate intakes reported for vitamin D, folate, Fe(7) and iodine(11,12). In France, the few studies that have assessed the nutrient intakes of pregnant women have revealed the same trends, with inadequate intakes of fat, saturated fats(13), dietary fibre, vitamin D(14), folate(14,15), Fe(15) and iodine(15,16) and an inadequate polyunsaturated fat profile(10,13).

As demonstrated by many qualitative studies, pregnancy is accompanied by a rise in nutrition awareness(17) associated with more nutrition-related information-seeking practices(18) and

**Abbreviations:** ALA, α-linolenic acid; EIEA, energy intake excluding alcohol.
* Corresponding author: Professsor François Mariotti, email: francois.mariotti@agroparistech.fr

Tailored dietary counselling in pregnancy

221

Fig. 1. Timeline of 12-week dietetic follow-up for one participant. The pictogram showing a woman corresponds to a face-to-face dietetic appointment, whereas the pictogram showing a telephone corresponds to a dietetic appointment over the telephone. The pictogram showing a book indicates the time point when the booklet was given to all participants. Specificities for the intervention arm are presented in bold, italic and underlined characters. W, week.

```jsonl
{"event": "Baseline questionnaires", "week": "W1", "action": "Inclusion", "details": null}
{"event": "Initial assessment of the primary outcome", "week": "W2-W3", "action": "Dietary record (3 x 24 h)", "details": null}
{"event": "Dietetic appointment", "week": "W4", "action": "Face-to-face appointment", "details": "Booklet given"}
{"event": "Dietetic appointment", "week": "W6", "action": "Telephone appointment", "details": "Three advice"}
{"event": "Dietetic appointment", "week": "W8", "action": "Telephone appointment", "details": "Six advice"}
{"event": "Final assessment of the primary outcome", "week": "W11-W12", "action": "Dietary record (3 x 24 h)", "details": "Nine advice"}
{"event": "Final questionnaires", "week": "W12", "action": null, "details": null}
```

the adoption of healthier diets(19–21). However, despite their motivation to change their diets, pregnant women are not always successful and find themselves lost in the mass of confusing information provided on nutrition-related issues and are looking to receive credible and trustworthy dietary advice(21–23). This places pregnancy as a window of opportunity to implement dietary interventions by means of counselling. An increasing number of lifestyle interventions using dietary counselling and targeting pregnant women have thus been designed and have reported benefits regarding the consumption of fruits and vegetables(24,25), intakes of saturated fats, Ca, K, vitamins A and C, riboflavin and folate(24) or the correct contribution of macronutrients to energy intake(26). Furthermore, lifestyle interventions providing dietary counselling have also been shown to be beneficial to maternal and pregnancy outcomes such as weight gain(27,28), systolic and diastolic blood pressure(29) and the incidence of caesarian deliveries(27), although no clear effects of dietary counselling have been observed with respect to neonatal outcomes(30). Lifestyle interventions and the methods employed to deliver dietary counselling may vary. During the studies, most of these interventions were not tailored but individualised, meaning that a dietitian interacted with the woman in order to provide generic dietary recommendations and/or meal plans. However, nutrition interventions using a computer-based algorithm to provide tailored dietary counselling proved more efficient in improving the diet of individuals, while also reducing costs(31–33). Tailoring implied selecting the most appropriate characteristics of individuals to target the advice, using behaviour change techniques adapted to the target population and selecting the best computer-based device for data collection and advice provision(32). Our group recently developed a computer-based tailored dietary counselling approach for pregnant women, based on improving the nutrient adequacy of their individual diets, as assessed by the PANDiet score(34,35). The acceptability of this approach was evaluated in French pregnant women, and the results were used to refine it(35–37). However, no computer-based tailored dietary intervention which takes account of the global nutrient adequacy of the diet has been reported to date in pregnant women with a normal pre-pregnancy BMI. The objective of the present study was therefore to determine whether a guided, stepwise and tailored dietary counselling programme, based on an optimisation algorithm, could better improve the nutrient adequacy of the diet of pregnant women than an approach based solely on generic guidelines.

Methods

Study design and ethics

The present study was a 12-week, two-arm, single-blind, randomised, controlled clinical trial (Fig. 1). The present study was registered with the French National Agency for Medicines and Health Products Safety (Agence Nationale de Sécurité du Médicament et des Produits de Santé) with the identification number: ID RCB 2016-A00853648, under the administrative supervision of the French Ministry of Health. The present study was also approved by two French Ethics Committees (Comité de Protection des Personnes (CPP) Île-de-France II (identification number: 2016-07-02 MS1 SC) and Comité Consultatif sur le Traitement de l’Information en matière de Recherche dans le domaine de la Santé (CCTIRS) (identification number: 16–259)). The trial was registered at clinicaltrials.gov as NCT03084627. A written informed consent was obtained from all subjects before any data collection.

For inclusions, 186 women were approached when attending their first appointment with the midwife in the maternity clinic or by means of flyers and posters displayed in the clinic’s waiting rooms. On the day of their inclusion, all participants filled in three questionnaires. The first focused on social and demographic features, the second assessed some pregnancy characteristics (gestational diabetes, number of fetus and complications during current and previous pregnancies) and the third evaluated basic characteristics of their lifestyle (including diet). The baseline characteristics of participants are presented in Table 1. The participants were randomised within 2 weeks of their inclusion; during weeks 2 and 3 (initial assessment), their diet was evaluated from a 3-d online dietary record (see the ‘Dietary assessments’ section). At the beginning of week 5, the participants attended their first dietetic appointment with the dietitian, which lasted between 30 and 45 min. Details about the content of dietetic appointments for the control and intervention arms are available in the ‘Content of dietetic appointments’ section. At the beginning of weeks 7 and 9, all participants were contacted by telephone by the dietitian regarding their second and third dietetic appointments. During weeks 11 and 12 (final assessment), their diet was evaluated as during weeks 2 and 3. After completing their last diet record, the participants filled two online questionnaires about changes to their dietary habits during pregnancy and the dietary counselling they received during the study. The final questionnaire differed between the control and intervention arms.

Table 1. Characteristics of the women included in the analysis of the randomised controlled trial by arm* (control arm:
n 38; intervention arm: n 40) and for the total study population (n 78)
(Mean values and standard deviations; percentages and numbers)

```jsonl
{"Characteristic": "Age (years)", "Control (n 38) %": null, "Control (n 38) n": null, "Intervention (n 40) %": null, "Intervention (n 40) n": null, "Total (n 78) %": null, "Total (n 78) n": null}
{"Characteristic": "Mean", "Control (n 38) %": 31.4, "Control (n 38) n": null, "Intervention (n 40) %": 31.5, "Intervention (n 40) n": null, "Total (n 78) %": 31.4, "Total (n 78) n": null}
{"Characteristic": "sd", "Control (n 38) %": 3.63, "Control (n 38) n": null, "Intervention (n 40) %": 3.69, "Intervention (n 40) n": null, "Total (n 78) %": 3.64, "Total (n 78) n": null}
{"Characteristic": "Number of children†", "Control (n 38) %": null, "Control (n 38) n": null, "Intervention (n 40) %": null, "Intervention (n 40) n": null, "Total (n 78) %": null, "Total (n 78) n": null}
{"Characteristic": "0", "Control (n 38) %": 65.8, "Control (n 38) n": 25, "Intervention (n 40) %": 62.5, "Intervention (n 40) n": 25, "Total (n 78) %": 64.1, "Total (n 78) n": 50}
{"Characteristic": "1", "Control (n 38) %": 29.0, "Control (n 38) n": 11, "Intervention (n 40) %": 30.0, "Intervention (n 40) n": 12, "Total (n 78) %": 29.5, "Total (n 78) n": 23}
{"Characteristic": "2", "Control (n 38) %": 5.3, "Control (n 38) n": 2, "Intervention (n 40) %": 5.0, "Intervention (n 40) n": 2, "Total (n 78) %": 5.1, "Total (n 78) n": 4}
{"Characteristic": "3", "Control (n 38) %": 0.0, "Control (n 38) n": 0, "Intervention (n 40) %": 2.5, "Intervention (n 40) n": 1, "Total (n 78) %": 1.3, "Total (n 78) n": 1}
{"Characteristic": "Socio-professional group†‡", "Control (n 38) %": null, "Control (n 38) n": null, "Intervention (n 40) %": null, "Intervention (n 40) n": null, "Total (n 78) %": null, "Total (n 78) n": null}
{"Characteristic": "Craftsperson, storekeeper", "Control (n 38) %": 5.3, "Control (n 38) n": 2, "Intervention (n 40) %": 0.0, "Intervention (n 40) n": 0, "Total (n 78) %": 2.6, "Total (n 78) n": 2}
{"Characteristic": "Senior executive", "Control (n 38) %": 60.5, "Control (n 38) n": 23, "Intervention (n 40) %": 52.5, "Intervention (n 40) n": 21, "Total (n 78) %": 56.4, "Total (n 78) n": 44}
{"Characteristic": "Intermediate profession", "Control (n 38) %": 10.5, "Control (n 38) n": 4, "Intervention (n 40) %": 15.0, "Intervention (n 40) n": 6, "Total (n 78) %": 12.8, "Total (n 78) n": 10}
{"Characteristic": "Employee", "Control (n 38) %": 15.8, "Control (n 38) n": 6, "Intervention (n 40) %": 17.5, "Intervention (n 40) n": 7, "Total (n 78) %": 16.7, "Total (n 78) n": 13}
{"Characteristic": "Student", "Control (n 38) %": 0.0, "Control (n 38) n": 0, "Intervention (n 40) %": 2.5, "Intervention (n 40) n": 1, "Total (n 78) %": 1.3, "Total (n 78) n": 1}
{"Characteristic": "Inactive", "Control (n 38) %": 5.3, "Control (n 38) n": 2, "Intervention (n 40) %": 7.5, "Intervention (n 40) n": 3, "Total (n 78) %": 6.4, "Total (n 78) n": 5}
{"Characteristic": "Other", "Control (n 38) %": 1.3, "Control (n 38) n": 1, "Intervention (n 40) %": 5.0, "Intervention (n 40) n": 1, "Total (n 78) %": 3.9, "Total (n 78) n": 3}
{"Characteristic": "Highest diploma†‡", "Control (n 38) %": null, "Control (n 38) n": null, "Intervention (n 40) %": null, "Intervention (n 40) n": null, "Total (n 78) %": null, "Total (n 78) n": null}
{"Characteristic": "PhD or MD", "Control (n 38) %": 2.6, "Control (n 38) n": 1, "Intervention (n 40) %": 2.5, "Intervention (n 40) n": 1, "Total (n 78) %": 2.6, "Total (n 78) n": 2}
{"Characteristic": "Master", "Control (n 38) %": 60.5, "Control (n 38) n": 23, "Intervention (n 40) %": 67.5, "Intervention (n 40) n": 27, "Total (n 78) %": 64.1, "Total (n 78) n": 50}
{"Characteristic": "Bachelor", "Control (n 38) %": 7.9, "Control (n 38) n": 3, "Intervention (n 40) %": 10.0, "Intervention (n 40) n": 4, "Total (n 78) %": 9.0, "Total (n 78) n": 7}
{"Characteristic": "Undergraduate\n(2 years after high school)", "Control (n 38) %": 18.4, "Control (n 38) n": 7, "Intervention (n 40) %": 12.5, "Intervention (n 40) n": 5, "Total (n 78) %": 15.4, "Total (n 78) n": 12}
{"Characteristic": "High school diploma", "Control (n 38) %": 7.5, "Control (n 38) n": 3, "Intervention (n 40) %": 2.5, "Intervention (n 40) n": 1, "Total (n 78) %": 5.1, "Total (n 78) n": 4}
{"Characteristic": "Technical diploma\n(2 years after middle school)", "Control (n 38) %": 2.6, "Control (n 38) n": 1, "Intervention (n 40) %": 2.5, "Intervention (n 40) n": 1, "Total (n 78) %": 2.6, "Total (n 78) n": 2}
{"Characteristic": "No diploma, middle school education", "Control (n 38) %": 0.0, "Control (n 38) n": 0, "Intervention (n 40) %": 2.5, "Intervention (n 40) n": 1, "Total (n 78) %": 1.3, "Total (n 78) n": 1}
{"Characteristic": "Household monthly income†‡", "Control (n 38) %": null, "Control (n 38) n": null, "Intervention (n 40) %": null, "Intervention (n 40) n": null, "Total (n 78) %": null, "Total (n 78) n": null}
{"Characteristic": "<€500", "Control (n 38) %": 0.0, "Control (n 38) n": 0, "Intervention (n 40) %": 2.5, "Intervention (n 40) n": 1, "Total (n 78) %": 1.3, "Total (n 78) n": 1}
{"Characteristic": "€2000–2999", "Control (n 38) %": 15.8, "Control (n 38) n": 6, "Intervention (n 40) %": 12.5, "Intervention (n 40) n": 5, "Total (n 78) %": 14.1, "Total (n 78) n": 11}
{"Characteristic": "€3000–3999", "Control (n 38) %": 13.2, "Control (n 38) n": 5, "Intervention (n 40) %": 12.5, "Intervention (n 40) n": 5, "Total (n 78) %": 12.8, "Total (n 78) n": 10}
{"Characteristic": "€4000–4999", "Control (n 38) %": 26.3, "Control (n 38) n": 10, "Intervention (n 40) %": 20.0, "Intervention (n 40) n": 8, "Total (n 78) %": 23.1, "Total (n 78) n": 18}
{"Characteristic": "≥€5000", "Control (n 38) %": 44.7, "Control (n 38) n": 17, "Intervention (n 40) %": 52.5, "Intervention (n 40) n": 21, "Total (n 78) %": 48.7, "Total (n 78) n": 38}
{"Characteristic": "Number of weeks of amenorrhoea", "Control (n 38) %": null, "Control (n 38) n": null, "Intervention (n 40) %": null, "Intervention (n 40) n": null, "Total (n 78) %": null, "Total (n 78) n": null}
{"Characteristic": "Mean", "Control (n 38) %": 18.8, "Control (n 38) n": null, "Intervention (n 40) %": 19.1, "Intervention (n 40) n": null, "Total (n 78) %": 19.0, "Total (n 78) n": null}
{"Characteristic": "sd", "Control (n 38) %": 2.51, "Control (n 38) n": null, "Intervention (n 40) %": 2.76, "Intervention (n 40) n": null, "Total (n 78) %": 2.63, "Total (n 78) n": null}
{"Characteristic": "Primiparous†", "Control (n 38) %": 65.8, "Control (n 38) n": 25, "Intervention (n 40) %": 62.5, "Intervention (n 40) n": 25, "Total (n 78) %": 64.1, "Total (n 78) n": 50}
{"Characteristic": "Attention to a healthy diet", "Control (n 38) %": null, "Control (n 38) n": null, "Intervention (n 40) %": null, "Intervention (n 40) n": null, "Total (n 78) %": null, "Total (n 78) n": null}
{"Characteristic": "Before this pregnancy†§", "Control (n 38) %": null, "Control (n 38) n": null, "Intervention (n 40) %": null, "Intervention (n 40) n": null, "Total (n 78) %": null, "Total (n 78) n": null}
{"Characteristic": "Totally agree", "Control (n 38) %": 31.6, "Control (n 38) n": 12, "Intervention (n 40) %": 32.5, "Intervention (n 40) n": 13, "Total (n 78) %": 32.1, "Total (n 78) n": 25}
{"Characteristic": "Agree", "Control (n 38) %": 57.9, "Control (n 38) n": 22, "Intervention (n 40) %": 52.5, "Intervention (n 40) n": 21, "Total (n 78) %": 55.1, "Total (n 78) n": 43}
{"Characteristic": "Neither agree nor disagree", "Control (n 38) %": 10.5, "Control (n 38) n": 4, "Intervention (n 40) %": 10.0, "Intervention (n 40) n": 4, "Total (n 78) %": 10.3, "Total (n 78) n": 9}
{"Characteristic": "Disagree", "Control (n 38) %": 0.0, "Control (n 38) n": 0, "Intervention (n 40) %": 2.5, "Intervention (n 40) n": 1, "Total (n 78) %": 1.3, "Total (n 78) n": 1}
{"Characteristic": "Totally disagree", "Control (n 38) %": 0.0, "Control (n 38) n": 0, "Intervention (n 40) %": 2.5, "Intervention (n 40) n": 1, "Total (n 78) %": 1.3, "Total (n 78) n": 1}
{"Characteristic": "Since the beginning of pregnancy†||", "Control (n 38) %": null, "Control (n 38) n": null, "Intervention (n 40) %": null, "Intervention (n 40) n": null, "Total (n 78) %": null, "Total (n 78) n": null}
{"Characteristic": "Totally agree", "Control (n 38) %": 47.4, "Control (n 38) n": 18, "Intervention (n 40) %": 35.0, "Intervention (n 40) n": 14, "Total (n 78) %": 41.0, "Total (n 78) n": 32}
{"Characteristic": "Agree", "Control (n 38) %": 31.6, "Control (n 38) n": 12, "Intervention (n 40) %": 50.0, "Intervention (n 40) n": 20, "Total (n 78) %": 41.0, "Total (n 78) n": 32}
{"Characteristic": "Neither agree nor disagree", "Control (n 38) %": 13.2, "Control (n 38) n": 5, "Intervention (n 40) %": 12.5, "Intervention (n 40) n": 5, "Total (n 78) %": 12.8, "Total (n 78) n": 10}
{"Characteristic": "Disagree", "Control (n 38) %": 5.3, "Control (n 38) n": 2, "Intervention (n 40) %": 2.5, "Intervention (n 40) n": 1, "Total (n 78) %": 3.9, "Total (n 78) n": 3}
{"Characteristic": "Totally disagree", "Control (n 38) %": 2.6, "Control (n 38) n": 1, "Intervention (n 40) %": 0.0, "Intervention (n 40) n": 0, "Total (n 78) %": 1.3, "Total (n 78) n": 1}
```

* There was no difference between the arms regarding all the variables presented, as assessed using either Student's t tests for continuous
variables or Fisher's exact tests for categorical variables. P > 0·05.
† Values correspond to the percentage of participants presenting the characteristic followed by the associated number of participants.
‡ Only answers including at least one participant are presented in the table.
§ The statement was as follows: 'Before this pregnancy, I paid a specific attention to consuming a healthy and balanced diet'.
|| The statement was as follows: 'Since the beginning of this pregnancy, I have paid more attention to consuming a healthy and balanced diet'.

The primary outcome measure of the study was differences in
the PANDiet score between the initial and final dietary assessments.
The secondary outcome measures of the study were changes in the
values of the items composing the PANDiet score (adequacy and
moderation subscores and probabilities of adequacy for nutrient
intakes – see the ‘Assessment of nutrient adequacy’ section), the
frequency with which participants read the booklet in both arms
and implementation of the advice they had received (number
and frequency) in the intervention arm only.

Participants

All participants were attending Notre-Dame de Bon Secours
Maternity Clinic (Hôpital Paris Saint-Joseph, Paris, France) for

Tailored dietary counselling in pregnancy

223

Fig. 2. Flow diagram of a participant's progress through the study.

```jsonl
{"node": "Enrolment", "type": "process"}
{"node": "Assessed for eligibility (n 186)", "details": "Maternity information meeting (n 15)\nFirst consultation with a midwife in the maternity clinic (n 168)\nPoster in the waiting room in the maternity clinic (n 3)", "type": "process"}
{"node": "Excluded (n 106)", "details": "Amenorrhoea weeks ≥ 24 (n 45)\nNot willing to participate (n 34)\nBMI ∉ 18·5–25 kg/m² (n 14)\nNot fluent in French (n 6)\nAge > 40 years old (n 3)\nGestational diabetes (n 2)\nMajor food allergies (n 2)", "type": "process"}
{"node": "Randomised (n 80)", "type": "process"}
{"node": "Allocation", "type": "process"}
{"node": "Control group (n 40)", "type": "process"}
{"node": "Intervention group (n 40)", "type": "process"}
{"node": "Follow-up", "details": "Completed initial questionnaires (n 40)", "group": "Control", "type": "process"}
{"node": "Follow-up", "details": "Completed initial questionnaires (n 40)", "group": "Intervention", "type": "process"}
{"node": "Excluded (n 2)", "details": "Loss to follow-up (n 1)\nMiscarriage (n 1)", "group": "Control", "type": "process"}
{"node": "Follow-up", "details": "Completed the initial dietary record (n 38)\nAttended the first appointment (in person) (n 38)\nAttended the second and third appointments (by telephone) (n 38)\nCompleted the final dietary record (n 38)\nCompleted final online questionnaires (n 38)", "group": "Control", "type": "process"}
{"node": "Follow-up", "details": "Completed the initial dietary record (n 40)\nAttended the first appointment (in person) (n 40)\nAttended the second and third appointments (by telephone) (n 40)\nCompleted the final dietary record (n 40)\nCompleted final online questionnaires (n 40)", "group": "Intervention", "type": "process"}
{"node": "Analysis", "details": "Analysed (n 38)", "group": "Control", "type": "process"}
{"node": "Analysis", "details": "Analysed (n 40)", "group": "Intervention", "type": "process"}
{"source": "Enrolment", "target": "Assessed for eligibility (n 186)", "type": "flow"}
{"source": "Assessed for eligibility (n 186)", "target": "Excluded (n 106)", "type": "flow"}
{"source": "Assessed for eligibility (n 186)", "target": "Randomised (n 80)", "type": "flow"}
{"source": "Randomised (n 80)", "target": "Allocation", "type": "flow"}
{"source": "Allocation", "target": "Control group (n 40)", "type": "flow"}
{"source": "Allocation", "target": "Intervention group (n 40)", "type": "flow"}
{"source": "Control group (n 40)", "target": "Follow-up (Control initial)", "type": "flow"}
{"source": "Intervention group (n 40)", "target": "Follow-up (Intervention initial)", "type": "flow"}
{"source": "Follow-up (Control initial)", "target": "Excluded (n 2)", "type": "flow"}
{"source": "Follow-up (Control initial)", "target": "Follow-up (Control final)", "type": "flow"}
{"source": "Follow-up (Intervention initial)", "target": "Follow-up (Intervention final)", "type": "flow"}
{"source": "Follow-up (Control final)", "target": "Analysis (Control)", "type": "flow"}
{"source": "Follow-up (Intervention final)", "target": "Analysis (Intervention)", "type": "flow"}
```

their antenatal care. The inclusion criteria were as follows:
female, pregnant, 10–24 weeks of amenorrhoea, 18–40 years
old, BMI of 18·5–25 kg/m², fluent in speaking, reading and writ-
ing French, an opportunity for daily Internet access, a valid email
and telephone number and benefiting from French national
health insurance. Non-inclusion criteria were as follows: multi-
ple pregnancy, at-risk pregnancy (according to the clinic’s
classification), history of gestational diabetes mellitus (for mul-
tiparous women), health conditions requiring a specific diet,
vegan diets or allergies to one or more of the major allergens
listed in Regulation no. 1169/2011 of the European Parliament
and of the Council. Exclusion criteria included a diagnosis of

gestational diabetes during the study period (12 weeks), a diag-
nosis of pregnancy complications requiring modifications to the
diet or spontaneous abortion. The participants were randomly
allocated to two groups in blocks of twelve that were balanced
as a function of age, BMI, parity (percentage of primiparous
women in each arm) and household income level, using a math-
ematical method to minimise differences between the arms. The
participants were blinded to the existence of two different dietary
counselling approaches. All participants were compensated for
their trips to the clinic, and the time they spent completing the
study with a maximum of 400€ for complete participation. A

diagram of subject flow according to Consolidated Standards of Reporting Trials (CONSORT) guidelines is presented in Fig. 2.

### Dietary assessments

Dietary data were recorded online using Dietlib’ (MyGoodLife), which is a professional tool used by French dietitians for patient care that complies with the requirements of the French National Health Authority and the French Association of Dietitians and Nutritionists. The software included a 3-d dietary record using a closed food list (6287 food items). Portion sizes were estimated using coloured images from a national food portion guidebook(38), household measures (e.g. one teaspoon) or commercial servings (e.g. a standard yogurt).

Three non-consecutive days, including 2 weekdays and 1 weekend day, were randomly selected for the initial (weeks 2 and 3) and final (weeks 11 and 12) dietary assessments. The participants were informed of the dates for their diet recording periods at least 7 d beforehand. Before each day of recording, an electronic reminder was sent to the participant. Each day of the record was checked by the dietitian within 48 h of its completion; if any inconsistencies were seen, the participant was contacted by email. Based on these 3-d records, the energy intake excluding alcohol (EIEA):BMR ratio (determined according to Black(39)) of the participants was calculated. A ratio below 1 was considered to be a potential indicator of underreporting, and the participant was contacted and asked to check her dietary records. This contact did not aim at increasing the ratio. If required, the dietary record could slightly be updated.

The nutrient values used to calculate nutrient intake came from the French food composition database (CIQUAL 2013(40)). In exceptional cases, participants might have declared a food item for which no correspondence with the CIQUAL database could be made, so the nutrient values were those provided by the retailer and already included in the software database. For each participant, the mean intakes calculated included weighting for the day of the week (weekday or weekend day) with respect to the following nutrients: alcohol, protein, total carbohydrate, starch, sugars, added sugars, free sugars, total fat, PUFA, α-linolenic acid (ALA), linoleic acid, EPA, DHA, MUFA, SFA, cholesterol, dietary fibre, vitamin A, thiamin, riboflavin, niacin, pantothenic acid, vitamin B6, folate, vitamins B12, C, D and E, Ca, iodine, Fe, Mg, P, K, Se and Zn.

### Assessment of nutrient adequacy

The nutrient adequacy of each participant’s diet was assessed from the initial and final dietary records using the PANDiet diet quality index, previously adapted to the specific requirements for the third trimester of pregnancy(34). Briefly, the PANDiet aims to measure the overall diet quality of an individual by combining the probabilities of having an adequate intake of nutrients. The PANDiet is a 100-point score that results from averaging two subscores, the Adequacy sub-score (Adeq-S) and the Moderation sub-score (Mod-S); the higher the PANDiet score, the better the nutrient adequacy. Each sub-score is composed of probabilities of adequacy for nutrients (27 for Adeq-S: protein, total carbohydrate, dietary fibre, total fat, linoleic acid, ALA, DHA, EPA+DHA, vitamin A, thiamin, riboflavin, niacin, pantothenic acid, vitamin B6, folate, vitamins B12, C, D, E, Ca, iodine, Fe, Mg, P, K, Se and Zn and 7 for Mod-S: protein, total carbohydrate, free sugars, total fat, SFA, cholesterol and Na), with a further fourteen potential penalties for exceeding the tolerable upper intake limits (retinol, niacin, vitamin B6, folate, vitamins C, D, E, Ca, iodine, Fe, Mg, P, Se and Zn) which are added to Mod-S. Because DHA intakes are considered in the probabilities of adequacy for both DHA and EPA+DHA intakes, each one was weighted by 0·5 in the final score, resulting in an Adeq-S with twenty-six probabilities of adequacy for nutrient intakes. The dietary reference values used to calculate PANDiet were mostly those issued by the French Agency for Food, Environmental and Occupational Health (Agence Nationale de Sécurité Sanitaire de l’alimentation, de l’environnement et du travail, ANSES)(34,41).

### Content of dietetic appointments

Control arm. During the first dietetic appointment, participants in the control arm received generic dietary advice based on a booklet edited by the French Institute for Health Promotion and Health Education (Institut National de Prévention et d’Education pour la Santé, INPES)(42). Sections from the booklet were read and briefly commented on by the dietitian with each participant during the 30 min appointment. The booklet was then given to the participant, who was also informed of their initial PANDiet score. During the second and third dietetic appointments, participants in the control arm were asked if they had any questions about the booklet contents. If any medical questions came, women were referred to their antenatal care provider.

Intervention arm (method used to generate tailored dietary advice). During the first dietetic appointment, participants in the intervention arm also received the INPES booklet, which was read and commented on by the dietitian as for the control arm. But, they also received three pieces of tailored dietary advice generated by the optimisation software in order to improve the nutrient adequacy of their diets, as evaluated by the PANDiet score adapted for pregnancy(34,35). The participants were informed of their initial PANDiet score at the start of the appointment, and it was explained that each piece of dietary advice proposed by the software could optimally improve their initial score. The software included an algorithm that calculated the initial PANDiet score of each participant (using her dietary data), then implemented a stepwise dietary optimisation model designed to improve the initial PANDiet score. For each piece of dietary advice, a participant could choose between three options proposed by the algorithm, two that best increased the PANDiet score by replacing a food item consumed in the initial diet with a food item from the same subgroup, and one that best increased the PANDiet score by modifying the amount consumed of a food item from the initial diet. These two types of dietary advice have already been described in depth and were chosen by considering a trade-off between their theoretical nutritional efficiency and their acceptability as evaluated during previous studies(35,37).

The theoretical increase in the PANDiet score resulting from each option was communicated to the subject who then selected her preference. This choice was then implemented in the dietary

record as a theoretical change that had been made, and the corresponding PANDiet score was calculated. This PANDiet score
served as a reference to generate a new set of three options.
At each step, tailored dietary advice should not decrease the
initial EIEA and not increase it by more than 795 kJ (i.e. the difference between the increase in energy requirements between the
first and second trimester of pregnancy according to EFSA
guidelines).

During the second and third dietetic appointments, participants in the intervention arm were asked if they had any questions about the booklet. They also received three more pieces of
tailored dietary advice according to the process detailed above.
In total, after the third dietetic appointment, participants in
the intervention arm had received nine pieces of tailored
dietary advice.

After each appointment, an email was sent to each participant
that included the following information: her initial PANDiet
score, the list of dietary advice that she had chosen during all previous appointments (i.e. three after the first dietetic appointment,
six after the second one and nine after the third one), the theoretical increase in the PANDiet score procured by each change
and an encouragement to read the booklet. A reminder was sent
out 1 week after each appointment.

To maintain the same intensity of interaction between the
dietitian and participants in the intervention and control arms,
participant in the control arm also received an email after each
appointment and 1 week after that included the following information: her initial PANDiet score and an encouragement to read
the booklet.

### Statistical analyses

Sample size calculation. We computed the sample size
required to obtain a statistically significant difference in the
PANDiet score (primary outcome) between the two arms. A
5-point difference was defined as being nutritionally significant,
based on our previous simulation studies(34,35). This difference
was the interquartile range in the population whose standard
deviation was 7 points(34). Furthermore, in our simulations, the
least theoretically efficient type of advice resulted in an approximately 1 point improvement per piece of advice, with a probability of intention to use it of approximately 0·6, so we reasoned that
the nine dietary changes provided in the present study could be
expected to lead to an approximately 5-point improvement in the
PANDiet score(35). Considering a sd of 7 points for the PANDiet
score, a two-side power calculation required thirty-two participants per group, with an 80 % (β = 0·80) chance of demonstrating
an effect of intervention on the PANDiet score at a 95 % confidence level (α = 0·05). Allowing for a 20 % dropout rate, we therefore sought to include forty participants per arm.

Descriptive and inferential statistics. Descriptive statistics
(means, sd, sem and quartiles) were used to present continuous
variables, and percentages were used for categorical variables.
Differences between the arms were determined using
Student’s t tests for continuous variables and Fisher’s exact tests
for categorical variables. The change in the PANDiet score and its

associated subscores and the probabilities of adequacy for
nutrient intakes were calculated as the final value minus the initial value. The primary outcome measure of the study was the
change in the PANDiet score. In a first model, which addressed
the pre-specified analysis, we tested the effect of the intervention
using a t test, while further models of analysis were secondary
post hoc analyses. In a second model, we added the initial
PANDiet score as a covariate using ANCOVA. Control variables
were included as well as the intervention and initial PANDiet
scores in two additional models to test for possible
prediction of the change in the score. The third model included
the following control variables assessed at baseline: age, BMI,
parity, household income per person, level of education and
attention paid to the diet score (sum of attention paid to the diet
before pregnancy and since the start of pregnancy assessed
using five-point Likert scales). The fourth model also included
the control variables assessed in the final questionnaires:
attention paid to reading the booklet (four levels: Reading each
section of the booklet very carefully – Reading the booklet with
variations in attention depending on the section – Not reading
the entire booklet but only the summary sheet presented on
the two last pages – Not reading the booklet at all) and the attention paid to the diet since the start of the study (assessed using a
five-point Likert scale).

A secondary analysis was performed in the intervention arm
to determine whether changes in the PANDiet score differed
depending on the number of pieces of advice actually implemented in the diet (as declared by the participant in the final
questionnaire) or the sum of the frequency of implementing
advice (as evaluated by the participant in the final questionnaire
using a five-level scale for each point: the score was calculated
by attributing 0·25 points per level from always (1 point) to never
(0 points)).

All analyses were performed using SAS 9.1.3 (SAS Institute
Inc.). P < 0·05 was considered to be statistically significant.

## Results

### Characteristics of participants

Of the eighty women included between September and
November 2016, equal numbers (n 40) were randomly assigned
to each arm and seventy-eight women (thirty-eight in the control
arm and forty in the intervention arm) completed the study
(Fig. 2). The mean age of participants was 31 (sd 3·6) years
(Table 1), about one-third of whom (35 %) already had at least
one child. More than half of the women (56 %) belonged to
the ‘senior executive’ socio-professional group and almost half
(49 %) had a household income higher than €5000 per month.
Almost all the women (91 %) had pursued their education for
at least 2 years after high school. At inclusion, the mean number
of weeks of amenorrhoea was 19 (sd 2·6). A great majority of the
women in our study (87 %) had paid specific attention to consuming a healthy and balanced diet before this pregnancy,
and 82 % declared they had paid more attention such consumption since the start of this pregnancy. No differences between the
arms were observed regarding all these variables.

226
C. M. Bianchi et al.

Table 2. Initial and final PANDiet scores and associated sub-scores and their changes by arm (control arm: n 38; intervention arm: n 40)
(Mean values and standard deviations)

```jsonl
{"Score": "PANDiet", "Control (n 38)_Initial_Mean": 60.4, "Control (n 38)_Initial_SD": 7.3, "Control (n 38)_Final_Mean": 60.1, "Control (n 38)_Final_SD": 8.7, "Control (n 38)_Change†_Mean": -0.3, "Control (n 38)_Change†_SD": 7.3, "Control (n 38)_P‡": 0.77, "Intervention (n 40)_Initial_Mean": 60.3, "Intervention (n 40)_Initial_SD": 7.3, "Intervention (n 40)_Final_Mean": 63.9, "Intervention (n 40)_Final_SD": 8.1, "Intervention (n 40)_Change†_Mean": 3.6, "Intervention (n 40)_Change†_SD": 9.3, "Intervention (n 40)_P‡": 0.02, "Intervention (n 40)_P*": 0.039}
{"Score": "Adeq-S", "Control (n 38)_Initial_Mean": 53.3, "Control (n 38)_Initial_SD": 17.0, "Control (n 38)_Final_Mean": 51.6, "Control (n 38)_Final_SD": 16.6, "Control (n 38)_Change†_Mean": -1.7, "Control (n 38)_Change†_SD": 17.0, "Control (n 38)_P‡": 0.50, "Intervention (n 40)_Initial_Mean": 55.6, "Intervention (n 40)_Initial_SD": 14.1, "Intervention (n 40)_Final_Mean": 58.9, "Intervention (n 40)_Final_SD": 15.9, "Intervention (n 40)_Change†_Mean": 3.4, "Intervention (n 40)_Change†_SD": 15.6, "Intervention (n 40)_P‡": 0.15, "Intervention (n 40)_P*": 0.18}
{"Score": "Mod-S", "Control (n 38)_Initial_Mean": 67.6, "Control (n 38)_Initial_SD": 13.7, "Control (n 38)_Final_Mean": 68.6, "Control (n 38)_Final_SD": 13.5, "Control (n 38)_Change†_Mean": 1.0, "Control (n 38)_Change†_SD": 13.7, "Control (n 38)_P‡": 0.69, "Intervention (n 40)_Initial_Mean": 65.0, "Intervention (n 40)_Initial_SD": 12.3, "Intervention (n 40)_Final_Mean": 68.8, "Intervention (n 40)_Final_SD": 11.6, "Intervention (n 40)_Change†_Mean": 3.9, "Intervention (n 40)_Change†_SD": 12.4, "Intervention (n 40)_P‡": 0.06, "Intervention (n 40)_P*": 0.38}
```

Adeq-S, Adequacy sub-score; Mod-S, Moderation sub-score.
* Student's t tests were performed to determine whether the changes differed between arms.
† Difference between the values obtained from the final dietary record and the initial dietary record in each arm.
‡ Student's t tests were performed to determine whether the mean changes within each group were different from 0.

Effect of tailored dietary advice on changes to the
PANDiet score

The mean initial PANDiet scores were approximately 60 points
and similar in both arms (Table 2). The PANDiet increased
significantly in the intervention arm (+3·6 (sd 9·3) points) but
remained unchanged in the control arm (−0·3 (sd 7·3) points),
and the change in the intervention arm differed from that in
the control arm. No effect of the intervention was observed in
the change of the sub-scores or probabilities of adequacy except
for ALA (whose improvement was significantly higher in the
intervention arm). The probabilities of adequacy for ALA, thia-
min, folate and cholesterol intakes increased in the intervention
arm. The initial and final probabilities of adequacy composing
the PANDiet score, as well as their changes, are presented by
arm in online Supplementary Table S1. The mean initial EIEA
values were 7858 (sd 1782) kJ/d in the total population, with
no difference between the arms, while the mean final EIEA val-
ues were 7740 (sd 1674) kJ/d, with no difference between the
arms. No differences in the change of the EIEA were observed
between the arms.

Effect of the initial PANDiet score on the change in the
PANDiet score

The higher the initial PANDiet score, the less marked was the
change in the PANDiet score (β = −0·49; P < 0·0001) and we
found an interaction between the initial PANDiet score and the
effect of the intervention. When stratifying according to quartiles
of the initial PANDiet score, the improvement in the PANDiet
score was greater in the first than in the last initial PANDiet quar-
tile. After a median split, we found that in the population with a
lower initial PANDiet score, the change in the PANDiet score was
0·70 (sd 8·02) in the control arm and 7·32 (sd 7·41) in the interven-
tion arm, which was approximately twice the degree of effect
found for the whole population (Fig. 3).

Analysis with control variables

Using model 3, we found that as well as the intervention, the ini-
tial PANDiet score and the attention paid to the diet score had an
effect on the change of the PANDiet score. When other control
variables were added (determined at the end of the study), same
results were found as well as some trends regarding the effects of

the attention paid to reading the booklet and to the diet since the
start of the study (P = 0·08 for both variables).

Evaluation of tailored dietary counselling

Fewer than 5 % of women in each arm did not read the booklet at
all after the first dietetic appointment. Participants in the control
arm read the booklet more often than those in the intervention
arm. Indeed, 29·0 % of the women in the control arm declared
that they read the booklet five times or more, whereas all women
in the intervention arm read it four times or less. Table 3 summa-
rises the characteristics of the dietary advice chosen by women in
the intervention arm (number by type, number of pieces of
advice implemented in the diet and intensity of implementation
of this advice). There was no difference between the number of
pieces of dietary advice involving modifications to the amounts
consumed (4·4 (sd 1·7)) and the number of dietary advice involv-
ing a substitution (4·6 (sd 1·7)) chosen by the participants.
Women in the intervention arm largely reported having imple-
mented the dietary advice (intensity of implementation:
5·7 (sd 1·4) points out of 9). In the intervention arm, we found
no effect of the number of pieces of advice effectively imple-
mented in the diet or of the intensity of their implementation
on the change in the PANDiet score.

Discussion

Tailored dietary counselling using a computer-based algorithm
was more efficient than (pregnancy-focused) generic dietary
counselling alone in improving the nutrient adequacy of the diet
of French women in mid-pregnancy. An improvement in the
nutrient adequacy of the diet was observed among participants
who received generic plus tailored dietary counseling, whereas
no such change was detected among those who only received
generic dietary counselling based on a booklet. Furthermore,
we found that the intervention improved the probabilities of
adequacy for key nutrient intakes during pregnancy such as
ALA and folate.

Among interventions that offer dietary counselling to
pregnant women, some have proved effective in improving diet
quality during pregnancy(28–30). However, these interventions
differ considerably in terms of the characteristics of the women
concerned, the nature of dietary counselling and its objective

Tailored dietary counselling in pregnancy 227

Fig. 3. Box plots of the change in PANDiet score by quartiles of the initial PANDiet score for the total population ((A) n 78), for the control arm ((B) n 38) and for the intervention arm ((C) n 40). The white bars represent the first quartile of the PANDiet score, and the light grey bars represent the second quartile of the PANDiet score. The middle grey bars represent the third quartile of the PANDiet score, and the dark grey bars represent the fourth quartile of the PANDiet score. The middle line in the box plots shows the median, the cross in the box plots shows the mean, the bottom and top of the box are the 25th and 75th percentiles, respectively, and the ends of the whiskers represent the 5th and 95th percentiles. This analysis was a secondary, post hoc analysis. a,b Values with unlike letters are significantly different within the same panel. Q1, first quartile; Q2, second quartile; Q3, third quartile; Q4, fourth quartile.

```jsonl
{"panel": "A", "population": "Total population (n 78)", "quartile": "Q1", "median": 13, "mean": 4.5, "q1": -4, "q3": 13, "p5": -10, "p95": 15, "significance": "a"}
{"panel": "A", "population": "Total population (n 78)", "quartile": "Q2", "median": 6, "mean": 4, "q1": -1.5, "q3": 9.5, "p5": -11, "p95": 16, "significance": "a, b"}
{"panel": "A", "population": "Total population (n 78)", "quartile": "Q3", "median": 0, "mean": 0, "q1": -4, "q3": 7, "p5": -15, "p95": 12, "significance": "a, b"}
{"panel": "A", "population": "Total population (n 78)", "quartile": "Q4", "median": -1, "mean": -3, "q1": -9.5, "q3": 3, "p5": -17, "p95": 7, "significance": "b"}
{"panel": "B", "population": "Control (n 38)", "quartile": "Q1", "median": 4, "mean": 2, "q1": -3, "q3": 9.5, "p5": -11, "p95": 14, "significance": null}
{"panel": "B", "population": "Control (n 38)", "quartile": "Q2", "median": 0, "mean": -1, "q1": -5, "q3": 3, "p5": -12, "p95": 6, "significance": null}
{"panel": "B", "population": "Control (n 38)", "quartile": "Q3", "median": -1, "mean": -1, "q1": -5, "q3": 4.5, "p5": -14, "p95": 9.5, "significance": null}
{"panel": "B", "population": "Control (n 38)", "quartile": "Q4", "median": -2, "mean": -3, "q1": -8, "q3": 3, "p5": -12, "p95": 6, "significance": null}
{"panel": "C", "population": "Intervention (n 40)", "quartile": "Q1", "median": 11, "mean": 8, "q1": 1.5, "q3": 14, "p5": -8.5, "p95": 16, "significance": null}
{"panel": "C", "population": "Intervention (n 40)", "quartile": "Q2", "median": 8, "mean": 8, "q1": 1.5, "q3": 12.5, "p5": -4.5, "p95": 16, "significance": null}
{"panel": "C", "population": "Intervention (n 40)", "quartile": "Q3", "median": 1, "mean": 1, "q1": -2.5, "q3": 9, "p5": -10.5, "p95": 12, "significance": null}
{"panel": "C", "population": "Intervention (n 40)", "quartile": "Q4", "median": -2, "mean": -4, "q1": -10.5, "q3": 5, "p5": -18, "p95": 11, "significance": null}
```

(to improve pregnancy, maternal or infant outcomes). A majority
of recent studies have focused on obese or overweight women
or women with/or at-risk of gestational diabetes mellitus. Few
studies have only included women with a normal pre-pregnancy
BMI(28). Given this scarcity of data, the present study makes an
important contribution to dietary counselling in healthy preg-
nant women.

In other groups of population, tailored nutrition interventions
have proved to be effective, mainly because personalisation
made the advice more acceptable to the targeted popula-
tion(31,33,43). Thus, the tailored dimension of our approach
might have increased its acceptability and hence the effective
implementation of dietary advice. The women were informed
that the advice generated using the application was specific to

their diet and would not have been proposed to another woman
with a different diet. This may have enhanced their feelings of
identification with the approach when compared with the
generic advice. Furthermore, some existing behaviour change
techniques were used to improve the adherence of women to
the intervention(44). Indeed, they were aware that each piece
of advice was generated to optimise their own nutrient adequacy
score evaluated using their declared diets and they were told
about the theoretical benefits of each type of advice (in points)
to improving their PANDiet score. This is referred to as ‘provide
information on consequences of behavior to the individual’
according to the CALO-RE taxonomy(44). Furthermore, the nine
pieces of dietary advice were not chosen during the same ses-
sion. The provision of three, 2-week spaced sessions offered

**Table 3.** Numbers of pieces of advice chosen according to the type of advice and intensity of the implementation of dietary advice in the diet, among women in the intervention arm* (n 40)
(Mean values, standard deviations and ranges)

```jsonl
{"Number of pieces of advice chosen": "Modification of amounts", "Mean": 4.4, "SD": 1.7, "Range": "0-8"}
{"Number of pieces of advice chosen": "Substitution", "Mean": 4.6, "SD": 1.7, "Range": "1-9"}
{"Number of pieces of advice chosen": "Actually implemented in the diet", "Mean": 7.8, "SD": 1.3, "Range": "5-9"}
{"Number of pieces of advice chosen": "Intensity of the implementation of advice", "Mean": 5.7, "SD": 1.4, "Range": "2.3-8.3"}
```

them an opportunity to gradually implement the advice in their diets. This is referred to as ‘set graded tasks’ in the CALO-RE taxonomy. At the end of each session, the list of advice was reviewed with the dietitian and confirmed automatically by email to each participant. A reminder was also sent 1 week later (referred to as ‘goal setting (behavior)’). The second and third sessions also provided an opportunity to review these previously set goals with the participant (referred to as ‘prompt review of behavioral goals’). At the end of dietary follow-up, the final nutrient adequacy score was sent to all participants by email (referred to as ‘provide feedback on performance’). To ensure that the reception of tailored advice was the only difference between the two arms, the booklet content was discussed during each session with women of both groups. Furthermore, women in the control arm were also aware of their scores and knew they could use them as a measure of improvements made to their diet by the generic guidelines at the end of the follow-up. However, the tailored approach naturally enabled a more intensive use of behaviour change techniques.

Furthermore, few previous interventions had employed a computer-based tailored approach to improve the diet of women during pregnancy. During a randomised controlled trial, Jackson *et al.* used a computer-based video counselling programme to provide advice on physical activity and diet to pregnant women of various BMI(25). Diet-related advice was tailored to each woman’s dietary habits and their motivation to change the behaviour targeted by each piece of advice. Both dietary habits and motivation were assessed using questionnaires generated by the computer-based programme, giving complete autonomy to the women. Within 4 weeks, the authors observed greater increases in the consumption of fruits and vegetables, fish, avocado and nuts and whole-grain products, and more marked reductions in that of solid fats and fried foods in the intervention arm *v.* the control arm(25). Their study and ours concur regarding the view that tailoring associated with behaviour change techniques could be a key determinant in improving diet quality during pregnancy. However, unlike ours, the present study only focused on the consumption of certain food groups (and not on individual nutrient intakes) and dietary counselling only concerned four components of the diet (fruits and vegetables, ‘healthy’ fats, whole grains and sugary foods). Until now, nutrient-based approaches to dietary counselling have only focused on one(45) or several nutrients(24,46–48), but mostly macronutrients. To our knowledge, even if some nutrients have been identified to be key during pregnancy, such as folate, DHA or Fe, there is no literature to define specific weights to those nutrients when setting PANDiet score parameters. Finally, the specific feature of our study and its findings was that it covered a large set of nutrients and generated tailored dietary advice using an algorithm to improve the overall nutrient adequacy during pregnancy. For this work, we chose a measure of dietary quality applied at the nutrient level, which is holistic and not specific to pregnancy, yet parameterised for pregnant women.

Overall, our tailored approach improved the nutrient adequacy of the diet of pregnant women during the study period, with particularly marked improvements among those with the lowest initial PANDiet scores. This result is of particular interest because it means that the benefits of intervention are greater in the women who need this most, which is a key characteristic of efficiency in public health nutrition. By contrast, it should be pointed out that in the intervention arm, only a few significant improvements were achieved when each probability of adequacy for nutrient intakes was considered separately. Accordingly, in the event of major deficiencies in specific nutrients deemed important for pregnancy, this approach should be associated with supplementation(49). However, when no major deficiencies are observed as in the case of our participants, our results indicate that this tailored approach could be valuable in improving the overall nutrient adequacy of the diet of pregnant women without resorting to multiple nutrient supplementation(50) which is often the case during pregnancy(14). The tailored approach would also be better than taking multiple supplements because, with a few dietary changes, it can improve overall nutritional status, avoid excessive intakes, address the problem of nutrients whose intake needs to be reduced and promotes healthier dietary practices that could be maintained after pregnancy.

Limitations
Two main limitations could be identified as affecting the present study. The first concerned the dietary assessments. Dietary data were recorded online, as is already done in France(51), which enabled participants to benefit from complete autonomy and to automate the data collection process, but it restricted the number of days that could be recorded. Using 3 days of dietary record at the end of dietary follow-up limited the possibility to detect any effects of the number of pieces of dietary advice that were actually implemented in the diet. Furthermore, pregnancy is accompanied by many specific physiological changes that affect food intakes and choices, such as nausea, acid reflux or tiredness(36), which can result in important inter-individual and intra-individual (between days within a dietary record and between both final and initial dietary records) variations in food intake. Taken together, these two limitations were expected to cause an underestimation of the true effect of the intervention and reduce the statistical power of the study.

The second limitation concerned the socio-demographic characteristics of our population which was predominantly composed of women with high levels of education, household income and socio-occupational categories and living in an urban area. The implementation of dietary advice was therefore not limited by affordability or availability concerns. Furthermore, most of the women were already aware of the importance of

good nutrition and had paid specific attention to consuming a
healthy and balanced diet before their pregnancy, as shown
by the relatively high initial PANDiet scores when compared
with previous reports in French women(34,35). Because we found
that the intervention was more efficient in women with a lower
nutrient adequacy, this limitation may also have led to an under-
estimation of the degree of effect that might be expected in a
more general population. The effect size of the intervention
nevertheless remained quantitatively important (approximately
0·5 × sd in the overall population and approximately 1 sd in those
with a lower initial score), particularly if it was attributed to just
the three sets of three pieces of advice regarding nine dietary
items. Giving the findings obtained with this specific population,
another study was performed in a more deprived area also in
Paris with vulnerable pregnant women. Results obtained for
populations whose socio-demographic characteristic differed
could be compared.

Perspectives

Given the extent of demand related to dietary counselling during
pregnancy(36,37) confirmed by the very low attrition rate in the
present study, the findings of the present study may encourage
the proposal of dietary counselling as a regular process during
antenatal care. Nevertheless, to deploy a tailored dietary
approach during pregnancy at a larger scale, time and cost
should be assessed. Furthermore, pregnant women have been
known to express their interest in benefiting from tailored dietary
advice(37), and the resulting higher compliance may be form of
the success of this intervention in improving the overall nutrient
adequacy of the diet. This lends credence to the idea that preg-
nancy is confirmed to be a teachable moment(52) in favour of
adopting healthier behaviours. Therefore, it would be interesting
to conduct a dietary intervention during pregnancy and to follow
women after delivery to assess whether the healthier dietary
behaviours that they adopted during the intervention are then
maintained.

Conclusion

When accompanying generic dietary information, tailored
dietary counselling using a computer-based algorithm was more
efficient than the generic information alone in improving
the nutrient adequacy of the diet of French women in mid-
pregnancy, particularly among women with a lower initial diet
quality.

Acknowledgements

The authors would like to thank the Notre-Dame de Bon Secours
Maternity Clinic for hosting the present study.

The present study received support in the form of a grant
from Danone Nutricia Research and Blédina. Blédina was not
involved in the design, conduct, analysis and interpretation of
the study. Danone Nutricia Research did not have a decision-
making role in the design, conduct, analysis and interpretation
of the study; however, an employee of this company, co-author
of this manuscript, who have some expertise in dietary advice

participated in the discussions about some points of the design
of the study (not on the content of the algorithm that provided
dietary advice, including for the nutrients, the food groups/
items, and the types of dietary advice that were considered).
This employee was also involved in the conduct of the study
by receiving regular information on the follow-up of the study
and giving feedbacks, but was not in contact with the partici-
pants. This employee was not involved in the analysis and the
interpretation of the results. There was no commercial interest
in the frame of the present study. The dietary advice tool that
was tested in the present study has never been the subject of
any commercial valorisation by Blédina or Danone Nutricia
Research.

C. M. B., F. M., A. L., E. O. V., E. A. and J. F. H. designed the
research and C. M. B., F. M., A. L., C. J., Y. S., H. B., J. F., R. E., E. O.
V., F. M. and J. F. H. conducted the research. S. D. and D. C. T.
provided essential material. C. M. B. performed the statistical
analysis, analysed the data and wrote the first draft of the manu-
script. All authors contributed to writing the manuscript and
offered critical comments. C. M. B. had primary responsibility
for the final content. All authors read and approved the final
manuscript.

C. M. B., F. M., C. J., Y. S., H. B., J. F., S. D., D. C.-T., E. R., E. O.
V., E. A. and J. F. H. declare no conflicts of interest. A. L. is
employed by Danone Nutricia Research.

Supplementary material

For supplementary material referred to in this article, please visit
https://doi.org/10.1017/S0007114519002617

References

1. Barker DJ (1992) Fetal and Infant Origins of Adult Diseases.
London: British Medical Journal Publishing Group.
2. Barker DJP (2003) The developmental origins of adult disease.
Eur J Epidemiol 18, 733–736.
3. Hanson M (2015) The birth and future health of DOHaD. J Dev
Orig Health Dis 6, 434–437.
4. Muhlhausler S & Ong ZY (2011) The fetal origins of obesity:
early origins of altered food intake. Endocr Metab Immune
Disord Drug Targets 11, 189–197.
5. Pasternak Y, Aviram A, Poraz I, et al. (2013) Maternal nutrition
and offspring’s adulthood NCD’s: a review. J Matern Fetal
Neonatal Med 26, 439–444.
6. Blumfield ML, Hure AJ, Macdonald-Wicks L, et al. (2012)
Systematic review and meta-analysis of energy and macronu-
trient intakes during pregnancy in developed countries. Nutr
Rev 70, 322–336.
7. Blumfield ML, Hure AJ, Macdonald-Wicks L, et al. (2013) A
systematic review and meta-analysis of micronutrient intakes
during pregnancy in developed countries. Nutr Rev 71,
118–132.
8. Goletzke J, Buyken AE, Louie JCY, et al. (2015) Dietary micro-
nutrient intake during pregnancy is a function of carbohydrate
quality. Am J Clin Nutr 102, 626–632.
9. Hauner H, Much D, Vollhardt C, et al. (2012) Effect of reducing
the n-6:n-3 long-chain PUFA ratio during pregnancy and lacta-
tion on infant adipose tissue growth within the first year of life:

an open-label randomized controlled trial. *Am J Clin Nutr* **95**,
383–394.

10. Bernard JY, Agostini MD, Forhan A, *et al.* (2013) The dietary
*n*6:*n*3 fatty acid ratio during pregnancy is inversely associated
with child neurodevelopment in the EDEN mother–child
cohort. *J Nutr* **143**, 1481–1488.

11. Caldwell KL, Pan Y, Mortensen ME, *et al.* (2013) Iodine status in
pregnant women in the National Children’s Study and in U.S.
women (15-44 years), National Health and Nutrition
Examination Survey 2005-2010. *Thyroid* **23**, 927–937.

12. Rayman MP & Bath SC (2015) The new emergence of iodine
deficiency in the UK: consequences for child neurodevelop
ment. *Ann Clin Biochem* **52**, 705–708.

13. Drouillet P, Forhan A, De Lauzon-Guillain B, *et al.* (2009)
Maternal fatty acid intake and fetal growth: evidence for
an association in overweight women. The ‘EDEN mother
child’ cohort (study of pre- and early postnatal determinants
of the child’s development and health). *Br J Nutr* **101**,
583–591.

14. Pouchieu C, Lévy R, Faure C, *et al.* (2013) Socioeconomic, life
style and dietary factors associated with dietary supplement use
during pregnancy. *PLOS ONE* **8**, e70733.

15. Kadawathagedara M, Kersuzan C, Wagner S, *et al.* (2017)
Adéquation des consommations alimentaires des femmes
enceintes de l’étude ELFE aux recommandations du
Programme national nutrition santé (Adequacy of food con
sumption by pregnant women in the ELFE study compared with
recommendations of the National Health and Nutrition
Programme). *Cah Nutr Diet* **52**, 78–88.

16. Caron P (2015) Neurocognitive outcomes of children secon
dary to mild iodine deficiency in pregnant women. *Ann*
*Endocrinol* **76**, 248–252.

17. Szwajcer EM, Hiddink GJ, Koelen MA, *et al.* (2007) Nutrition
awareness and pregnancy: implications for the life course
perspective. *Eur J Obstet Gynecol Reprod Biol* **135**, 58–64.

18. Szwajcer EM, Hiddink GJ, Koelen MA, *et al.* (2005) Nutrition
related information-seeking behaviours before and throughout
the course of pregnancy: consequences for nutrition communi
cation. *Eur J Clin Nutr* **59**, Suppl. 1, S57–S65.

19. Whitaker KM, Wilcox S, Liu J, *et al.* (2016) African American and
White women’s perceptions of weight gain, physical activity,
and nutrition during pregnancy. *Midwifery* **34**, 211–220.

20. Goodrich K, Cregger M, Wilcox S, *et al.* (2013) A qualitative
study of factors affecting pregnancy weight gain in African
American women. *Matern Child Health J* **17**, 432–440.

21. Wennberg AL, Lundqvist A, Högberg U, *et al.* (2013) Women’s
experiences of dietary advice and dietary changes during
pregnancy. *Midwifery* **29**, 1027–1034.

22. Lucas C, Charlton KE & Yeatman H (2014) Nutrition advice
during pregnancy: do women receive it and can health
professionals provide it? *Matern Child Health J* **18**, 2465–
2478.

23. Ferrari RM, Siega-Riz AM, Evenson KR, *et al.* (2013) A qualita
tive study of women’s perceptions of provider advice about diet
and physical activity during pregnancy. *Patient Educ Couns*
**91**, 372–377.

24. Dodd JM, Cramp C, Sui Z, *et al.* (2014) The effects of antenatal
dietary and lifestyle advice for women who are overweight or
obese on maternal diet and physical activity: the LIMIT rando
mised trial. *BMC Med* **12**, 161.

25. Jackson RA, Stotland NE, Caughey AB, *et al.* (2011) Improving
diet and exercise in pregnancy with Video Doctor counseling: a
randomized trial. *Patient Educ Couns* **83**, 203–209.

26. Wolff S, Legarth J, Vangsgaard K, *et al.* (2008) A randomized
trial of the effects of dietary counseling on gestational weight

gain and glucose metabolism in obese pregnant women.
*Int J Obes 2005* **32**, 495–501.

27. Muktabhant B, Lawrie TA, Lumbiganon P, *et al.* (2015) Diet or
exercise, or both, for preventing excessive weight gain in preg
nancy. *Cochrane Database Syst Rev*, issue 6, CD007145.

28. O’Brien CM, Grivell RM & Dodd JM (2016) Systematic review
of antenatal dietary and lifestyle interventions in women with
a normal body mass index. *Acta Obstet Gynecol Scand* **95**,
259–269.

29. Gresham E, Bisquera A, Byles JE, *et al.* (2014) Effects of dietary
interventions on pregnancy outcomes: a systematic review and
meta-analysis. *Matern Child Nutr* **12**, 5–23.

30. Gresham E, Byles JE, Bisquera A, *et al.* (2014) Effects of dietary
interventions on neonatal and infant outcomes: a systematic
review and meta-analysis. *Am J Clin Nutr* **100**, 1298–1321.

31. Brug J, Oenema A & Campbell M (2003) Past, present, and
future of computer-tailored nutrition education. *Am J Clin*
*Nutr* **77**, 1028S–1034S.

32. Celis-Morales C, Lara J & Mathers JC (2015) Personalising
nutritional guidance for more effective behaviour change.
*Proc Nutr Soc* **74**, 130–138.

33. Broekhuizen K, Kroeze W, van Poppel MNM, *et al.* (2012) A
systematic review of randomized controlled trials on the effec
tiveness of computer-tailored physical activity and dietary
behavior promotion programs: an update. *Ann Behav Med*
*Publ Soc Behav Med* **44**, 259–286.

34. Bianchi CM, Mariotti F, Verger EO, *et al.* (2016) Pregnancy
requires major changes in the quality of the diet for nutritional
adequacy: simulations in the French and the United States
Populations. Cardoso MA, editor. *PLOS ONE* **11**, e0149858.

35. Bianchi CM, Huneau J-F, Barbillon P, *et al.* (2018) A clear trade
off exists between the theoretical efficiency and acceptability of
dietary changes that improve nutrient adequacy during preg
nancy in French women: combined data from simulated
changes modeling and online assessment survey. *PLOS ONE*
**13**, e0194764.

36. Bianchi CM, Huneau J-F, Le Goff G, *et al.* (2016) Concerns, atti
tudes, beliefs and information seeking practices with respect to
nutrition-related issues: a qualitative study in French pregnant
women. *BMC Pregnancy Childbirth* **16**, 306.

37. Bianchi CM, Mariotti F, Reulet E, *et al.* (2017) Perception
of tailored dietary advice to improve the nutrient adequacy
of the diet by French pregnant women: a mixed methods study.

38. Hercberg S, Deheeger M & Prezio P (2002) *SU.VI.MAX Portions*
*alimentaires manuel-photos pour l’estimation des quantités*
*(SU.VI.MAX Food Portion Photo Manual for Estimating*
*Quantities)*. Paris: Polytechnica.

39. Black A (2000) Critical evaluation of energy intake using the
Goldberg cut-off for energy intake:basal metabolic rate. A prac
tical guide to its calculation, use and limitations. *Int J Obes* **24**,
1119–1130.

40. Anses (2013) Table Ciqual 2013 Composition nutritionnelle
des aliments (Ciqual Nutritional Food Composition Table
2013). https://pro.anses.fr/TableCIQUAL/index.htm (accessed
October 2014).

41. AFSSA (2001) *Apports nutritionnels conseillés pour la popula*
*tion française*, 3e éd. (*Recommended Dietary Intakes for the*
*French Population*, 3rd ed.). Paris: Editions Lavoisier.

42. INPES (2015) *Le guide nutrition de la grossesse (Pregnancy*
*Nutrition Guide)*. Paris: Institut National de Prévention et
d’Education pour la Santé.

43. Brug J, Campbell M & van Assema P (1999) The application
and impact of computer-generated personalized nutrition
education: a review of the literature. *Patient Educ Couns*
**36**, 145–156.

44. Michie S, Ashford S, Sniehotta FF, et al. (2011) A refined
taxonomy of behaviour change techniques to help
people change their physical activity and healthy eating
behaviours: the CALO-RE taxonomy. Psychol Health 26,
1479–1498.

45. Clark J, Craig L, McNeill G, et al. (2012) A novel dietary inter-
vention to optimize vitamin E intake of pregnant women to
15 mg/day. J Acad Nutr Diet 112, 297–301.

46. Khoury J, Henriksen T, Christophersen B, et al. (2005) Effect of
a cholesterol-lowering diet on maternal, cord, and neonatal lip-
ids, and pregnancy outcome: a randomized clinical trial. Am J
Obstet Gynecol 193, 1292–1301.

47. Hawkins M, Chasan-Taber L, Marcus B, et al. (2014) Impact of
an exercise intervention on physical activity during pregnancy:
the behaviors affecting baby and you study. Am J Public Health
104, e74–e81.

48. Korpi-Hyövälti E, Schwab U, Laaksonen DE, et al. (2012) Effect
of intensive counselling on the quality of dietary fats in preg-
nant women at high risk of gestational diabetes mellitus.
Br J Nutr 108, 910–917.

49. Haider BA & Bhutta ZA (2017) Multiple-micronutrient supple-
mentation for women during pregnancy. Cochrane Database
Syst Rev, issue 4, CD004905.

50. Parisi F, Laoreti A & Cetin I (2014) Multiple micronutrient needs in
pregnancy in industrialized countries. Ann Nutr Metab 65, 13–21.

51. Touvier M, Kesse-Guyot E, Méjean C, et al. (2011) Comparison
between an interactive web-based self-administered 24 h
dietary record and an interview by a dietitian for large-scale epi-
demiological studies. Br J Nutr 105, 1055–1064.

52. Phelan S (2010) Pregnancy: a “teachable moment” for weight
control and obesity prevention. Am J Obstet Gynecol 202,
135.e1–135.e8.

