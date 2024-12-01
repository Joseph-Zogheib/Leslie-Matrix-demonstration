eggzeroone = 3000
eggonetwo = 3000
eggtwothree = 3000
nymphthreefour = 4000
nymphfourfive = 4000
subimagofivesix = 1000
imagosixseven = 10000

def calculate():
    global firstrow, secondrow, thirdrow, fourthrow, fifthrow, sixthrow, seventhrow, eggzeroone, eggonetwo, eggtwothree, nymphthreefour, nymphfourfive, subimagofivesix, imagosixseven
    firstrow = 100 * imagosixseven
    secondrow = 0.5 * eggzeroone
    thirdrow = 0.5 * eggonetwo
    fourthrow = 0.5 * eggtwothree
    fifthrow = 0.25 * nymphthreefour
    sixthrow = 0.25 * nymphfourfive
    seventhrow = 0.99 * subimagofivesix

    total_eggs = firstrow + secondrow + thirdrow
    total_nymphs = fourthrow + fifthrow
    
    print(f"After day {i+1}:")
    print(f"    TotalEgg: {total_eggs:.2f}")
    print(f"  Egg0-1: {firstrow:.2f}")
    print(f"  Egg1-2: {secondrow:.2f}")
    print(f"  Egg2-3: {thirdrow:.2f}")
    print(f"    TotalNymph: {total_nymphs:.2f}")
    print(f"  Nymph3-4: {fourthrow:.2f}")
    print(f"  Nymph4-5: {fifthrow:.2f}")
    print(f"  Subimago: {sixthrow:.2f}")
    print(f"  Imago: {seventhrow:.2f}")
    
    eggzeroone = firstrow
    eggonetwo = secondrow
    eggtwothree = thirdrow
    nymphthreefour = fourthrow
    nymphfourfive = fifthrow
    subimagofivesix = sixthrow
    imagosixseven = seventhrow


total_eggss = eggzeroone + eggonetwo + eggtwothree
total_nymphss = nymphthreefour + nymphfourfive
print("Initially:")
print(f"    TotalEgg: " + str(total_eggss))
print(f"  Egg0-1: " + str(eggzeroone))
print(f"  Egg1-2: " + str(eggonetwo))
print(f"  Egg2-3: " + str(eggtwothree))
print(f"    TotalNymph: " + str(total_nymphss))
print(f"  Nymph3-4: " + str(nymphthreefour))
print(f"  Nymph4-5: " + str(nymphfourfive))
print(f"  Subimago: " + str(subimagofivesix))
print(f"  Imago: " + str(imagosixseven))

for i in range(10):
    calculate()
