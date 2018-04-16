#!/usr/bin/awk -f

function cmp_str_idx(i1, v1, i2, v2)
{
    # string index comparison, ascending order
    if (i1 < i2)
        return -1
    return (i1 != i2)
}

BEGIN {
	if (ARGC < 3) {
		print "Usage: tsv2bow.awk <TSV> <VOCAB>"      >"/dev/stderr"
		print "    <TSV>:   tab-separated input file" >"/dev/stderr"
		print "    <VOCAB>: vocabulary file"          >"/dev/stderr"
		exit 1
	}

	FS = "\t"

	print "Reading vocabulary..." >"/dev/stderr"
}

# Read the vocabulary
NR == FNR {
	vocab[$1] = 1
	next
}

FNR == 1 {
	print "Processing data..." >"/dev/stderr"
}

FNR % 100 == 0 { print "Line " + FNR >"/dev/stderr" }

{
	# Create the set of tokens
	split($2, tok_split, " ")
	for (i in tok_split) {
		tokens[tok_split[i]]
	}

	# Create the BOW vector
	#PROCINFO["sorted_in"] = "@ind_num_asc"
	for (word in vocab) {
		if (word in tokens) {
			printf(" 1")
		} else {
			printf(" 0")
		}
	}
	print ""
}
