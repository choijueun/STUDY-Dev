# Typing

type hint를 언어 차원에서 지원

**3.9를 기점으로 메서드가 달라짐**

## List, Dict, Tuple, Set

> List[int] = [1,2,3]

> Dict[str, str] = { 'Name': 'CJE', 'Email', 'songjueun815@gmail.com' }

> Tuple[int, str, bool] = (12, "Tue", True)

> Set[str] = {'A', 'B', 'C'}

### Final

`상수`: 재할당 불가능

> Final[int] = 0

### Union

`여러 타입` 허용

> Union[int, float]

### Optional

`None` 허용

> Optional[int]

= Union[int, None]

### Callable

`함수`

...?

### 타입 추상화

> Iterable[int]