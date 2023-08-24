#!/usr/bin/env bash
# Generate author list for this project

echo '# List of all individuals who have contributed to this repository'\
 > AUTHORS
echo >> AUTHORS
echo "$(git log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf)" >> AUTHORS
