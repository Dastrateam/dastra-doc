# Glossary

One row per concept, in the four documentation languages. Each cell holds the term to use, then, after `≠`,
the variants to replace. `scripts/lint_doc.py` reads the variants from this table: keep the format
(`term ≠ variant, variant`), one table per section, the language columns named `fr`, `en`, `de`, `nl`.

How the variants are matched: a variant with a capital letter (`DPIA`, `RoPA`, `Zustimmung`) is case-sensitive,
a lowercase variant is not;
a plural ending is accepted (`workspace` also catches `workspaces`); code, links, URLs and HTML are ignored.

Two rules decide which term wins:

1. **A UI label is quoted exactly as the app shows it in the page's language**, even when it contradicts this
   table. The app is the source of truth for what is on screen (`Dastra.WebApp/src/assets/lang/modules/*/<lang>.json`).
2. **In running text, this table wins.** When the app itself is inconsistent, the table follows the app's main
   label, or the official GDPR wording in that language when the app has none. App labels that look wrong are
   listed at the end of this file, to fix in the app (Localazy), not in the documentation.

For German, [`glossary-de.md`](glossary-de.md) gives the customer's French to German terms for the concepts
this table does not cover.

## Privacy and GDPR

| Concept | fr | en | de | nl | Note |
| --- | --- | --- | --- | --- | --- |
| The regulation | RGPD ≠ GDPR | GDPR ≠ RGPD | DSGVO ≠ GDPR, RGPD | AVG ≠ GDPR, RGPD | Use the regulation's name in the page language. |
| Data protection officer | délégué à la protection des données (DPO) ≠ DPD | data protection officer (DPO) | Datenschutzbeauftragter (DSB) ≠ DPO | functionaris voor gegevensbescherming (FG) ≠ DPO | Spell out on first mention, then use the abbreviation. |
| Impact assessment | PIA ≠ AIPD, DPIA | DPIA ≠ PIA | DSFA ≠ DPIA | DPIA ≠ GEB | French uses PIA, masculine (« un PIA »), as the app does. A module introduction may name the legal term once: « analyse d'impact relative à la protection des données (AIPD) ». In English, PIA only names the CNIL PIA tool. |
| Record of processing activities | registre des traitements ≠ registre des activités de traitement | record of processing activities (ROPA) ≠ RoPA, register of processing, processing register, processing record, processing activity record | Verarbeitungsverzeichnis | verwerkingsregister ≠ register voor gegevensverwerking | The French legal wording may appear when quoting Article 30. ROPA is the English menu label. |
| One entry of the record | traitement | processing activity ≠ processings | Verarbeitungstätigkeit | verwerkingsactiviteit | In English, "data processing" is the UI label ("Create data processing"); in running text, write "processing activity". "processing" is uncountable: never "a processing" or "processings". |
| Controller | responsable du traitement | controller | Verantwortlicher | verwerkingsverantwoordelijke | |
| Processor | sous-traitant | processor ≠ subcontractor, sub-contractor | Auftragsverarbeiter ≠ Subunternehmer | verwerker ≠ subcontractant | A sub-processor (sous-traitant ultérieur, Unterauftragsverarbeiter, subverwerker) is a different role: keep it. |
| Data subject | personne concernée | data subject ≠ concerned person, concerned people | betroffene Person | betrokkene | |
| Personal data | données personnelles | personal data ≠ personal datas, PII | personenbezogene Daten | persoonsgegevens | "données à caractère personnel" is fine when quoting the law. |
| Personal data breach | violation de données ≠ fuite de données | data breach ≠ data leak | Datenschutzvorfall ≠ Datenleck, Datenschutzverletzung | datalek | The module is named "Incidents" (Vorfälle, Incidenten) in the app menus: quote it as a label. |
| Data subject request | demande d'exercice de droits ≠ DSR | data subject request | Betroffenenanfrage | verzoek van een betrokkene | In English, DSR is fine after the first mention. |
| Lawful basis | base légale ≠ base juridique | lawful basis ≠ legal ground | Rechtsgrundlage | wettelijke basis | Label of the purpose form in each language. |
| Purpose | finalité | purpose | Zweck | doeleinde | German: Verarbeitungszweck for the purpose of a processing activity. |
| Recipient | destinataire | recipient | Empfänger | ontvanger | |
| Consent | consentement | consent | Einwilligung ≠ Zustimmung | toestemming | |
| Transfer outside the EU | transfert hors UE | transfer outside the EU | Drittlandübermittlung | doorgifte buiten de EU | |
| Retention period | durée de conservation | retention period | Speicherdauer | bewaartermijn | |
| Supervisory authority | autorité de contrôle | supervisory authority ≠ control authority | Aufsichtsbehörde | toezichthoudende autoriteit | Name the authority when it matters (CNIL, ICO, BfDI, Autoriteit Persoonsgegevens). |
| Cookie banner | bannière de cookies ≠ bandeau | cookie banner | Cookie-Banner | cookiebanner | |
| AI Act | AI Act | AI Act | KI-Verordnung | AI-verordening | |

## Dastra product

| Concept | fr | en | de | nl | Note |
| --- | --- | --- | --- | --- | --- |
| Product name | Dastra ≠ DASTRA | Dastra ≠ DASTRA | Dastra ≠ DASTRA | Dastra ≠ DASTRA | Never in capitals, never lowercase in running text. |
| Workspace | espace de travail ≠ workspace | workspace | Mandant ≠ Workspace, Arbeitsbereich | werkruimte ≠ workspace | German follows the app label. |
| Organization (the customer account) | organisation ≠ tenant | organization ≠ tenant | Organisation ≠ Tenant | organisatie ≠ tenant | "Tenant" is internal vocabulary: write organization, or workspace when that is what is meant. |
| Organizational unit | unité organisationnelle | organizational unit ≠ organisational unit | Organisationseinheit | organisatorische eenheid | An entity (entité, Entität, entiteit) is one type of organizational unit, not a synonym. |
| Stakeholder | acteur | stakeholder ≠ actor | Stakeholder | actor ≠ acteur | Menu label in each language. A project stakeholder (partie prenante) is an Interessengruppe in German. In Dutch, a person involved in a processing activity or an AI system (partie prenante) is a stakeholder, and the people who sign a contract are ondertekenaars. |
| Asset | actif | asset | Asset | activum | Dutch menu label: Activa. |
| Dataset | jeu de données | dataset | Datensatz | dataset | Menu labels: Datenkategorien (de), Gegevenssets (nl): quote them as labels. Datenkategorie in running text is a data category (catégorie de données), not a dataset. |
| Data catalog | catalogue de données | data catalog | Datenkatalog | gegevenscatalogus | |
| Data glossary | glossaire de données | data glossary | Datenglossar ≠ Daten-Glossar | verklarende woordenlijst voor gegevens | German menu label « Datensätze » is questioned at the end of this file: quote it only as a label. Dutch follows the menu label. |
| Security measure | mesure de sécurité | security measure | Sicherheitsmaßnahme | veiligheidsmaatregel | |
| Questionnaire | questionnaire | questionnaire | Fragebogen | vragenlijst | |
| Risk management | gestion des risques | risk management | Risikomanagement | risicobeheer | |
| Task | tâche | task | Aufgabe | taak | |
| User | utilisateur | user | Nutzer ≠ Benutzer | gebruiker | Quote « Benutzer » only where it is the on-screen label. |
| Owner | propriétaire | owner | Inhaber ≠ Eigentümer | eigenaar | |
| Privacy notice | politique de confidentialité | privacy notice | Datenschutzinformation | privacyverklaring | |
| Regular review | revue régulière | regular review | regelmäßige Überprüfung | terugkerende beoordeling | |
| Custom field | champ personnalisé | custom field | benutzerdefiniertes Feld | aangepast veld | |
| Collection form | formulaire de collecte | form | Formular zur Datenerfassung | verzamelformulier | |
| File manager | gestionnaire de fichiers | file manager | Dateimanager | bestandsbeheer | |
| Dashboard | tableau de bord ≠ dashboard | dashboard | Dashboard | dashboard | |
| Contracts and policies | contrats et politiques | contracts and policies | Verträge und Richtlinien | contracten en beleidslijnen | |
| AI system | système d'IA ≠ système IA | AI system | KI-System ≠ AI-System | AI-systeem | |
| AI agent | agent IA | AI agent | KI-Agent | AI-agent | |
| Trust Center | Trust Center | Trust Center | Trust Center | vertrouwenscentrum | Dutch follows the app label. |

## Technical terms

| Concept | fr | en | de | nl | Note |
| --- | --- | --- | --- | --- | --- |
| API key | clé d'API ≠ clé API | API key | API-Schlüssel ≠ API-Key, API Schlüssel | API-sleutel ≠ API key | |
| Email | e-mail ≠ email, courriel | email ≠ e-mail | E-Mail ≠ Email | e-mail ≠ email | French: « un e-mail », « une adresse e-mail ». |
| Upload | importer ≠ uploader, upload | upload | hochladen | uploaden | In French, « télécharger » means download only. |
| Sign in | se connecter ≠ se logger | sign in | anmelden ≠ einloggen | inloggen | |
| Single sign-on | authentification unique (SSO) | single sign-on (SSO) | Single Sign-On (SSO) | single sign-on (SSO) | Spell out on first mention. |
| Webhook | webhook | webhook | Webhook | webhook | |

## Dutch app vocabulary

Dutch terms the app uses since its Dutch review (November 2026). The documentation uses the same words.

| Concept | nl | Note |
| --- | --- | --- |
| Compliance framework | kader | Menu: Conformiteit > Bibliotheek > Kaders. Keep a framework's own name as published (NIST Cybersecurity Framework). |
| Scope of a compliance project | perimeter | App label "Perimeter". |
| Template | sjabloon | |
| Redaction of a document | weglakken | |
| Contract signer | ondertekenaar | |
| AI governance menu | AI-governance | Menu label; the law itself is the AI-verordening. |
| History tab | Activiteit | "Activiteitengeschiedenis" where the app shows the full label. |

## App labels that look wrong

Quote these as they are when they are on screen, and list them in the "app side" part of the report so they get
fixed in the app. Do not use them in running text.

| Language | Label in the app | Problem |
| --- | --- | --- |
| en | "Subcontractors" (AI analysis criteria) | French calque: the GDPR term is "processors". |
| en | "Webhooks" for the vendors settings entry | The French label of the same key is « Sous-traitants ». |
| de | "Datensätze" for the data glossary | The same word is used for datasets. |
| fr | « email » and « e-mail » both used | The documentation uses « e-mail ». |
