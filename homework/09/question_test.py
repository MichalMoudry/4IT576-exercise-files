#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#O:/p4_INP/question_test.py
"""
Definuje jednoduchý test založený na pokládání sady otázek,
pro něž se vybírají správné odpovědi z nabízené sady.
"""
import dbg; dbg.start_mod(1, __name__)
###########################################################################q

from collections import namedtuple

import re



###########################################################################q

A = namedtuple('Answer', ('correct answer'))
A.__doc__ = """\
Jedna z nabízených odpovědí, přičemž 
- v atributu "correct" je logická hodnota, zda je daná odpověď správná,
- v atributu "answer" je text dané odpovědi.
"""


Q = namedtuple('Question', 'text, answers')
Q.__doc__ = """
Testová otázka se sadou nabízených odpovědí, přičemž
- v atributu 'text' je text příslušné testové otázky,
- v atributu "answers" je n-tice odpovědí typu Answer.
"""

def qr(self):
    """Systémový podpis testové otázky: text otázky následovaný
    texty nabízených odpovědí uvozených vždy indexem dané odpovědi.
    """
    ta = [f'{index}.\n{answer.answer}'
         for index, answer in enumerate(self.answers, start=1)]
    result = '\n\n'.join(['\n'+self.text] + ta) + '\n'
    return result
Q.__repr__ = qr;    del qr



###########################################################################q

def ask(question:Q) -> list[int]:
    """Položí otázku a předzpracuje odpověď;
    jako odpověď vrátí seznam indexů otázek považovaných za správné.
    """
    # dbg.prSE(0, 1, 'ask')
    num     = len(question.answers) # Počet nabízených odpovědí
    ptrnsrc = f'0|[' + '12345689'[:num] + ']+'
    pattern = re.compile(ptrnsrc)   # Definice akceptovatelné odpovědi
    answer  = input(f'{question}\nZadejte čísla všech správných odpovědí'
                     '\nNení-li žádná odpověď správná, zadejte nulu: ')
    while True:
        answer = answer.strip()
        if pattern.match(answer):   break
        answer = input("Smíte zadat pouze znak '0' anebo čísla odpovědí,\n"
                       "které považujete za správné.\n"
                       "Zkuste odpovědět znovu: ")
    result = [] if answer=='0' else [ord(c)-ord('1') for c in answer]
    # dbg.prSE(0, 0, 'ask', result)
    return result


def test_q(question:Q) -> float:
    """Položí testovací otázku spolu s nabídkou odpovědí
    a vrátí procentní úspěšnost.
    """
    num     = len(question.answers) # Počet nabízených odpovědí
    answer  = ask(question)
    # Seznam indexů správných odpovědí
    correct = [index for index, answer in enumerate(question.answers)
                      if answer.correct]
    # dbg.prIN(0, f'{answer=}, {correct=}')
    right = len(question.answers) - len(answer)
    for i in answer:
        if i in correct:
            right += 1
            correct.remove(i)
        else:
            right -= 1
    right -= 2 * len(correct)
    return right / num


def test_seq(seq:tuple[Q]):
    """Cvičně položí všechny otázky z n-tice collections.
    """
    sum = 0
    for q in seq:
        result = test_q(q)
        sum   += result
        print(f'\n{30*"-"}\nHodnocení odpovědi: {result:.2} bodů'
              f'\n{60*"="}')
    print(f'\n{60*"#"}\nSouhrnné hodnocení: {sum:.2} bodů\n{60*"#"}')



###########################################################################q
#Testy

questions = (
    Q('První otázka',
      (A(1, 'ANO - První'),
       A(1, 'ANO - Druhý'),
       A(0, 'NE  - Třetí'),
    )),
    Q('Druhá otázka',
      (A(0, 'NE  - První'),
       A(1, 'ANO - Druhý'),
       A(0, 'NE  - Třetí'),
    )),
)



###########################################################################q

__all__ = ('A', 'Q', 'test_seq')


###########################################################################q
dbg.stop_mod(1, __name__)
