# Branch

> git branch   

git branch 확인
- -a
- -r
- -v : 마지막 commit msg
- --merged: merged list
- --no-merged: no-merged list
<br/>
   
> git branch (branch명)   

git branch 생성
- -c: 생성 후 branch 변경
<br/>
   
> git switch (branch명)   

git branch 변경   
<br/>
   
> git push --set-upstream (remote명) (branch명)   

remote 명시
- Auto: git config --global push.default current
<br/>
   
> git branch -d (branch명)   

git branch 삭제   
<br/>
   
> git branch -D (branch명)   

git branch 강제 삭제   
<br/>

> git log

현재 branch 수정 내역
- --branches: local의 모든 branch 수정 내역
- --graph: 시각적으로 표시
- --oneline: branch와 msg만 간략하게 표시
<br/>

> git log (branch명1)..(branch명2)

branch와 master branch의 commit 차이
- -p: 수정 내역 표시
<br/>

> git diff (branch명1)..(branch명2)

두 branch 차이점 간략 표시   
<br/>
