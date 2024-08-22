# webScrapingAlteredOfficialFAQ
Ciao a tutti!
Ecco a voi il mio primo script di web scraping creato per un progetto interno alla community italiana di Altered TCG.
E' ancora la prima versione, quindi siate clementi con me :D

Questo repository contiene uno script Python che esegue il web scraping di un sito di supporto, estraendo automaticamente le domande frequenti (FAQ) e le relative risposte. Lo script effettua richieste HTTP per ottenere il contenuto delle pagine, individua le sezioni rilevanti utilizzando pattern di espressioni regolari, e formatta le informazioni in un file leggibile.

## Caratteristiche principali:
- **Richiesta e parsing di pagine web**: Recupera il contenuto HTML delle pagine target.
- **Identificazione e pulizia di URL**: Estrae e pulisce gli URL specifici dalle pagine di supporto.
- **Formattazione delle domande**: Converte i titoli delle domande in un formato leggibile.
- **Estrazione delle risposte**: Raccoglie le risposte associate e le salva in un file di output.
