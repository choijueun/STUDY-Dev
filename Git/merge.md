# Merge

> git merge (branch명)

명시한 branch를 현재 branch로 merge   
<br/>

# Conflict

> git status

git status 확인   
<br/>

```
# vi example2.txt
<<<<<<< HEAD
git merge 실행한 branch
=======
git merge 대상 branch
>>>>>>> develop
```

> main

HEAD 내용만 남김

