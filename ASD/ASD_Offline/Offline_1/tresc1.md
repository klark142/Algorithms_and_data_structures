## Zadanie offline 1.

Cesarzowa Bajtocji zgubiła w napisie s swój ulubiony palindrom. Cesarzowa nikomu nie mówiła jaki
jest jej ulubiony palindrom i wiadomo jedynie, że jest bardzo długi oraz składa się z nieparzystej
liczby liter alfabetu łacińskiego. Postanowiono odnaleźć zaginiony palindrom cesarzowej. W tym
celu należy zaimplementować funkcję:
`def ceasar( s )`, 
która na wejściu otrzymuje słowo s (składające się wyłącznie z małych liter alfabetu łacińskiego)
i zwraca długość najdłuższego spójnego podsłowa, które jest palindromem i którego długość
jest nieparzysta. Użyty algorytm powinien być możliwie jak najszybszy. Proszę uzasadnić jego
poprawność i oszacować złożoność obliczeniową.

**Przykład.** 
Dla słowa:
_akontnoknonabcddcba_
wynikiem jest 7 (kontnok; proszę zwrócić uwagę, że abcddcba jest dłuższym palindromem, ale jest
długości parzystej więc na pewno nie jest zagubionym palindromem cesarzowej).