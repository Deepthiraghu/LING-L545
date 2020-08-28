sed 's/[^a-zA-Z]\+/\n/g' | grep -i '^[^aeiou]' | sed 's/[aeiouyAEIOU][^aeiouyAEIOU]*//g' | sort | uniq -c | sort -nr

