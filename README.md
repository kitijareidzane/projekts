# Konkrētas prasības meklēšana vairākos PDF failos un to izvadīšana.
## Programmatūras uzdevums:
Lietotājs ievada konkrētu vārdu vai vārdu savienojumu, kuru vēlas atrast vairākos PDF failos (piem. CV), programma to meklē visos failos un izvada rindas numuru, lappaspuses numuru, rindu un faila nosaukumu, kur atrodas konkrēts vārds. Ja tāds vārds vai vārdu savienojums nav minēts nevienā failā, tad programma izvada "Vārds 'Jūsu vards' netika atrasts".
## Izmantotas bibliotēkas:
programmatūras izstrādes procesā tika izmantota tikai viena bibliotēka. PyMuPDF bibliotēka ļauj darboties ar PDF failiem Python valodā, kā arī tā it ļoti parocīga un viegla izmantošanā. Pirmkārt, PyMuPDF ir viegli izmantot, jo tā piedāvā intuitīvu interfeisu. Otrkārt, šī bibliotēka ļauj dabūt tekstu no PDF failiem, kas ir nepieciešam šī projekta ietvaros, lai atrastu pieprasitu informāciju. Treškārt, šī bibliotēka ir platformu neatkarīga un darbojas uz dažādām operētājsistēmām.
## Programmatūras apraksts:
Lietotājs tiek aicināts ievadīt mapes ceļu, kurā jāmeklē PDF faili.
Lietotājs ievada meklējamo vārdu.
Pirms sākt meklēšanu, skripts pārbauda, vai norādītais mapes ceļš ir derīgs un vai šī ceļa beigās ir esoša direktorija ar PDF failiem.
Ja mapes ceļš nav derīgs vai nav direktorija, tiek izvadīts kļūdas paziņojums, un programma beidz izpildi.
Skripts iterē cauri visiem failiem norādītajā mapē.
Ja fails ir ar paplašinājumu .pdf, tas tiek atvērts izmantojot PyMuPDF (fitz.open).
Ja PDF fails ir atvērts veiksmīgi, skripts iterē cauri visām lapām.
No katras lapas izgūst tekstu, izmantojot page.get_text().
Izmantojot regulārās izteiksmes, skripts meklē norādīto vārdu katrā lapas teksta rindā.
Ja vārds tiek atrasts, izvada informāciju par atradumu, iekļaujot faila nosaukumu, lapas numuru un rindu, kur atrasts vārds.
Ja vārds nav atrasts konkrētajā failā, izvada attiecīgu ziņojumu.
Ja vārds ir atrasts vismaz vienā failā, izvada informāciju par šiem atradumiem.
Ja vārds nav atrasts nevienā failā, izvada paziņojumu par to.
Skriptā norādīts piemēra izmantošanas gadījums, kur tiek meklēts vārds mapē ar PDF failiem.
Programma ir lietderīga risinājums, ja ir nepieciešams ātri un efektīvi meklēt noteiktu vārdu vairākos PDF failos.
