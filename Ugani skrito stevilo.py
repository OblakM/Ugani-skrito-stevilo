
secret = 7

guess = int(raw_input("Ugani skrito stevilo: "))

if guess == secret:
    print "Bravo, uganil si skrito stevilo. To stevilo je " + str(secret) + "."

if guess != secret:
    print "Napacen odgovor, poskusi ponovno."