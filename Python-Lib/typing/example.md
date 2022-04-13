### var

    age: int = 20
    name: str = '최주은'

<br/>

### function

    def temp(num: int) -> bool:
        if num == 1:
            return true

<br/>

### Container

    from typing import List
    numList: List[int] = [1,2,3,4,5]

    <br/>

    from typing import Set
    numSet: Set[int] = {1,2,3,4,5}

    <br/>

    from typing import Dict
    numDict: Dict[int, str] = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e'}

    <br/>

<br/>

### Final

    from typing import Final
    SOLD_OUT: Final[int] = 10

<br/>

### Union

    from typing import Union

    def temp(val: Union[int, float]):
        return val

    temp(1)
    temp(1.5)

<br/>

### Optional

    from typing import Optional

    def temp(val: Optional[int]) -> bool:
        if val is None:
            return False
        else:
            return True

    temp(1)
    temp(None)

<br/>

### Callable

    from typing import Callable

    def temp(func: Callable[[str], int], val: str) -> None:
        print(func(val))

    def temp2(val: str) -> int:
        return int(val)

    temp(temp2, '20')

<br/>

### Custom Type

    from typing import NewType

    CustomType = NewType('CustomType', int)

    def temp(var: CustomType):
        print(var)
        print(type(var))

<br/>

    # 1
    # <class 'int'>

    num = CustomType(1)
    temp(num)

