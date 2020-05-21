---
url: bms4pv
---

# R-dplyr

```R
library(tidyr)<br />
library(dplyr)

df <- data.frame(x = c(NA, "a.b", "a.d", "b.c","a-b"))<br />
df %>% separate(x, c("A", "B"),'-')
```
