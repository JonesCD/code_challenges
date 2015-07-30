"""
Implement a hashmap (with amortized constant time look-ups) in the 
language of your choice without using a hashmap primitive. Please 
include an executable testing framework for your data structure.
"""

"""
Disclosure: the basic structure of the hashmap below follows from what 
I learned going through Learn Python the Hard Way. I have replaced 
Python's built-in hash() function with my own code.
"""

# initialize a map with an arbitrary, but defined (512 in this example), number of buckets
def new(num_buckets = 512):
	hmap = []
	for i in range(0, num_buckets):
		hmap.append([])
	return hmap
	
# given a key, create a number and then convert to an index for the hmap's buckets
# replace hash() with novel hash code in this section
def hash_key(hmap, key):
	# create new local variables for counter and for sum
	n = 0
	tot = 0
	while n < len(key):
		# convert key to numbers using ordinal function
		# each unique key will create a 'likely unique'
		# sum, which is then binned by size of total Map
		tot += ord(key[n])
		n += 1
	return tot % len(hmap)
	# return hash(key) % len(hmap)
	
# given a key, find the bucket where it would go
def get_bucket(hmap, key):
	bucket_id = hash_key(hmap, key)
	return hmap[bucket_id]
	
# return the index, key, and value of a slot found in a bucket
# return -1, key, and default (None if not set) when not found
def get_slot(hmap, key, default = None):
	bucket = get_bucket(hmap, key)
	
	for i, kv in enumerate(bucket):
		k, v = kv
		if key == k:
			return i, k, v
			
	return -1, key, default
	
# get the value in a bucket for a given key, (or default)
def get(hmap, key, default = None):
	i, k, v = get_slot(hmap, key, default = default)
	return v
	
# set the key to the value and replace existing value
def set(hmap, key, value):
	bucket = get_bucket(hmap, key)
	i, k, v = get_slot(hmap, key)
	
	# if key exists, replace it
	if i >= 0:
		bucket[i] = (key, value)
		
	# if key doesn't exist, append to create it
	else:
		bucket.append((key, value))
		
# delete a given key from the Map
def delete(hmap, key):
	bucket = get_bucket(hmap, key)
	
	for i in xrange(len(bucket)):
		k, v = bucket[i]
		if key == k:
			del bucket[i]
			break
			
# print out the Map
def list(hmap):
	for bucket in hmap:
		if bucket:
			for k, v in bucket:
				print k, v