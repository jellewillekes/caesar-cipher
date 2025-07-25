# Substitution cipher solver

A substitution cipher is a method for encrypting text which works by replacing units of plaintext with units of 
ciphertext by using a fixed system. A well-known type of substitution cipher is the Caesar cipher, which rotates the 
cipher alphabet according to a fixed index:

![ROT13.png](ROT13.png)

In this exercise, you will implement a solver for a substitution cypher,
and make it available through a REST(ish) API. 

The exercise is split into several steps:

## 1. Echo endpoint

This is a basic endpoint that echos the original message 

    POST /api/solve/echo
    {'ciphertext': 'URYYB JBEYQ!'}

This endpoint should return a JSON response that looks like this:

    {
        'ciphertext' : 'URYYB JBEYQ!',
        'plaintext' : 'URYYB JBEYQ!'
    }

## 2. English language solver

This endpoint will crack the ciphertext and returns the plaintext for all english plaintexts.

    POST /api/solve/en
    {'ciphertext': 'URYYB JBEYQ!'}
    
This endpoint should return a JSON response that looks like this:

    [{
        'ciphertext' : 'URYYB JBEYQ!',
        'plaintext' : 'HELLO WORLD!'
    }]
    
## 3. Generic language solver

For the final part of this assignment, you will implement an endpoint that does not require the user to 
specify the language of the plaintext. 

    POST /api/solve/
    {'ciphertext': 'UNYYB JRERYQ!'}
    
This endpoint should return a JSON response that looks like this:

    [{
        'ciphertext' : 'UNYYB JRERYQ!',
        'plaintext' : 'HALLO WERELD!'
    }]
    
It should be possible to easily add new languages.