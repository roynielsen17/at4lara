---
id: 01HPT9HVQDD6M5XQGTP3QCDZC9
created: 2024-02-07T20:04
updated: 2024-02-16T18:05
---
# Converting a markdown file to PDF

What worked:

```
brew install pandoc
brew install basictex
eval "$(/usr/libexec/path_helper)"
pandoc README.md -f markdown -s -o applicationFramework-v0.0.1.pdf
open applicationFramework-v0.0.1.pdf 
```

# References:

https://stackoverflow.com/questions/9998337/how-to-print-from-github

https://github.com/jgm/pandoc/issues/7570

https://stackoverflow.com/questions/41604263/how-do-i-display-local-image-in-markdown




