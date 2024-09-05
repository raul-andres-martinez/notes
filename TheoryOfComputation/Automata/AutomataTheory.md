# Formal Definition
## Alphabet
An alphabet is a finite set of elements called *symbols*. It is usually represented by Greek letters.
Examples:

Σ = {0, 1}
Σ1 = {a, b, ..., z}
Γ = {#, a1, bd} - This is valid, but not recommended.

Given a set Σ, a string (over Σ) is a sequence x1, x2, ..., xn, where xi ∈ Σ for each 1 ≤ i ≤ n, which is a finite sequence of symbols. Strings are usually represented by lowercase Greek letters.

## Strings
The length of a string ω is the number of positions in the sequence and is denoted as |ω|.
Example:

ω = 011011 is a string over Σ = {0, 1} and |ω| = 6.

If x ∈ Σ and ω is a string over Σ, we denote by |ω|x the number of times the symbol x appears in ω.
Example:

|ω|1 = 4

## Concatenation
The concatenation of a string α = α1 α2 ... αn with a string β = β1 β2 ... βn is αβ = α1 α2 ... αn β1 β2 ... βn.

We denote by α^k the concatenation of α with itself k times.

Examples:

α = aba and β = caa
αβ = abacaa
βα = caaaba
α^3 = abaabaaba
α^2β^3 = abaabacaacaacaa 

## Important strings
The reverse of a string ω = ω1 ω2 ... ωwn is w^R = wn wn-1 ... w1

A empty string, usually denoted by ε, is a string of length 0. For any string ω, ωε = εω = ω.

## Substrings
A string β is a substring of another string ω if there exist strings α and δ such that ω = αβδ.
Example:

β = 01 is a substring of ω = 011011 because ω = αβδ
with α = ε (empty) and δ = 1011 (or α = 011 and δ = 1).

## Power of an Alphabet
Given an alphabet Σ, we denote by Σ^k the set of all strings of length k over Σ.

If Σ = {0, 1}, then:

Σ^0 = {ε}
Σ^1 = {0, 1}
Σ^2 = {00, 01, 10, 11}
Σ^3 = {000, 001, 010, 011, 100, 101, 110, 111}

The size of Σ^k is given by |Σ^k| = |Σ|^k.