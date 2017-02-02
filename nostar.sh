f=/tmp/$(date -Iseconds); wget 'https://api.github.com/search/repositories?q=forks>1&sort=forks&order=desc&since=daily' -O "$f" && less "$f"
