# German POS

A very simple German part-of-speech (POS) tagger trained with [TIGER-corpus](https://www.ims.uni-stuttgart.de/forschung/ressourcen/korpora/tiger.html).

## Usage

The POS tagger needs tokenized text as input, i.e., a list of words.

```python
import load_tagger

text = "Was ich von der Geschichte des armen Werther nur habe auffinden können, habe ich mit Fleiß gesammelt und lege es euch hier vor, und weiß, daß ihr mir's danken werdet. Ihr könnt seinem Geist und seinem Charakter eure Bewunderung und Liebe, seinem Schicksale eure Tränen nicht versagen. Und du gute Seele, die du eben den Drang fühlst wie er, schöpfe Trost aus seinem Leiden, und laß das Büchlein deinen Freund sein, wenn du aus Geschick oder eigener Schuld keinen näheren finden kannst." 
token_text = nltk.word_tokenize(text)
load_tagger.tag_text(token_text)

[('Was', 'PWS'), ('ich', 'PPER'), ('von', 'APPR'), ('der', 'ART'), ('Geschichte', 'NN'), ('des', 'ART'), ('armen', 'ADJA'), ('Werther', 'NN'), ('nur', 'ADV'), ('habe', 'VAFIN'), ('auffinden', 'PIAT'), ('können', 'VMINF'), (',', '$,'), ('habe', 'VAFIN'), ('ich', 'PPER'), ('mit', 'APPR'), ('Fleiß', 'NN'), ('gesammelt', 'VVPP'), ('und', 'KON'), ('lege', 'VVFIN'), ('es', 'PPER'), ('euch', 'PPER'), ('hier', 'ADV'), ('vor', 'APPR'), (',', '$,'), ('und', 'KON'), ('weiß', 'VVFIN'), (',', '$,'), ('daß', 'KOUS'), ('ihr', 'PPER'), ('mir', 'PPER'), ("'s", 'PPER'), ('danken', 'VVINF'), ('werdet', 'VAFIN'), ('.', '$.'), ('Ihr', 'PPOSAT'), ('könnt', 'ADJD'), ('seinem', 'PPOSAT'), ('Geist', 'NN'), ('und', 'KON'), ('seinem', 'PPOSAT'), ('Charakter', 'NN'), ('eure', 'VVPP'), ('Bewunderung', 'NN'), ('und', 'KON'), ('Liebe', 'NN'), (',', '$,'), ('seinem', 'PPOSAT'), ('Schicksale', 'NN'), ('eure', 'VVPP'), ('Tränen', 'NN'), ('nicht', 'PTKNEG'), ('versagen', 'VVINF'), ('.', '$.'), ('Und', 'KON'), ('du', 'PPER'), ('gute', 'ADJA'), ('Seele', 'NN'), (',', '$,'), ('die', 'PRELS'), ('du', 'PPER'), ('eben', 'ADV'), ('den', 'ART'), ('Drang', 'NN'), ('fühlst', 'VVFIN'), ('wie', 'KOKOM'), ('er', 'PPER'), (',', '$,'), ('schöpfe', 'VVFIN'), ('Trost', 'NE'), ('aus', 'PTKVZ'), ('seinem', 'PPOSAT'), ('Leiden', 'NN'), (',', '$,'), ('und', 'KON'), ('laß', 'ADJD'), ('das', 'ART'), ('Büchlein', 'NN'), ('deinen', 'ART'), ('Freund', 'NN'), ('sein', 'VAINF'), (',', '$,'), ('wenn', 'KOUS'), ('du', 'PPER'), ('aus', 'APPR'), ('Geschick', 'NN'), ('oder', 'KON'), ('eigener', 'ADJA'), ('Schuld', 'NN'), ('keinen', 'PIAT'), ('näheren', 'ADJA'), ('finden', 'VVINF'), ('kannst', 'VMFIN'), ('.', '$.')]
```
