import hashmap

# create a mapping of animal to genus (not necessarily accurate)
animals = hashmap.new()
hashmap.set(animals, 'Dog', 'Canine')
hashmap.set(animals, 'Cat', 'Feline')
hashmap.set(animals, 'Human', 'Sapien')
hashmap.set(animals, 'Wolf', 'Canine')
hashmap.set(animals, 'Jellyfish', 'Scyphozoa')
hashmap.set(animals, 'Octopus', 'Octopus')

# create a basic set of animals and some sounds for them
sounds = hashmap.new()
hashmap.set(sounds, 'Canine', 'woof')
hashmap.set(sounds, 'Sapien', 'hello world')
hashmap.set(sounds, 'Scyphozoa', '...')

# add some more sounds
hashmap.set(sounds, 'Feline', 'meow')
hashmap.set(sounds, 'Octopus', '...')


# print out some sounds
print '-' * 10
print "Wolves make %s sounds" % hashmap.get(sounds, 'Canine')
print "Humans make %s sounds" % hashmap.get(sounds, 'Sapien')

# print some genii
print '-' * 10
print "Dog is of genus %s" % hashmap.get(animals, 'Dog')
print "Octopus is of genus %s" % hashmap.get(animals, 'Octopus')

# do it by using the animals then sounds dict
print '-' * 10
print "Jellyfish makes %s sounds" % hashmap.get(sounds, hashmap.get(animals, 'Octopus'))
print "Cats make %s sounds" % hashmap.get(sounds, hashmap.get(animals, 'Cat'))

# print every animal genus
print '-' * 10
hashmap.list(animals)

# print every sound by genus
print '-' * 10
hashmap.list(sounds)

print '-' * 10
animals = hashmap.get(animals, 'Unicorn')

if not animals:
  print "Sorry, no Unicorns."

# default values using ||= with the nil result
sounds = hashmap.get(sounds, 'Sound of rainbows', 'Imaginary')
print "The sound for the genus 'Equine, Magical' is: %s" % sounds