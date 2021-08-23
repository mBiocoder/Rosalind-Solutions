#!/usr/bin/env python

import sys


class Clump_finding:

    # k: länge kmer L: länge interval t: menge der Kmere
    def __init__(self, params):

        # argv muss 9 elementig sein sonst sind zu viele ode zu wenige Paramenter angegeben
        if len(params) != 9:
            print('Wrong input')
            return

        self.genom = ''
        self.k = 0
        self.L = 0
        self.t = 0
        self.best_clump = set()
        self.kmers = {}

        # Sorgt dafür dass die Reihenfogle in der die Flags übergeben werden egal ist

        for flag in params:
            if flag == '-k':
                self.k = int(params[params.index(flag) + 1])
            elif flag == '-L':
                self.L = int(params[params.index(flag) + 1])
            elif flag == '-t':
                self.t = int(params[params.index(flag) + 1])
            elif flag == '-g':
                self.genom = ''.join(open(params[params.index(flag) + 1], 'r').readlines()).strip()

    # findet die patterns in clumps

    def find_Clumps(self):
        self.initalize_first_kmers()

        for i in range(1, len(self.genom) - self.L):
            self.update_kmers(i)

        for seq in self.best_clump:
            print(seq, end=' ')

    # Erstellt ein Dictionary mit allen patterns der Länge k und speichert diese mit ihrer Häufigkeit in kmers (dict)
    # Wird nur einmal aufgerufen und sammellt alle patterns im ersten Interval L

    def initalize_first_kmers(self):

        for i in range(0, self.L - self.k + 1):
            kmer = self.genom[i:i + self.k]
            if kmer in self.kmers.keys():
                self.kmers[kmer] = self.kmers[kmer] + 1
            else:
                self.kmers.update({kmer: 1})

        for k, v in self.kmers.items():
            if v >= self.t:
                self.best_clump.add(k)

    # updated das kmers dict indem der leserahmen der größe L immer um 1 verschoben wird
    # so entsteht ein neues kmer das hinzugefügt wird
    # und ein altes wird entfernt

    def update_kmers(self, start):

        # das kmer das links nicht mehr existiert da der Leserahmen verschoben wurde
        discarded_kmer = self.genom[start - 1:start + self.k - 1]

        # wenn es öfter als 1 mal vorkommt wird die Anzahl um 1 reduziert, sonst komplett gelöscht
        if self.kmers[discarded_kmer] > 1:
            self.kmers[discarded_kmer] = self.kmers[discarded_kmer] - 1
        else:
            self.kmers.pop(discarded_kmer)

        # gleiches vorgehen für das neue kmer

        new_kmer_end = self.genom[start + self.L - self.k: start + self.L]

        if new_kmer_end in self.kmers.keys():
            self.kmers[new_kmer_end] = self.kmers[new_kmer_end] + 1
        else:
            self.kmers.update({new_kmer_end: 1})

        # alle kmere die häufiger als k mal vorkommen in die Ergebnisliste hinzufügen

        for k, v in self.kmers.items():
            if v >= self.t:
                self.best_clump.add(k)


test = Clump_finding(sys.argv)
test.find_Clumps()