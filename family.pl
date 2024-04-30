parent(john, sam).
parent(amy, sam).
parent(sam, rachel).
parent(sam, chandler).
parent(sam, joey).

wife(amy, john).
wife(rachel, ross).
wife(monica, chandler).
wife(mona, sam).

female(amy).
female(rachel).
female(monica).

male(john).
male(sam).
male(ross).

mother(X, Y):- parent(X, Y), female(X).
husband(X, Y):- wife(Y, X).
sibling(X,Y):- parent(Z, X), parent(Z,Y).
grandfather(X,Y):- parent(X, Z), parent(Z, Y), male(X).
