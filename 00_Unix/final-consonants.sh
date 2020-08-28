sed 's/[^a-zA-Z]\+/\n/g' | grep -i '^[a-z]' | sed 's/[a-zA-Z]*[aeiouAEIOU]//g' | sort | uniq -c | sort -nr
